import csv
from datetime import date, timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.http import HttpResponse

from ..models.allocation import Allocation, Period
from ..models.students import LongRebate, Student


def fill_periods(email, start_date, end_date):
    print(f"Start date: {start_date}, End date: {end_date}")
    current_date = start_date
    days_per_period = []
    student = Student.objects.filter(email__iexact=email).last()
    for period in Period.objects.all():
        if (
            period.start_date <= current_date <= period.end_date
            and period.start_date <= end_date
            and Allocation.objects.filter(period=period, email=student).exists()
        ):
            days_in_period = (min(period.end_date, end_date) - current_date).days + 1
            days_per_period.append((period, days_in_period))
            current_date = current_date + timedelta(days=days_in_period)

    if current_date <= end_date:
        days_per_period.append((current_date, end_date))

    for period_no, days in days_per_period:
        print(f"{period_no}: {days} days")

    return days_per_period


def map_periods_to_long_rebate(
    longRebate: list[LongRebate],
    user: AbstractBaseUser | AnonymousUser,
    semesterName: str = "Autumn 2024",
):
    periods = Period.objects.filter(semester__name=semesterName)
    period_to_long_rebate_map = {period.Sno: {} for period in periods}
    periods_to_email = {period.Sno: [] for period in periods}
    for rebate in longRebate:
        for period in periods:
            if (
                rebate.start_date <= period.end_date
                and rebate.end_date > period.start_date
            ):
                start_date: date = max(rebate.start_date, period.start_date)
                end_date: date = min(rebate.end_date, period.end_date)
                if period_to_long_rebate_map[period.Sno].get(rebate.email) is None:
                    period_to_long_rebate_map[period.Sno][rebate.email] = 0
                period_to_long_rebate_map[period.Sno][rebate.email] += (
                    end_date - start_date
                ).days + 1
                periods_to_email[period.Sno].append(rebate.email)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="Rebate.csv"'

    writer = csv.writer(response)
    writer.writerow(["Email", "Period", "caterer", "Days"])

    for period_no, emails in periods_to_email.items():
        period = periods[period_no - 1]
        allocations = Allocation.objects.filter(Q(email__in=emails), period=period)
        for allocation in allocations:
            if (
                not user.is_superuser
                and not user.groups.filter(name="College Administration")
                and not user.username == allocation.caterer.name
            ):
                continue
            writer.writerow(
                [
                    allocation.email,
                    period_no,
                    allocation.caterer.name,
                    period_to_long_rebate_map[period_no][allocation.email],
                ]
            )

    return response
