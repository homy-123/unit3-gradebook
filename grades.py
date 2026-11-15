"""Core logic for Grade Book: store grades per student and compute results."""


def add_grade(book, student, grade):
    """Add a grade for a student (creates the student if new)."""
    book.setdefault(student, []).append(grade)


def average(book, student):
    """Return the student's average, or 0.0 if there are no grades."""
    grades = book.get(student, [])
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def letter(avg):
    """Convert a numeric average to a letter grade."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"
