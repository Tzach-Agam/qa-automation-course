class Student_2:
    def __init__(self,id, name):
        if type(id) != int:
            raise TypeError("id needs to be type int!!!")
        if type(name) != str:
            raise TypeError("name has to be type str!!!")
        if id < 1000:
            raise TypeError("id have to be more than four numbers!!!")
        for i in name:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        self.id = id
        self.name = name
        self.dic_grades = {}

    def __repr__(self):
        return f"All student info:\n"\
               f"Id: {self.id}\n"\
               f"Name: {self.name}\n"\
               f"All grades: {self.dic_grades}\n"

    # the method will get a subject and grade and will ass it to the dictionary
    def add_grade(self, subject_name, grade = 0):
        if type(subject_name) != str:
            raise TypeError("subject name has to be string")
        if type(grade) != int:
            raise TypeError("grade has to be type int")
        self.dic_grades[subject_name] = grade

    # this method will add a factor to the grade
    def calc_factor(self, subject_name, factor):
        if type(factor) != int:
            raise TypeError("factor has to be a number")
        if (factor * self.dic_grades[subject_name] / 100 + self.dic_grades[subject_name]) <= 100:
            self.dic_grades[subject_name] = factor * self.dic_grades[subject_name] / 100 + self.dic_grades[subject_name]
        else:
            self.dic_grades[subject_name] = 100

    # This method wil give the avarage grade of the student
    def average(self):
        sum_grades = 0
        for grade in self.dic_grades.values():
            sum_grades += grade
        average_grade = sum_grades / len(self.dic_grades)
        return average_grade

    # This method will compare between two students
    def __eq__(self, other):
        if type(other) != Student_2:
            raise TypeError("other must be type Student_2!!!")
        if self.id == other.id:
            return True
        else:
            return False
