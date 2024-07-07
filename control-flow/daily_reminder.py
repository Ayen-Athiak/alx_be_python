task = input("do you have task this week")
priority = input("task’s priority (high, medium, low)")
time_bound = input(" task is time-bound (yes or no)")
match priority:
    case"high":
        print("you really need to squeeze time for you work")
    case "medium":
        print("just work according this week")
    case "low":
        print("you still have time")
    case _:print("just be patient")


if time_bound.lower()== "yes":
    print("finish your work befor you sleep today")
else:print("no need to rush")