class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def checkPass(self):
        if 70 <= self.grade <= 100:
            return True
        elif 0 <= self.grade < 70:
            return False

    def Update_grade(self, factor):
        if self.grade + factor <= 100:
            self.grade += factor

    def show(self):
        print(f"All info on the student:\n"
              f"id: {self.id}"
              f" name: {self.name}"
              f" grade: {self.grade}")

The_student = Student(207795360, "Tzach Agam", 90)
if The_student.checkPass():
    print("GOOD! THE STUDENT PASSED!")
else:
    print("FAILED!!")
The_student.show()

