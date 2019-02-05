#inital ifelse practice in python
today = "Wednesday"
if today == "Tuesday":
  print("We get to write code!")
else:
  print("Time to learn Scrum!")

  #modified
today = "Saturday"
code_days = ["Tuesday", "Thursday"]
scrum_days = ["Monday", "Wednesday", "Friday"]

if today in code_days:
  print("We get to write code!")
elif today in scrum_days:
  print("Time to learn Scrum!")
else:
  print("Time to relax!")
#more if else checkes the grade based off the num in class

gradeSum = 0
totalGrades = int(input("Enter number of grades that are to be assessed: "))
gradeNum = totalGrades
while totalGrades > 0:
    num = int(input("Enter your numeric grade: "))
    if num >= 90:
        letter_grade = 'A'
    elif num >= 80:
        letter_grade = 'B'
    elif num >= 70:
        letter_grade = 'C'
    elif num >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    print("Your letter grade is " + letter_grade )
    gradeSum = num + gradeSum
    totalGrades = totalGrades -1
print ("Your class average is: ", int(gradeSum/gradeNum))