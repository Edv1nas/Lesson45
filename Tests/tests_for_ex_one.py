import unittest
from exercise_one import PizzaPoint, customers, pizza_point


class TestExerciseOne(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = PizzaPoint(customers)

    def test_if_not_empty_list(self):
        self.assertNotEqual(self.pizza.eligible_customers(), [])

    # def test_eligible_customers(self):
