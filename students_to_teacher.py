# Three dictionaries for three students each with keys: name, homework, quizzes, tests.
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


# Function 'average' accept an array parameter with integer elements and return average of the elements
def average(numbers):
    total = sum(numbers)
    total = float(total)
    a = total / len(numbers)
    return a


# Function'get_average'accept a student dictionary and return a sum of weighted averages of the homework, quizzes and tests key
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (homework * .1) + (quizzes * .3) + (tests * .6)


# Function'get_letter_grade' accept the score of the student and return the grade acheived by them.
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


get_letter_grade(get_average(lloyd))


# The method 'class_average' return average of all scores for all students.
def get_class_average(students):
    results = []
    for student in students:
        a = get_average(student)
        results.append(a)
    return average(results)


students = [lloyd, alice, tyler]
a = get_class_average(students)
print a
print get_letter_grade(a)
