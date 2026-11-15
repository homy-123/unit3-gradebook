import unittest

from grades import add_grade, average, letter


class TestGrades(unittest.TestCase):
    def test_average_of_two_grades(self):
        book = {}
        add_grade(book, "Ali", 80)
        add_grade(book, "Ali", 100)
        self.assertEqual(average(book, "Ali"), 90)

    def test_average_without_grades_is_zero(self):
        self.assertEqual(average({}, "Nobody"), 0.0)

    def test_letter_boundaries(self):
        self.assertEqual(letter(90), "A")
        self.assertEqual(letter(89.9), "B")
        self.assertEqual(letter(59), "F")


if __name__ == "__main__":
    unittest.main()
