from datetime import date, timedelta
from ..models.Semesters.spring23 import PeriodSpring23,AllocationSpring23

def fill_periods(email,start_date, end_date):
    print(f"Start date: {start_date}, End date: {end_date}")
    current_date = start_date
    days_per_period = []

    for period in PeriodSpring23.objects.all():
        if period.start_date <= current_date <= period.end_date and period.start_date <= end_date and AllocationSpring23.objects.filter(month=period,roll_no=email).exists():
            days_in_period = min((period.end_date - current_date).days + 1, (end_date - current_date).days + 1)
            days_per_period.append((period.Sno, days_in_period))
            current_date = current_date + timedelta(days=days_in_period)
    
    if(current_date <= end_date and (end_date - current_date).days + 1 >0):
        days_per_period.append((7, current_date))
        days_per_period.append((8, end_date))
    
    for period_no, days in days_per_period:
        print(f"{period_no}: {days} days")

    return days_per_period

