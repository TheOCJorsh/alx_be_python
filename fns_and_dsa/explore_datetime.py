from datetime import datetime, timedelta

# Display current time in raw & formatted form.

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
display_current_datetime()

# Display future time

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
calculate_future_date()