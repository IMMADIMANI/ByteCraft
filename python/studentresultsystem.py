class Student:
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"

s1 = Student("Ravi", 75)
print(Student.grade_category(s1.marks))
s1.result()