#Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this
#  (of course the value 5 should be the calculated number instead):

# Constants
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

days_in_year = int(input("Enter the number of days in a year (365 for normal, 366 for leap year): "))

seconds_in_year = days_in_year * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

print(f"There are {seconds_in_year} seconds in a year with {days_in_year} days!")
