from unittest import TestCase
import classroom_manager


class Test_Student(TestCase):
    def test_prop_construct(self):
        id = 1234
        first_name = "Hannah"
        last_name = "Pittman"
        assignments = []

        student = classroom_manager.Student(self, id, first_name, last_name)

        self.assertEqual(1234, student.id)
        self.assertEqual(first_name, student.first_name)
        self.assertEqual(last_name, student.last_name)
        self.assertEqual(assignments, student.assignments)

    def test_full_name(self):
        student = classroom_manager.Student(1234, "Hannah", "Pittman")
        self.assertEqual(student.get_full_name(), "Hannah Pittman")

    def test_get_assignnments(self):
        self.assertEqual()

    def test_get_assignnment(self):
        self.assertEqual()

    def test_get_average(self):
        self.assertEqual()

    def test_submit_assignnment(self):
        self.assertEqual()

    def test_remove_assignnment(self):
        self.assertEqual()
