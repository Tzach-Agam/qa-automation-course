from unittest import TestCase, mock
from unittest.mock import patch
from Project_Students import Student_2
from Project_Course import Course_2

class TestCourse_2(TestCase):
    def setUp(self):
        print("The setup")
        self.course = Course_2(1, "History", 3)
        self.student = Student_2(2077, "tzach")

    # Test all valid __init__
    def test__init__valid(self):
        self.assertEqual(self.course.course_num, 1)
        self.assertEqual(self.course.course_name, "History")
        self.assertEqual(self.course.students_max, 3)
        self.assertEqual(self.course.dict_course, {})
        self.assertEqual(self.course.lst_student, [])

    # Test all invalid __init__
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_course = Course_2("abc", "History")
        with self.assertRaises(TypeError):
            invalid_course = Course_2(1, 10)
        with self.assertRaises(TypeError):
            invalid_course = Course_2(1, "History", 101)

    # Test all defaults __init__
    def test__init__default(self):
        course = Course_2(1, "History")
        self.assertEqual(course.students_max, 100)

    # Test valid add_student function
    def test_add_student(self):
        self.assertTrue(self.course.add_student(self.student))
        self.assertEqual(self.course.lst_student, [self.student])
        print(self.course.lst_student)

    # Test if add_student function doesnt add more students than it should
    def test_add_student_max(self):
        course = Course_2(1, "History", 3)
        student1 = Student_2(2077, "tzach")
        student2 = Student_2(3077, "noa")
        student3 = Student_2(4077, "bill")
        student4 = Student_2(5077, "anat")
        lst_student = [student1, student2, student3]
        for student in lst_student:
            course.add_student(student)
        self.assertFalse(course.add_student(student4))

    # Test if the student is valid
    def test_invalid_student(self):
        course = Course_2(1, "History", 3)
        with self.assertRaises(TypeError):
            invalid_course = course.add_student("shimi")

    # Test if the factor is added to all students
    def test_add_factor(self):
        course = Course_2(1, "History", 3)
        student1 = Student_2(2077, "tzach")
        student2 = Student_2(3077, "noa")
        student1.add_grade("medieval", 80)
        student2.add_grade("medieval", 80)
        course.add_student(student1)
        course.add_student(student2)
        course.add_factor("medieval", 20)
        self.assertEqual(student1.dic_grades, {"medieval":96})
        self.assertEqual(student2.dic_grades, {"medieval":96})
        # Test negative factor
        course.add_factor("medieval", -20)
        self.assertEqual(student1.dic_grades, {"medieval":76.8})
        self.assertEqual(student2.dic_grades, {"medieval":76.8})
        # Test default factor
        course.add_factor("medieval", 60)
        self.assertEqual(student1.dic_grades, {"medieval":100})
        self.assertEqual(student2.dic_grades, {"medieval":100})

    # Test if the add factor function doesnt add a factor that is invalid
    def test_add_factor_invalid(self):
        course = Course_2(1, "History", 3)
        student1 = Student_2(2077, "tzach")
        student2 = Student_2(3077, "noa")
        student1.add_grade("medieval", 80)
        student2.add_grade("medieval", 80)
        course.add_student(student1)
        course.add_student(student2)
        with self.assertRaises(TypeError):
            invalid_factor = course.add_factor("medieval", "aaa")

    # Test if del function can delete a student from list
    def test_del_student(self):
        course = Course_2(1, "History", 3)
        student1 = Student_2(2077, "tzach")
        student2 = Student_2(3077, "noa")
        course.add_student(student1)
        course.add_student(student2)
        course.del_student(student1)
        self.assertEqual(course.lst_student, [student2])
        course.del_student(student2)
        self.assertTrue(course.lst_student == [])

    # Test if function does gives a list of averages grades for each student
    def test_averages(self):
        course = Course_2(1, "History", 3)
        student1 = Student_2(2077, "tzach")
        student2 = Student_2(3077, "noa")
        student3 = Student_2(4077, "bill")
        student4 = Student_2(5077, "anat")
        student1.dic_grades = {"medieval":90, "new age":90, "old age":90}
        student2.dic_grades = {"medieval":40, "new age":40, "old age":40}
        student3.dic_grades = {"medieval":80, "new age":80, "old age":80}
        lst_student = [student1, student2, student3, student4]
        for student in lst_student:
            course.add_student(student)
        self.assertEqual(course.averages(), [90, 40, 80])

    # Test if the weak students function returns right index
    @mock.patch('Project_Course.Course_2.averages', return_value=[90, 40, 80])
    def test_weak_students(self, mock_averages):
        self.assertEqual(self.course.weak_students(), 1)

    # Another test for weak student with different method
    def test_weak_students_with(self):
        with patch("Project_Course.Course_2.averages") as mock_averages:
            mock_averages.return_value = [90, 40, 80]
            self.assertEqual(self.course.weak_students(), 1)

            mock_averages.return_value = [40, 40, 80]
            self.assertEqual(self.course.weak_students(), [0, 1])











