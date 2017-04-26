""""
Introduction Adventure

Author: igui
"""
import codecs
import io
import sys
import unittest
from unittest.mock import create_autospec
from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

class TestOutput(unittest.TestCase):
    "Introduction Adventure test"
    def __init__(self, sourcefile):
        "Inits the test"
        super(TestOutput, self).__init__()
        self.sourcefile = sourcefile

    def setUp(self):
        self.__old_stdout = sys.stdout
        sys.stdout = self.__mockstdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.__old_stdout
        self.__mockstdout.close()

    @staticmethod
    def mock_print(stringy):
        "Mock function"
        pass

    def runTest(self):
        "Makes a simple test of the output"
        raw_program = codecs.open(self.sourcefile).read()
        code = compile(raw_program, self.sourcefile, 'exec', optimize=0)
        exec(code)
        self.assertEqual(
            self.__mockstdout.getvalue().lower().strip(),
            'hello world',
            "Should have printed 'Hello World'"
        )

class Adventure(BaseAdventure):
    "Introduction Adventure"
    title = _('Introduction')

    @classmethod
    def test(cls, sourcefile):
        "Test against the provided file"
        suite = unittest.TestSuite()
        suite.addTest(TestOutput(sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
