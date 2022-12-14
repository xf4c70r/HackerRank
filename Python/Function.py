def is_leap(year):
    if(1990<=year<=10**5):
        if(year%4==0 and (year % 400 == 0 or year % 100 != 0)):
            leap = True
        else:
            leap = False
    return leap
