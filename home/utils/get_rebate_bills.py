def get_rebate_bills(rebate, period):
    period = int(period)
    if period == 1:
        short = rebate.period1_short
        long = rebate.period1_long
        high_tea = rebate.period1_high_tea
        bills = rebate.period1_bill
    elif period == 2:
        short = rebate.period2_short
        long = rebate.period2_long
        high_tea = rebate.period2_high_tea
        bills = rebate.period2_bill
    elif period == 3:
        short = rebate.period3_short
        long = rebate.period3_long
        high_tea = rebate.period3_high_tea
        bills = rebate.period3_bill
    elif period == 4:
        short = rebate.period4_short
        long = rebate.period4_long
        high_tea = rebate.period4_high_tea
        bills = rebate.period4_bill
    elif period == 5:
        short = rebate.period5_short
        long = rebate.period5_long
        high_tea = rebate.period5_high_tea
        bills = rebate.period5_bill
    elif period == 6:
        short = rebate.period6_short
        long = rebate.period6_long
        high_tea = rebate.period6_high_tea
        bills = rebate.period6_bill
    rebate_bill = [short, long, high_tea, bills]
    return rebate_bill
