def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_date(year, month, day):
    
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day += 1

    
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
        
       
        if month > 12:
            month = 1
            year += 1

    return year, month, day


year=int(input("enter the year in the range 1800 - 2024"))
month=int(input("enter the month in range of 1-12"))
day=int(input("enter the day in the range of 1-31"))
next_year, next_month, next_day = next_date(year, month, day)
print(f"The next date after {year}-{month:02}-{day:02} is {next_year}-{next_month:02}-{next_day:02}.")
