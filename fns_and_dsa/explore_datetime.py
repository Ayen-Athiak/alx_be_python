import datetime  # Ensure datetime module is imported

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    number_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now().date()
    delta = datetime.timedelta(days=number_days)  # Corrected timedelta usage
    future_date = current_date + delta
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after adding {number_days} days: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
