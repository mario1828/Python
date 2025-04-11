def calculate_average(scores):
    """Calculates the average of scores and rounds to 2 decimal places."""
    return round(sum(scores) / len(scores), 2)

def assign_grade(avg):
    """Assigns a grade based on the average score using normal if-else statements."""
    if avg >= 85:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 65:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'