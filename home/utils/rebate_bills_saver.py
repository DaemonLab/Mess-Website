from ..models import Caterer,LongRebate, LeftLongRebate,Student, StudentBills,CatererBills, Period,Semester, Allocation
from django.db.models.query import QuerySet

def save_short_bill(student,period,days,high_tea,caterer):
    rebate = StudentBills.objects.get(email=student,semester=period.semester)
    print(caterer,caterer,student)
    catererBill = CatererBills.objects.get(caterer=caterer)
    amount = days*115
    if(high_tea):
        amount = amount + days*15
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


def save_long_bill(student,days_per_period,j):
    print (student,days_per_period,j)
    for period,days in days_per_period:
        if not isinstance(period, QuerySet):
            rebate = StudentBills.objects.get(email=student,semester=period.semester)
            allocation = Allocation.objects.get(email=student,period=period)
            caterer = Caterer.objects.get(name=allocation.caterer)
            catererBill = CatererBills.objects.get(caterer=caterer,semester=period.semester) 
            days*=j
            amount = days*115
            if(allocation.high_tea):
                amount = amount + days*15
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
            if(j==1):
                left,created = LeftLongRebate.objects.get_or_create(email=str(student.email))
                left.start_date = period
                left.end_date = days
                left.save()
                print("left",left.start_date)
            else:
                LeftLongRebate.objects.filter(email=str(student.email),start_date=period).delete()    
                print("deleted")
                break
