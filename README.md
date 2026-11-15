# Grade Book - validated input

A small command-line program that stores grades per student and shows each
student's average and letter grade (A-F).

## What it does

- Add a grade for a student
- Show a student's average and letter grade
- Runs in the terminal, no external libraries needed

## How to run

Requires Python 3.9 or newer.

```bash
python main.py
```

Run the tests:

```bash
python -m unittest -v
```

## Project files

| File | Purpose |
|------|---------|
| `grades.py` | Core logic (add grade, average, letter grade) |
| `main.py` | Command-line menu |
| `test_grades.py` | Unit tests |
