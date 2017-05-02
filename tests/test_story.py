import py101
import py101.boilerplate
import py101.introduction
import py101.lists
import py101.variables
import py101.operators
import py101.formatting
import py101.strings
import unittest


class AdventureData(object):
    def __init__(self, test_module, good_solution):
        self.module = test_module
        self.good_solution = good_solution

adventures = [
    AdventureData(
        py101.introduction,
        """print('Hello World')"""
    ),
    AdventureData(
        py101.variables,
        """myinteger = 4; mystring = 'Python String Here'; print(myinteger); print(mystring)"""
    ),
    AdventureData(
        py101.lists,
        """languages = ["ADA", "Pascal", "Fortran", "Smalltalk"]; print(languages)"""
    ),
    AdventureData(
        py101.operators,
        """print('ka'*10)"""
    ),
    AdventureData(
        py101.formatting,
        """s = 'Talk is {}. Show me the {}.'.format('cheap', 'code'); print(s)"""
    ),
    AdventureData(
        py101.strings,
        """mystring = 'This Is MY string'
print(len(mystring))
print(mystring.upper())
print(mystring.lower())
print(mystring.split(' '))
"""
    )
]


class TestStory(unittest.TestCase):
    def test_name(self):
        self.assertEqual(py101.Story().name, 'py101', "name should be py101")

    def test_content(self):
        story_adventure_classes = [adventure.__class__ for adventure in py101.Story().adventures]

        for adventure in adventures:
            self.assertIn(adventure.module.Adventure, story_adventure_classes)


class TestAdventures(unittest.TestCase):
    def test_solution(self):
        for adventure in adventures:
            with self.subTest(adventure=adventure.module.__name__):
                test = adventure.module.TestOutput(adventure.good_solution)
                test.setUp()
                try:
                    test.runTest()
                finally:
                    test.tearDown()
