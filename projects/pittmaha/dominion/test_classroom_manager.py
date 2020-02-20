from unittest import TestCase
import classroom_manager


class Test_Student(TestCase):
    def test_prop_construct(self):
        id = 1234
        first_name = "Hannah"
        last_name = "Pittman"
        assignments = []

        # Constructor call
        student = classroom_manager.Student(id, first_name, last_name)

        self.assertEqual(id, student.id)
        self.assertEqual(first_name, student.first_name)
        self.assertEqual(last_name, student.last_name)
        self.assertEqual(assignments, student.assignments)

    def test_full_name(self):
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        self.assertEqual(student.get_full_name(), "Hannah Pittman")

    def test_get_assignments(self):
        assignment1 = classroom_manager.Assignment("Assignment 1", 100)
        assignment2 = classroom_manager.Assignment("Quiz 1", 50)
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        student.assignments = [assignment1, assignment2]
        self.assertEqual(student.get_assignments(), student.assignments)

    def test_get_assignment(self):
        assignment1 = classroom_manager.Assignment("Assignment 1", 100)
        assignment2 = classroom_manager.Assignment("Quiz 1", 50)
        student = classroom_manager.Student(1234, "Hannah", "Pittman")

        self.assertEqual(student.get_assignment("Quiz 1"), None)  # no assignments to look at
        student.assignments = [assignment1, assignment2]
        self.assertEqual(student.get_assignment("Quiz 1"), student.assignments[1])  # assignment at index 1

    def test_get_average(self):
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        assignment1 = classroom_manager.Assignment("Assignment 1", 100)
        assignment1.grade = None
        assignment2 = classroom_manager.Assignment("Quiz 1", 50)
        assignment2.grade = 50
        student.assignments = [assignment1, assignment2]

        self.assertEqual(student.get_average(), 50)
        assignment1.grade = 95
        self.assertEqual(student.get_average(), 72.5)

    def test_submit_assignnment(self):
        assignment1 = classroom_manager.Assignment("Assignment 1", 100)
        assignment2 = classroom_manager.Assignment("Quiz 1", 50)
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        student.assignments = [assignment1, assignment2]

        assignment3 = "Homework 1"
        student.submit_assignment(assignment3)

        self.assertEqual(len(student.assignments), 3)

    def test_remove_assignment(self):
        assignment1 = classroom_manager.Assignment("Assignment 1", 100)
        assignment2 = classroom_manager.Assignment("Quiz 1", 50)
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        student.assignments = [assignment1, assignment2]

        student.remove_assignment("Quiz 1")
        self.assertEqual(len(student.assignments), 1)

class Test_Assignment(TestCase):
    def test_prop_construct(self):
        name = "Quiz 1"
        max_score = 100
        grade = None

        # Constructor call
        assignment = classroom_manager.Assignment(name, max_score)

        self.assertEqual(name, assignment.name)
        self.assertEqual(max_score, assignment.max_score)
        self.assertEqual(grade, assignment.grade)

    def test_assign_grade(self):
        assignment = classroom_manager.Assignment('Quiz 1', 100)
        self.assertEqual(assignment.max_score, 100)

        assignment.assign_grade(100)
        self.assertEqual(assignment.grade, 100)
        assignment.assign_grade(101)
        self.assertEqual(assignment.grade, None)
