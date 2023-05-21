from datetime import date, timedelta

def fill_days(start_date, end_date):
    current_date = start_date
    days_per_month = []

    while current_date <= end_date:
        days_in_month = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1) - current_date
        days_in_month = min(days_in_month.days, (end_date - current_date).days + 1)
        days_per_month.append((current_date.strftime("%B"), days_in_month))

        current_date = current_date.replace(day=1) + timedelta(days=32)
        current_date = current_date.replace(day=1)

    for month_name, days in days_per_month:
        print(f"{month_name}: {days} days")

    return days_per_month

