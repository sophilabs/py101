import py101
import py101.boilerplate
import py101.introduction
import py101.lists
import py101.variables
import py101.operators
import py101.formatting
import py101.strings
import py101.conditions
import py101.loops
import py101.functions
import py101.classes
import py101.dictionaries
import unittest
from story.commands import PrintCommand, SolutionCommand, SelectCommand
from io import StringIO
import sys
from story.translation import activate
from os import path


class AdventureData(object):
    """Stores test data"""
    def __init__(self, test_module, good_solution, en_sentinel, es_sentinel):
        self.module = test_module
        self.good_solution = good_solution
        self.en_sentinel = en_sentinel
        self.es_sentinel = es_sentinel


class SelectCommandArgsMock(object):
    """Mock for the Story select command argument"""
    def __init__(self, name):
        self.name = name


class MockStdout(StringIO):
    def __enter__(self):
        self.__old_stdout = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.__old_stdout
        self.close()


def get_solution_path(solution_name):
    return path.join(path.dirname(__file__), 'solutions', solution_name)


adventures = [
    AdventureData(
        py101.introduction,
        get_solution_path('introduction.py'),
        'introduction',
        'introducción'
    ),
    AdventureData(
        py101.variables,
        get_solution_path('variables.py'),
        'variables',
        'variables'
    ),
    AdventureData(
        py101.lists,
        get_solution_path('lists.py'),
        'lists',
        'listas'
    ),
    AdventureData(
        py101.operators,
        get_solution_path('operators.py'),
        'operators',
        'operadores'
    ),
    AdventureData(
        py101.formatting,
        get_solution_path('formatting.py'),
        'formatting',
        'formateo'
    ),
    AdventureData(
        py101.strings,
        get_solution_path('strings.py'),
        'strings',
        'cadenas'
    ),
    AdventureData(
        py101.conditions,
        get_solution_path('conditions.py'),
        'conditions',
        'condiciones'
    ),
    AdventureData(
        py101.loops,
        get_solution_path('loops.py'),
        'loops',
        'bucles'
    ),
    AdventureData(
        py101.functions,
        get_solution_path('functions.py'),
        'functions',
        'funciones'
    ),
    AdventureData(
        py101.classes,
        get_solution_path('classes.py'),
        'classes',
        'clases'
    ),
    AdventureData(
        py101.dictionaries,
        get_solution_path('dictionaries.py'),
        'dictionaries',
        'diccionarios'
    )
]


def get_adventure_shortname(adventure):
    return adventure.module.__name__.split('.')[-1]


class TestStory(unittest.TestCase):
    def test_name(self):
        self.assertEqual(py101.Story().name, 'py101', "name should be py101")

    def test_required_commands(self):
        story = py101.Story()
        all_command_classes = [command.__class__ for command in story.commands]

        self.assertIn(PrintCommand,
                      all_command_classes,
                      "Story should have a print command")
        self.assertIn(SolutionCommand,
                      all_command_classes,
                      "Story should have a solution command")
        self.assertIn(SelectCommand,
                      all_command_classes,
                      "Story should have a select command")


class TestAdventures(unittest.TestCase):

    @staticmethod
    def get_command(story, command_class):
        return [
            command
            for command in story.commands
            if isinstance(command, command_class)
        ][0]

    def setUp(self):
        self.story = py101.Story()
        self.print_command = self.get_command(self.story, PrintCommand)
        self.solution_command = self.get_command(self.story, SolutionCommand)
        self.select_command = self.get_command(self.story, SelectCommand)

    def test_is_included(self):
        story_adventure_classes = [
            adventure.__class__
            for adventure in py101.Story().adventures
        ]
        for adventure in adventures:
            with self.subTest(adventure=get_adventure_shortname(adventure)):
                self.assertIn(adventure.module.Adventure,
                              story_adventure_classes,
                              "Adventure should be in the story adventures")

    def test_format_doesnt_break(self):
        for adventure in adventures:
            with self.subTest(adventure=get_adventure_shortname(adventure)):
                args = SelectCommandArgsMock(
                    get_adventure_shortname(adventure)
                )

                self.select_command.handle(args)

                with MockStdout() as mocked_stdout:
                    activate('en')
                    self.print_command.handle({})
                    self.assertIn(
                        adventure.en_sentinel,
                        mocked_stdout.getvalue().lower(),
                        "The output should have the correct sentinel")

                    self.solution_command.handle({})

                with MockStdout() as mocked_stdout:
                    activate('es')
                    self.print_command.handle({})
                    self.solution_command.handle({})
                    self.assertIn(
                        adventure.es_sentinel,
                        mocked_stdout.getvalue().lower(),
                        "The output should have the correct sentinel")

    def test_solution(self):
        for adventure in adventures:
            with self.subTest(adventure=get_adventure_shortname(adventure)):
                with open(adventure.good_solution) as code_file:
                    test = adventure.module.TestOutput(
                        code_file.read(),
                        adventure.good_solution
                    )
                    test.setUp()
                    try:
                        test.runTest()
                    finally:
                        test.tearDown()
