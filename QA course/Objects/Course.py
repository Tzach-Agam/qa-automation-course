class Course:
    def __init__(self, course_num, course_name, students_signed, students_max):
        self.course_num = course_num
        self.course_name = course_name
        self.students_signed = students_signed
        self.students_max = students_max

    def __str__(self):
        return f"All course info: course number: {self.course_num}\n" \
               f"course name: {self.course_name}\n" \
               f"number of pupils who singed: {self.students_signed}\n" \
               f"number of maximum students in the course: {self.students_max}"

    def sit_left(self):
        sits_left = self.students_max - self.students_signed
        return sits_left

    def new_students(self, new_students):
        if new_students <= self.sit_left():
        # sits_left = self.students_max - (self.students_signed + new_students)
        # if sits_left > 0:
            self.students_signed += new_students
            # return self.students_signed

My_course = Course(2077, "Computer science", 1000, 3000)
print(My_course)
My_course.new_students(1000)
print(My_course)
