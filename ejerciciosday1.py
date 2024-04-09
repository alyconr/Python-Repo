print("+" + 4 * "-" + "+" + "\n" + (("|" + " " * 4 + "|" + "\n") * 2)  + "+" + 4 * "-" + "+" + "\n" + (("|" + "\n") * 3)   )

print("+" + 4 * "-" + "+" + "\n" + "|" + " " * 4 + "|" + "\n" + "|" + " " * 4 + "|" + "\n" + "+" + 4 * "-" + "+" + "\n" + "|" + "\n" + "|" + "\n" +"|"  )

phrase = input("Enter a phrase: ")
print(phrase)

gradeA = int(input("Enter your gradeA: "))
gradeB = int(input("Enter your gradeB: "))
gradeC = int(input("Enter your gradeC: "))

average = ((int(gradeA) + int(gradeB) + int(gradeC)) / 3) * 55 / 100

final_exam = gradeB * 30 / 100

capstone_project = gradeC * 15 / 100

print(average + final_exam + capstone_project)


