from Project_Students import Student_2
class Course_2:
    def __init__(self, course_num, course_name, students_max = 100):
        if type(course_num) != int:
            raise TypeError("course number needs to be type int!!!")
        if type(course_name) != str:
            raise TypeError("course name needs to be type str!!!")
        if students_max > 100:
            raise TypeError("student max cannot be more than 100!!!")
        self.course_num = course_num
        self.course_name = course_name
        self.students_max = students_max
        self.dict_course = {}
        self.lst_student = []

    def __repr__(self):
        return f"All course information: course number: {self.course_num}\n" \
               f"course name: {self.course_name}\n" \
               f"maximum students in the course: {self.students_max}\n" \
               f"The course dictionary:{self.dict_course}\n" \
               f"All students: {self.lst_student}"

    # This method will add a student to the student list
    def add_student(self, student):
        if type(student) != Student_2:
            raise TypeError("the student has to be a valid student!!!")
        if len(self.lst_student) < self.students_max:
            self.lst_student.append(student)
            return True
        else:
            return False

    # This method will add the factor to all of the student grades
    def add_factor(self, subject, factor):
        if type(factor) != int:
            raise TypeError("factor has to be a number!!!")
        for student in self.lst_student:
            student.calc_factor(subject, factor)

    # This method will delete student object from the list
    def del_student(self, student):
        if student in self.lst_student:
            self.lst_student.remove(student)

    # This method will return a list with all of the students average grades
    def averages(self):
        lst_averages = []
        for student in self.lst_student:
            grade = student.average()
            lst_averages.append(grade)
        return lst_averages

    # This method will return the students with the weakest average grade
    def weak_students(self):
        lst_averages = self.averages()
        minimum_avergae = min(lst_averages)
        if lst_averages.count(minimum_avergae) > 1:
            lst_min = []
            for i in range(len(lst_averages)):
                if lst_averages[i] == minimum_avergae:
                    lst_min.append(i)
            return lst_min
        else:
            return lst_averages.index(minimum_avergae)























