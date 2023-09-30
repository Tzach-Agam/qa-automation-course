from unittest import TestCase
from Project_Students import Student_2

class TestStudent(TestCase):
    def setUp(self):
        print("The Setup")
        self.student = Student_2(2077, "tzach")

    # Test all valid cases of init
    def test__init__valid(self):
        self.assertEqual(self.student.id, 2077)
        self.assertEqual(self.student.name, "tzach")
        self.assertEqual(self.student.dic_grades, {})

    # Test invalid cases of init with wrong parameters
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_person = Student_2("abc", "tzach")
        with self.assertRaises(TypeError):
            invalid_person = Student_2(2077, 10)

    # Test invalid parameters
    def test_invalid__init__parameters(self):
        with self.assertRaises(TypeError):
            invalid_person = Student_2(1, "tzach")
        with self.assertRaises(TypeError):
            invalid_person = Student_2(2077, "tzach2")

    # Tests if the repr function doesnt return int
    # def test__repr__(self):
    #     self.assertTrue(type(print(self.student)) != int)

    # Test if the function adds the grade
    def test_add_grade(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval", 90)
        self.assertEqual(student1.dic_grades, {"medieval":90})
        # Test if the function adds more than one grade
        student1.add_grade("new age", 100)
        self.assertEqual(student1.dic_grades, {"medieval": 90, "new age":100})

    # Test if the function can change a grade
    def test_add_grade_same_subject(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval", 90)
        student1.dic_grades["medieval"] = 100
        self.assertEqual(student1.dic_grades, {"medieval": 100})

    # Test default grade in add_grade
    def test_add_grade_default(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval")
        self.assertEqual(student1.dic_grades, {"medieval":0})

    # Test wrong parameters for ass grade function
    def test_add_grade_wrong_parameters(self):
        student1 = Student_2(2077, "tzach")
        with self.assertRaises(TypeError):
            invalid_grade = student1.add_grade(10, 90)
        with self.assertRaises(TypeError):
            invalid_grade = student1.add_grade("medieval", "aaa")

    # Test add_factor function
    def test_calc_factor(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval", 80)
        student1.calc_factor("medieval", 20)
        self.assertEqual(student1.dic_grades, {"medieval":96})
        # Test negative factor
        student2 = Student_2(3077, "shimi")
        student2.add_grade("medieval", 80)
        student2.calc_factor("medieval", -20)
        self.assertEqual(student2.dic_grades, {"medieval":64})
        # Test a factor that gives a grade higher than 100
        student1.calc_factor("medieval", 50)
        self.assertEqual(student1.dic_grades, {"medieval":100})

    # Test add factor function with wrong parameters
    def test_calc_factor_wrong_factor(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval", 80)
        with self.assertRaises(TypeError):
            invalid_factor = student1.calc_factor("medieval", "aaa")

    # Test the avergae function
    def test_average(self):
        student1 = Student_2(2077, "tzach")
        student1.add_grade("medieval", 80)
        student1.add_grade("new age", 90)
        self.assertEqual(student1.average(), 85)
        student1.add_grade("old age", 100)
        self.assertEqual(student1.average(), 90)

    # Test __eq__ function True
    def test__eq__True(self):
        student2 = Student_2(2077, "shimi")
        self.assertTrue(self.student == student2)

    # Test __eq__ function False
    def test__eq__False(self):
        student2 = Student_2(3077, "shimi")
        self.assertFalse(self.student == student2)






