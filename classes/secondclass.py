class Student:
    def __init__(self, name, grade1, grade2):
        self.__name = name
        self.__grade1 = grade1
        self.__grade2 = grade2

    def get_average_grade(self):
        return (self.__grade1 + self.__grade2) / 2
    
    def show_info(self):
        print(f"Name: {self.__name}\nGrade 1: {self.__grade1}\nGrade 2: {self.__grade2}\nAverage Grade: {self.get_average_grade()}")

    def __str__(self):
        return f"Name: {self.__name}\n Average Grade: {self.get_average_grade()}"


s = Student("John", 90, 80)
s.show_info()
print(s)