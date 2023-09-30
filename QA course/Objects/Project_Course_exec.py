from Project_Students import Student_2
from Project_Course import Course_2


course1 = Course_2(1, "HISTORY", 3)
student1 = Student_2(2077, "tzach")
student2 = Student_2(3077, "noa")
student3 = Student_2(4077, "bill")

student1.add_grade("medival", 60)
student1.add_grade("new age", 70)
student1.add_grade("old age", 70)

student2.add_grade("medival", 60)
student2.add_grade("new age", 60)
student2.add_grade("old age", 50)

student3.add_grade("medival", 40)
student3.add_grade("new age", 40)
student3.add_grade("old age", 50)

course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
index = course1.weak_students()
course1.del_student(course1.lst_student[index])
print(course1.weak_students())

# max_students = int(input("Enter how many students will be in the course: "))
# course1 = Course_2(1, "History", max_students)
# course_subject = int(input("Enter number of subjects for a course: "))
# for i in range(course_subject):
#     teacher = input("Enter the teachers name: ")
#     subject = input("Enter the subject: ")
#     course1.dict_course[subject] = teacher
# id_number = int(input("Enter id numbers: "))
# while id_number != 0 or len(course1.lst_student) <= course1.students_max:
#     name = input("Enter the students name: ")
#     student1 = Student_2(id_number, name)
#     for subject in course1.dict_course:
#         grade = int(input("Enter a grade: "))
#         student1.add_grade(subject, grade)
#         course1.add_student(student1)
#     id_number = int(input("Enter id numbers: "))
# print(course1)
# course1.add_factor("medival", 20)
# index = course1.weak_students()
# course1.del_student(course1.lst_student[index])
# print(course1)
# course1.add_factor("medival", 20)
# print(course1)