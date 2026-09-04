def day_of_week(day):
    match day:
        case "Monday":
            return "It is Monday"
        case "Tuesday":
            return "It is Tuesday"
        case "Wednesday":
            return "It is Wednesday"
        case "Thursday":
            return "It is Thursday"
        case "Friday":
            return "It is Friday"
        case "Saturday":
            return "It is Saturday"
        case "Sunday":
            return "It is Sunday"
        case _:#Functions to handle invalid inputs similar to the else statement in if-else statements
            return "Invalid day"

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False

        
n = input("Enter a day of the week: ")
result = day_of_week(n)
weekend = is_weekend(n)
print(result)
print(f"Is it the weekend? {weekend}")
