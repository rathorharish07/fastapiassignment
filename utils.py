import datetime

# find working days
def find_working_days(start_date, end_date):
    weekend_days = [5, 6] # assuming Saturday and sunday as weeekend
    working_days = 0
    while start_date <= end_date:
        # Check if the current day is a weekend day
        if start_date.weekday() not in weekend_days:
            working_days += 1
        # Move to the next day
        start_date += datetime.timedelta(days=1)
    return working_days