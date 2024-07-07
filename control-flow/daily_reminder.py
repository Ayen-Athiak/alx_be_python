Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match Priority:

    case "medium":
        print("just work according this week")
    case "low":
        print("you still have time")
if time_bound== "yes":
    reminder = "Finish  math project ' is a high priority task that requires immediate attention today!"
    print( f"reminder : {reminder}")
else:print("no need to rush")