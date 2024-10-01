from datetime import timedelta

from home.models.students import LongRebate, Rebate

from ..models import (
    Allocation,
    CatererBills,
    LeftLongRebate,
    Period,
    Student,
    StudentBills,
)


def save_short_bill(student, period, days, high_tea, caterer):
    rebate = StudentBills.objects.get(email=student, semester=period.semester)
    print(caterer, student)
    catererBill = CatererBills.objects.get(caterer=caterer, semester=period.semester)
    amount = days * 115
    if high_tea:
        amount = amount + days * 15
    match period.Sno:
        case 1:
            rebate.period1_high_tea = high_tea
            rebate.period1_short = rebate.period1_short + days
            rebate.period1_bill = rebate.period1_bill - amount
            catererBill.period1_bills = catererBill.period1_bills + amount
            rebate.save()
            catererBill.save()
        case 2:
            rebate.period2_high_tea = high_tea
            rebate.period2_short = rebate.period2_short + days
            rebate.period2_bill = rebate.period2_bill - amount
            catererBill.period2_bills = catererBill.period2_bills + amount
            rebate.save()
            catererBill.save()
        case 3:
            rebate.period3_high_tea = high_tea
            rebate.period3_short = rebate.period3_short + days
            rebate.period3_bill = rebate.period3_bill - amount
            catererBill.period3_bills = catererBill.period3_bills + amount
            rebate.save()
            catererBill.save()
        case 4:
            rebate.period4_high_tea = high_tea
            rebate.period4_short = rebate.period4_short + days
            rebate.period4_bill = rebate.period4_bill - amount
            catererBill.period4_bills = catererBill.period4_bills + amount
            rebate.save()
            catererBill.save()
        case 5:
            rebate.period5_high_tea = high_tea
            rebate.period5_short = rebate.period5_short + days
            rebate.period5_bill = rebate.period5_bill - amount
            catererBill.period5_bills = catererBill.period5_bills + amount
            rebate.save()
            catererBill.save()
        case 6:
            rebate.period6_high_tea = high_tea
            rebate.period6_short = rebate.period6_short + days
            rebate.period6_bill = rebate.period6_bill - amount
            catererBill.period6_bills = catererBill.period6_bills + amount
            rebate.save()
            catererBill.save()


def save_long_bill(email, days_per_period, j):
    student = Student.objects.filter(email=email).last()
    for period, days in days_per_period:
        if isinstance(period, Period):
            rebate = StudentBills.objects.get(email=student, semester=period.semester)
            allocation = Allocation.objects.get(email=student, period=period)
            catererBill = CatererBills.objects.get(
                caterer=allocation.caterer, semester=period.semester
            )
            days *= j
            amount = days * 115
            if allocation.high_tea:
                amount = amount + days * 15
            match period.Sno:
                case 1:
                    rebate.period1_high_tea = allocation.high_tea
                    rebate.period1_long = rebate.period1_long + days
                    rebate.period1_bill = rebate.period1_bill - amount
                    catererBill.period1_bills = catererBill.period1_bills + amount
                    rebate.save()
                    catererBill.save()
                case 2:
                    rebate.period2_high_tea = allocation.high_tea
                    rebate.period2_long = rebate.period2_long + days
                    rebate.period2_bill = rebate.period2_bill - amount
                    catererBill.period2_bills = catererBill.period2_bills + amount
                    rebate.save()
                    catererBill.save()
                case 3:
                    rebate.period3_high_tea = allocation.high_tea
                    rebate.period3_long = rebate.period3_long + days
                    rebate.period3_bill = rebate.period3_bill - amount
                    catererBill.period3_bills = catererBill.period3_bills + amount
                    rebate.save()
                    catererBill.save()
                case 4:
                    rebate.period4_high_tea = allocation.high_tea
                    rebate.period4_long = rebate.period4_long + days
                    rebate.period4_bill = rebate.period4_bill - amount
                    catererBill.period4_bills = catererBill.period4_bills + amount
                    rebate.save()
                    catererBill.save()
                case 5:
                    rebate.period5_high_tea = allocation.high_tea
                    rebate.period5_long = rebate.period5_long + days
                    rebate.period5_bill = rebate.period5_bill - amount
                    catererBill.period5_bills = catererBill.period5_bills + amount
                    rebate.save()
                    catererBill.save()
                case 6:
                    rebate.period6_high_tea = allocation.high_tea
                    rebate.period6_long = rebate.period6_long + days
                    rebate.period6_bill = rebate.period6_bill - amount
                    catererBill.period6_bills = catererBill.period6_bills + amount
                    rebate.save()
                    catererBill.save()
        else:
            if j == 1:
                left, created = LeftLongRebate.objects.get_or_create(
                    email=str(student.email)
                )
                left.start_date = period
                left.end_date = days
                left.save()
                print("left", left.start_date)
            else:
                LeftLongRebate.objects.filter(
                    email=str(student.email), start_date=period
                ).delete()
                print("deleted")
                break


