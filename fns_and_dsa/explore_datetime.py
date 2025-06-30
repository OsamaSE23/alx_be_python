from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime('%Y-%m-%d %H:%M:%S'))
def calculate_future_date(x):
    future_date = datetime.now() + timedelta(x)
    print("Future date: ", future_date.strftime('%Y-%m-%d'))
display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(number_of_days)
