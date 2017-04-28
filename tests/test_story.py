from py101 import Story
from py101 import variables
from py101 import lists
import unittest


class TestStory(unittest.TestCase):
    def test_name(self):
        self.assertEqual(Story().name, 'py101', "name should be py101")


class TestAdventureVariables(unittest.TestCase):
    good_solution = """
myinteger = 4
mystring = 'Python String Here'
print(myinteger)
print(mystring)
    """

    def test_solution(self):
        test = variables.TestOutput(self.good_solution)
        test.setUp()
        try:
            test.runTest()
        finally:
            test.tearDown()


class TestAdventureLists(unittest.TestCase):
    good_solution = """
languages = ["ADA", "Pascal", "Fortran", "Smalltalk"]
print(languages)
    """

    def test_solution(self):
        test = lists.TestOutput(self.good_solution)
        test.setUp()
        try:
            test.runTest()
        finally:
            test.tearDown()

