from home.models import RebateAutumn23, RebateSpring23,Rebate, LongRebate
def count(start, end):
    """Counts the number of days of rebate applied"""
    sum = ((end - start).days) + 1
    return sum

def is_not_duplicate(s,start,end,period):
    """Checks if these dates are already applied for rebate"""
    try:
        short = Rebate.objects.filter(email=str(s.email)).last()
        long = LongRebate.objects.filter(email=str(s.email)).last()
        if short.end_date> start+2 and long.end_date> start+2:
            return False
        else:
            return True
    except:
        return True

def is_present_autumn(s):
    """
    Checks if student is registered in the rebate bills of autumn semester,
    if not the function registers it with that email ID
    """
    try:
        student = RebateAutumn23.objects.get(email=s)
    except:
        print(Exception)
        student = RebateAutumn23(email=s)
        student.save()
    return student

def is_present_spring(s):
    """
    Checks if student is registered in the rebate bills of spring semester,
    if not the function registers it with that email ID
    """
    try:
        student = RebateSpring23.objects.get(email=s)
    except:
        print(Exception)
        print(2)
        student = RebateSpring23(email=s)
        student.save()
    return student

def check_rebate_spring(a, s, start, end, period):
    """
    Checks what month rebate is being applied,
    if the rebate doesnot exceeds 8 days for that month approves the rebate and
    adds the rebate to rebate bills
    """
    student = is_present_spring(s)
    sum = count(start, end)
    match period:
        case 1:
            if student.period1_short + sum <= 8:
                # student.january+=sum
                # student.highTeaJanuary = a.high_tea
                # student.save(update_fields=["january", "highTeaJanuary"])
                return -1
            else:
                return 8 - student.period1_short
        case 2:
            if student.period2_short + sum <= 8:
                # student.february+=sum
                # student.highTeaFebruary = a.high_tea
                # student.save(update_fields=["february", "highTeaFebruary"])
                return -1
            else:
                return 8 - student.period2_short
        case 3:
            if student.period3_short + sum <= 8:
                # student.march+=sum
                # student.highTeaMarch = a.high_tea
                # student.save(update_fields=["march", "highTeaMarch"])
                return -1
            else:
                return 8 - student.period3_short
        case 4:
            if student.period4_short + sum <= 8:
                # student.april+=sum
                # student.highTeaApril = a.high_tea
                # student.save(update_fields=["april", "highTeaApril"])
                return -1
            else:
                return 8 - student.period4_short
        case 5:
            if student.period5_short + sum <= 8:
                # student.may+=sum
                # student.highTeaMay = a.high_tea
                # student.save(update_fields=["may", "highTeaMay"])
                return -1
            else:
                return 8 - student.period5_short
        case 6:
            if student.period6_short + sum <= 8:
                # student.june+=sum
                # student.highTeaJune = a.high_tea
                # student.save(update_fields=["june", "highTeaJune"])
                return -1
            else:
                return 8 - student.period6_short
        # case default:
        #     return -1
        

def check_rebate_autumn(a,s,start,end,period):
    """
    Checks what month rebate is being applied,
    if the rebate doesnot exceeds 8 days for that month approves the rebate and
    adds the rebate to rebate bills
    """
    match period:
        case 1:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period1_short + sum <= 8:
                # student.july+=sum
                # student.highTeaJuly = a.high_tea
                # student.save(update_fields=["july", "highTeaJuly"])
                return -1
            else:
                return 8 - student.period1_short
        case 2:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period2_short + sum <= 8:
                # student.august+=sum
                # student.highTeaAugust = a.high_tea
                # student.save(update_fields=["august", "highTeaAugust"])
                return -1
            else:
                return 8 - student.period1_short
        case 3:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period3_short + sum <= 8:
                # student.september+=sum
                # student.highTeaSeptember = a.high_tea
                # student.save(update_fields=["september", "highTeaSeptember"])
                return -1
            else:
                return 8 - student.period3_short
        case 4:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period4_short + sum <= 8:
                # student.october+=sum
                # student.highTeaOctober = a.high_tea
                # student.save(update_fields=["october", "highTeaOctober"])
                return -1
            else:
                return 8 - student.period4_short
        case 5:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period5_short + sum <= 8:
                # student.november+=sum
                # student.highTeaNovember = a.high_tea
                # student.save(update_fields=["november", "highTeaNovember"])
                return -1
            else:
                return 8 - student.period5_short
        case 6:
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.period6_short + sum <= 8:
                # student.december+=sum
                # student.highTeaDecember = a.high_tea
                # student.save(update_fields=["december", "highTeaDecember"])
                return -1
            else:
                return 8 - student.period6_short
        # case default:
        #     return "something"
