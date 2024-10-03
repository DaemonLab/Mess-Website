from django.utils import timezone
from home.models.students import Student, LongRebate, TodayRebate, Allocation


def is_student_on_rebate(student: Student, allocation: Allocation):
    """
    This function checks if the student is on rebate or not
    """
    long_rebate = LongRebate.objects.filter(email=student)
    today = timezone.localtime().date()

    rebate_exists = TodayRebate.objects.filter(allocation_id=allocation.id).exists()

    if rebate_exists:
        return True

    for r in long_rebate:
        if r.start_date <= today <= r.end_date and r.approved:
            return True
    return False
