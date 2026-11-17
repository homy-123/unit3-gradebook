"""Core logic for Grade Book: store grades per student and compute results."""

MIN_GRADE = 0
MAX_GRADE = 100


def validate_grade(grade):
    """Return the grade as a float, or raise ValueError if it is not a number in 0-100."""
    try:
        value = float(grade)
    except (TypeError, ValueError):
        raise ValueError(f"Grade must be a number, got {grade!r}")
    if not MIN_GRADE <= value <= MAX_GRADE:
        raise ValueError(f"Grade must be between {MIN_GRADE} and {MAX_GRADE}, got {value}")
    return value


def add_grade(book, student, grade):
    """Validate and add a grade for a student (creates the student if new).

    Raises ValueError for an invalid grade; the book is left unchanged.
    """
    value = validate_grade(grade)
    book.setdefault(student, []).append(value)


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
