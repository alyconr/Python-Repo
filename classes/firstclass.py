class Student:
    def __init__(self, name, grade1, grade2):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2

    def get_average_grade(self):
        return (self.grade1 + self.grade2) / 2
    
    def show_info(self):
        print(f"Name: {self.name}\nGrade 1: {self.grade1}\nGrade 2: {self.grade2}\nAverage Grade: {self.get_average_grade()}")


s = Student("John", 90, 80)
s.show_info()

