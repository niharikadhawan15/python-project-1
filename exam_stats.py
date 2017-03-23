grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


# The method 'print_grades' accept the grades as argument.
def print_grades(grades):
    for grade in grades:
        print grade


# The method 'grades_sum' return the sum of all the grades.
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


# The method 'grades_average' return average of all grade scores.
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


# The method 'grade_variance'return variance of grade scores.
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    return variance / len(scores)


# The method 'grade_standard_deviation'return standard variation of grades.
def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

# It prints all the grades.
print "All the grades are \n", print_grades(grades)

# It prints sum of grades.
print "Sum of grades is ", grades_sum(grades)

# It prints the average grade.
print "Average grade is ", grades_average(grades)

# It prints the variance
print "Variance is ", grades_variance(grades)

# It prints standard deviation of grades
print "Standard deviation is ", grades_std_deviation(variance)