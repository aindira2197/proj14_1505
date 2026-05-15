students = ["Ali", "Vali", "Sami", "Hasan"]

file = open("students.txt", "w")

for student in students:
    file.write(student + "\n")

file.close()

file = open("students.txt", "r")

data = file.readlines()

for line in data:
    print(line.strip())

file.close()
