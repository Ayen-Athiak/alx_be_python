import datetime
import pytz

def display_current_datetime():
    current_date = datetime.datetime.now(tz=pytz.UTC)
    print(current_date)

    def calculate_future_date():
        number_day = int(input("Enter the number of days to add to the current date:"))
        future_date = datetime.timedelta(number_day)
        print(future_date + current_date)
    calculate_future_date()
display_current_datetime()




