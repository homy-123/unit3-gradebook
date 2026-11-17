import unittest

from grades import add_grade, average, letter, validate_grade


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


class TestValidation(unittest.TestCase):
    def test_accepts_boundaries_and_numeric_text(self):
        self.assertEqual(validate_grade(0), 0.0)
        self.assertEqual(validate_grade(100), 100.0)
        self.assertEqual(validate_grade("85.5"), 85.5)

    def test_rejects_out_of_range(self):
        for bad in (-1, 100.1, 150):
            with self.assertRaises(ValueError):
                validate_grade(bad)

    def test_rejects_non_numbers(self):
        for bad in ("abc", "", None, "nan"):
            with self.assertRaises(ValueError):
                validate_grade(bad)

    def test_add_grade_rejects_bad_grade_and_keeps_book_clean(self):
        book = {}
        with self.assertRaises(ValueError):
            add_grade(book, "Sara", 101)
        self.assertEqual(book, {})


if __name__ == "__main__":
    unittest.main()
