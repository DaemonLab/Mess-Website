from django.utils import timezone

from home.models.students import Allocation, LongRebate, Rebate, Student


def is_student_on_rebate(student: Student, allocation: Allocation):
    """
    This function checks if the student is on rebate or not
    """
    today = timezone.localtime().date()

    # Check if there is a ShortRebate for the given allocation
    if Rebate.objects.filter(
        allocation_id=allocation,
        start_date__lte=today,
        end_date__gte=today,
        approved=True,
    ).exists():
        return True

    # Check if there is an approved LongRebate for the student within the date range
    return LongRebate.objects.filter(
        email=student, start_date__lte=today, end_date__gte=today, approved=True
    ).exists()
