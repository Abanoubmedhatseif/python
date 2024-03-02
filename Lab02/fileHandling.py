fileData = open("./lab02/students.txt")

totalGrades = 0
numberOfStudents = 0
failedStudents = []

for line in fileData:
    name , grades = line.split()
    totalGrades += int(grades)
    numberOfStudents += 1
    if int(grades) < 60:
        failedStudents.append(name)
        
averageGrade = totalGrades/numberOfStudents

print(int(averageGrade))
print(failedStudents)

fileData.close()

