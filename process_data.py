import csv
from utils import calculate_average, assign_grade

def process_grades():
    students = []

    # Read student data from CSV
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, math, science, english = row
            scores = list(map(int, [math, science, english]))  # Convert scores to integers
            average = calculate_average(scores)
            grade = assign_grade(average)
            students.append([name, math, science, english, average, grade])

    # Save processed data to a new CSV file
    with open('student_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Science', 'English', 'Average', 'Grade'])  # Keep same column names
        writer.writerows(students)

    print("Results saved to student_results.csv")