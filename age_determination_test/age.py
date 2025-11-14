def categorize_byAge(age):
    if age > 0 and age <= 9:
        return "Child"
    elif age > 9 and age <= 18:
        return "Teenager"
    elif age > 18 and age <= 64:
        return "Adult"
    elif age > 64 and age <= 120:
        return "Golden Age"
    elif age > 120:
        return f"Invalid age: {age}"