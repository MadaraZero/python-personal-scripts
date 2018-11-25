##  Students Assignment  ##
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

# class list (list of dictionaries)
#class_list = [lloyd, alice, tyler]

# Gets the average of any number list from student
def average(numbers):
  total = sum(numbers)
  total = float(total)
  total = total / len(numbers)
  return total

# Gets average of specific lists and divides them by their weight
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

# turns score in letter grade
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

# gets class average
def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

print "Class Average Score %s" % average(results)
print "Class Average Letter %s" % get_letter_grade(average(results))
print "Alice's Average %s" % get_letter_grade(get_average(alice))

students = [lloyd, alice, tyler]
print 83.8666666667
print get_letter_grade(83.8666666667)
