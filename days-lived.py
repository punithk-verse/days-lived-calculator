import datetime
# ask for user input
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# checks through the valid dates,month #error handling 
try:
    given = datetime.date(year, month, day)
except ValueError:
    print("Invalid date! Please enter a correct date.")
    exit()

# Calculate days lived 
current = datetime.date.today()
days_lived = (current - given)

print(f"The number of days you lived: {days_lived}")
