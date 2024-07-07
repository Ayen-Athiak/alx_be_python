Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match Priority:
    case"high":
        print("you really need to squeeze time for you work")
    case "medium":
        print("just work according this week")
    case "low":
        print("you still have time")



if time_bound.lower()== "yes":
    print("finish your work befor you sleep today")
else:print("no need to rush")