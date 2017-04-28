import py101
import py101.boilerplate
import py101.introduction
import py101.lists
import py101.variables
import unittest


class TestStory(unittest.TestCase):
    def test_name(self):
        self.assertEqual(py101.Story().name, 'py101', "name should be py101")


class AdventureData(object):
    def __init__(self, test_module, good_solution):
        self.module = test_module
        self.good_solution = good_solution


class TestAdventures(unittest.TestCase):
    adventures = [
        AdventureData(
            py101.boilerplate,
            ""
        ),
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
        )
    ]

    def test_solution(self):
        for adventure in self.adventures:
            with self.subTest(adventure=adventure.module.__name__):
                test = adventure.module.TestOutput(adventure.good_solution)
                test.setUp()
                try:
                    test.runTest()
                finally:
                    test.tearDown()
