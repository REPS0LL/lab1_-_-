import unittest
from grading_system import grade_converter

class TestGradeConverter(unittest.TestCase):

    def test_A_grade(self):
        self.assertEqual(grade_converter(95), 'A')
        self.assertEqual(grade_converter(90), 'A')

    def test_B_grade(self):
        self.assertEqual(grade_converter(85), 'B')
        self.assertEqual(grade_converter(80), 'B')

    def test_C_grade(self):
        self.assertEqual(grade_converter(75), 'C')
        self.assertEqual(grade_converter(70), 'C')

    def test_D_grade(self):
        self.assertEqual(grade_converter(65), 'D')
        self.assertEqual(grade_converter(60), 'D')

    def test_E_grade(self):
        self.assertEqual(grade_converter(55), 'E')
        self.assertEqual(grade_converter(50), 'E')

    def test_F_grade(self):
        self.assertEqual(grade_converter(45), 'F')
        self.assertEqual(grade_converter(0), 'F')

    def test_invalid_score(self):
        self.assertEqual(grade_converter(-5), 'Invalid score')
        self.assertEqual(grade_converter(105), 'Invalid score')

if __name__ == '__main__':
    unittest.main()