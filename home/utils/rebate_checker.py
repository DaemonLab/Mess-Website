from datetime import timedelta

from home.models import (
    GlobalConstants,
    LeftShortRebate,
    LongRebate,
    Rebate,
    StudentBills,
)


def count(start, end):
    """Counts the number of days of rebate applied"""
    sum = ((end - start).days) + 1
    return sum


def is_not_duplicate(student, new_rebate_start, new_rebate_end):
    """Checks if these dates are already applied for rebate"""
    try:
        for short_rebate in Rebate.objects.filter(email=student).all():
            if (
                short_rebate.start_date
                < new_rebate_start
                < short_rebate.end_date + timedelta(days=2)
            ) or (
                short_rebate.start_date - timedelta(days=2)
                < new_rebate_end
                < short_rebate.end_date
            ):
                return False
        for short_rebate in LeftShortRebate.objects.filter(email=student).all():
            if (
                short_rebate.start_date
                < new_rebate_start
                < short_rebate.end_date + timedelta(days=2)
            ) or (
                short_rebate.start_date - timedelta(days=2)
                < new_rebate_end
                < short_rebate.end_date
            ):
                return False
        for long_rebate in LongRebate.objects.filter(email=student).all():
            if (
                long_rebate.end_date
                > new_rebate_start
                > long_rebate.start_date - timedelta(days=2)
            ) or (
                long_rebate.start_date - timedelta(days=2)
                < new_rebate_end
                < long_rebate.end_date
            ):
                return False
        return True
    except Exception as e:
        print(e)
        return False


def max_days_rebate(student, start, end, period):
    """
    Checks what period rebate is being applied,
    if the rebate does not exceeds the set limit for that period approves the rebate and
    adds the rebate to student bills(Commented out this feature for now, as administration wants to approve it from its side before adding to student bills)
    """
    constants = GlobalConstants.objects.first()
    if not constants:
        constants = GlobalConstants.objects.create()

    limit = constants.short_rebate_period_limit

    student_bill, _ = StudentBills.objects.get_or_create(
        email=student, semester=period.semester
    )
    sum = count(start, end)
    match period.Sno:
        case 1:
            if student_bill.period1_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period1_short
        case 2:
            if student_bill.period2_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period2_short
        case 3:
            if student_bill.period3_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period3_short
        case 4:
            if student_bill.period4_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period4_short
        case 5:
            if student_bill.period5_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period5_short
        case 6:
            if student_bill.period6_short + sum <= limit:
                return -1
            else:
                return limit - student_bill.period6_short
