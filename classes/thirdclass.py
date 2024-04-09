from tabulate import tabulate

class Student:
    institution = "Sena"
    number_of_students = 0

    def __init__(self, name, grade1, grade2):
        self.__name = name
        if not (0 <= grade1 <= 5) or not (0 <= grade2 <= 5):
            raise ValueError("Grade must be between 0 and 5")
        self.__grade1 = grade1
        self.__grade2 = grade2
        Student.number_of_students += 1

    def get_average_grade(self):
        return (self.__grade1 + self.__grade2) / 2
    
    def get_info_list(self):
        return [self.__name, self.__grade1, self.__grade2, self.get_average_grade(), Student.institution]

    def show_info(self):
        print(
            f"Name: {self.__name}\nGrade 1: {self.__grade1}\nGrade 2: {self.__grade2}\nAverage Grade: {self.get_average_grade()}\nInstitution: {Student.institution}"
        ) 

    def __str__(self):
        return f"Name: {self.__name}\nAverage Grade: {self.get_average_grade()}"

    @classmethod
    def get_number_of_students(cls):
        return cls.number_of_students

    @classmethod
    def change_institution(cls, institution):
        cls.institution = institution

    @staticmethod

    def  show_scale():
        table = [
            ["Grade", "Description"],
            ["0 to 2.9", "Low"],
            ["3 to 3.9" , "Satisfactory"],
            ["4 to 4.5", "Good"],
            ["4.6 to 5", "Very Good"],
            ]

        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
        


try:
    students = []
    while True:
        s_name = input("Enter Student name: ")
        s_grade1 = float(input("Enter Student grade 1: "))
        s_grade2 = float(input("Enter Student grade 2: "))
        institution = input("Enter Student institution: ")
        new_student = Student(s_name, s_grade1, s_grade2)
        Student.change_institution(institution)
        students.append(new_student)
        add_more = input("Do you want to add more students? (yes/no): ").lower()
        if add_more != 'yes':
            break

    data = [student.get_info_list() for student in students]
    headers = ["Name", "Grade 1", "Grade 2", "Average Grade", "Institution"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    Student.show_scale()
    print(f"Number of students: {Student.get_number_of_students()}")

except ValueError as e:
    print(f"Error value: {e}")
