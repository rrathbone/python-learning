"""3 dictionaries with the same keys
Decimal points are needed so grades are stored as floats."""
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

"""This function takes a list of numbers and returns the average.
total stores the sum of all the numbers as a float
returns the total divided by the length of the numbers"""
def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)


"""get_average takes the student dictionary amd returns the weighted average.
The average function is called upon the specified keys from the student
dictionary. The results are stored to variables as a float.
Each variable is then multiplied by its weight and added together. """
def get_average(student):
    homework = float(average(student['homework']))
    quizzes = float(average(student['quizzes']))
    tests = float(average(student['tests']))
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


"""The results from the get_average function are appended to a new list.
This list is then passed into the average function."""
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

#students lists stores the 3 dictionaries
students = [lloyd, alice, tyler]

#prints the class average
print get_class_average(students)
#prints the grade that corresponds to the class average
print get_letter_grade(get_class_average(students))
