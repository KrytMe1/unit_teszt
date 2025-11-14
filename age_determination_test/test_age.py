import unittest
from age import categorize_byAge

class TestAgeCategorization(unittest.TestCase):

    def test_child_age(self):
        self.assertEqual(categorize_byAge(4), "Child")

    def test_teenager_age(self):
        self.assertEqual(categorize_byAge(10), "Teenager")

    def test_adult_age(self):
        self.assertEqual(categorize_byAge(19), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_byAge(65), "Golden Age")

    def test_invalid_age(self):
        self.assertEqual(categorize_byAge(130), "Invalid age: 130")
        self.assertEqual(categorize_byAge(121), "Invalid age: 121")
        
        
    #python -m unittest .\test_age.py -v futtatáshoz