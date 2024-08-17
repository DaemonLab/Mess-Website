from datetime import timedelta

from ..models.allocation import Allocation, Period
from ..models.students import Student


def fill_periods(email, start_date, end_date):
    print(f"Start date: {start_date}, End date: {end_date}")
    current_date = start_date
    days_per_period = []
    student = Student.objects.filter(email=email).last()
    for period in Period.objects.all():
        if (
            period.start_date <= current_date <= period.end_date
            and period.start_date <= end_date
            and Allocation.objects.filter(period=period, email=student).exists()
        ):
            days_in_period = min(
                (period.end_date - current_date).days + 1,
                (end_date - current_date).days + 1,
            )
            days_per_period.append((period, days_in_period))
            current_date = current_date + timedelta(days=days_in_period)

    if current_date <= end_date and (end_date - current_date).days + 1 > 0:
        days_per_period.append((current_date, end_date))

    for period_no, days in days_per_period:
        print(f"{period_no}: {days} days")

    return days_per_period