def update_bills(email, allocation):
    try:
        period = allocation.period
        rebate_bill = StudentBills.objects.get(email, semester=period.semester)
        sno = period.Sno
        days = (period.end_date - period.start_date).days + 1
        high_tea = allocation.high_tea
        amount = 115
        if high_tea:
            amount = 130
        if sno == 1:
            rebate_bill.period1_high_tea = high_tea
            rebate_bill.period1_bill = amount * days
        elif sno == 2:
            rebate_bill.period2_high_tea = high_tea
            rebate_bill.period2_bill = amount * days
        elif sno == 3:
            rebate_bill.period3_high_tea = high_tea
            rebate_bill.period3_bill = amount * days
        elif sno == 4:
            rebate_bill.period4_high_tea = high_tea
            rebate_bill.period4_bill = amount * days
        elif sno == 5:
            rebate_bill.period5_high_tea = high_tea
            rebate_bill.period5_bill = amount * days
        elif sno == 6:
            rebate_bill.period6_high_tea = high_tea
            rebate_bill.period6_bill = amount * days
        rebate_bill.save()
    except Exception as e:
        print(e)


def fix_all_bills(
    student_bill: StudentBills, period_1: Period, period_2: Period, period_3: Period
):
    email = student_bill.email
    print(email)
    period_1_days = (period_1.end_date - period_1.start_date).days + 1
    period_2_days = (period_2.end_date - period_2.start_date).days + 1
    period_3_days = (period_3.end_date - period_3.start_date).days + 1
    rebates = Rebate.objects.filter(email=email, approved=True)
    short_rebates_per_period = [0, 0, 0]
    for rebate in rebates:
        if rebate.end_date < period_1.start_date:
            continue
        if rebate.start_date > period_3.end_date:
            continue
        if rebate.start_date <= period_1.start_date:
            rebate.start_date = period_1.start_date
        if rebate.end_date <= period_1.end_date:
            short_rebates_per_period[0] += (
                rebate.end_date - rebate.start_date
            ).days + 1
            continue
        rebate.start_date = period_1.end_date + timedelta(days=1)
        if rebate.end_date <= period_2.end_date:
            short_rebates_per_period[1] += (
                rebate.end_date - rebate.start_date
            ).days + 1
            continue
        rebate.start_date = period_2.end_date + timedelta(days=1)
        if rebate.end_date <= period_3.end_date:
            short_rebates_per_period[2] += (
                rebate.end_date - rebate.start_date
            ).days + 1
            continue
        short_rebates_per_period[2] += (period_3.end_date - rebate.start_date).days + 1
    long_rebates = LongRebate.objects.filter(email=email, approved=True)
    long_rebates_per_period = [0, 0, 0]
    for rebate in long_rebates:
        if rebate.end_date < period_1.start_date:
            continue
        if rebate.start_date > period_3.end_date:
            continue
        if rebate.start_date <= period_1.start_date:
            rebate.start_date = period_1.start_date
        if rebate.end_date <= period_1.end_date:
            long_rebates_per_period[0] += (rebate.end_date - rebate.start_date).days + 1
            continue
        rebate.start_date = period_1.end_date + timedelta(days=1)
        if rebate.end_date <= period_2.end_date:
            long_rebates_per_period[1] += (rebate.end_date - rebate.start_date).days + 1
            continue
        rebate.start_date = period_2.end_date + timedelta(days=1)
        if rebate.end_date <= period_3.end_date:
            long_rebates_per_period[2] += (rebate.end_date - rebate.start_date).days + 1
            continue
        long_rebates_per_period[2] += (period_3.end_date - rebate.start_date).days + 1
    print(short_rebates_per_period, long_rebates_per_period)
    student_bill.period1_short = short_rebates_per_period[0]
    student_bill.period2_short = short_rebates_per_period[1]
    student_bill.period3_short = short_rebates_per_period[2]
    student_bill.period1_long = long_rebates_per_period[0]
    student_bill.period2_long = long_rebates_per_period[1]
    student_bill.period3_long = long_rebates_per_period[2]
    student_bill.period1_high_tea = False
    student_bill.period2_high_tea = False
    student_bill.period3_high_tea = False
    student_bill.period1_bill = 115 * (
        period_1_days - short_rebates_per_period[0] - long_rebates_per_period[0]
    )
    student_bill.period2_bill = 115 * (
        period_2_days - short_rebates_per_period[1] - long_rebates_per_period[1]
    )
    student_bill.period3_bill = 115 * (
        period_3_days - short_rebates_per_period[2] - long_rebates_per_period[2]
    )
    student_bill.save()
