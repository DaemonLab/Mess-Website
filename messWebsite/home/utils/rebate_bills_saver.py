from ..models import Caterer,RebateSpring23,RebateAutumn23,LongRebate,CatererBillsAutumn22,CatererBillsAutumn23,CatererBillsSpring23, AllocationSpring23, AllocationAutumn23, AllocationAutumn22, PeriodAutumn22, PeriodAutumn23, PeriodSpring23,LeftLongRebate,Student

def save_short_bill(email,period,days,high_tea,caterer):
    student=Student.objects.get(email=email)
    caterer_obj = Caterer.objects.get(name=caterer)
    rebate = RebateSpring23.objects.get(email=student)
    print(caterer_obj,caterer,student)
    catererBill = CatererBillsSpring23.objects.get(caterer=caterer_obj)
    amount = days*115
    if(high_tea):
        amount = amount + days*15
    print (email,period,days,high_tea, catererBill)
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
            catererBill.period6_bills = catererBill.period5_bills + amount
            rebate.save()
            catererBill.save()


def save_long_bill(email,days_per_period,j):
    print (email,days_per_period,j)
    student = email
    rebate = RebateSpring23.objects.get(email=student)
    for period_no,days in days_per_period:
        if(period_no <7):
            period = PeriodSpring23.objects.get(Sno=period_no)
            allocation = AllocationSpring23.objects.get(roll_no=student,month=period)
            caterer = Caterer.objects.get(name=allocation.caterer_name)
            catererBill = CatererBillsSpring23.objects.get(caterer=caterer) 
            days*=j
            amount = days*115
            if(allocation.high_tea):
                amount = amount + days*15
        match period_no:
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
                catererBill.period6_bills = catererBill.period5_bills + amount
                rebate.save()
                catererBill.save()
            case 7:
                if(j==1):
                    left,created = LeftLongRebate.objects.get_or_create(email=email)
                    left.start_date = days
                    left.save()
                    print("left",left.start_date)
                else:
                    LeftLongRebate.objects.get(email=email,start_date=days).delete()
            case 8:
                left,created = LeftLongRebate.objects.get_or_create(email=email)
                left.end_date = days
                left.save()
