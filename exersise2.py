def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: #we want the year to be divided by 400, instead of 4000
                return True
            else:
                return False
        else:
            return True
    else:
        return False