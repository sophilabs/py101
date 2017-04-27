""""
Introduction Adventure

Author: Ignacio Avas (iavas@sophilabs.com)
"""
import codecs
import io
import sys
import unittest
from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _


class TestOutput(unittest.TestCase):
    "Introduction Adventure test"
    def __init__(self, candidate_code, file_name = '<inline>'):
        """Init the test"""
        super(TestOutput, self).__init__()
        self.candidate_code = candidate_code
        self.file_name = file_name

    def setUp(self):
        self.__old_stdout = sys.stdout
        sys.stdout = self.__mockstdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.__old_stdout
        self.__mockstdout.close()

    def runTest(self):
        """Makes a simple test of the output"""

        code = compile(self.candidate_code, self.file_name, 'exec', optimize=0)

        self.assertIn('myinteger', code.co_names, 'Should have defined myinteger variable')
        self.assertIn('mystring', code.co_names, 'Should have defined mystring variable')
        exec(code)
        lines = [line.lower().strip() for line in self.__mockstdout.getvalue().split('\n')]
        self.assertEqual(3, len(lines), 'Should have printed two lines')
        self.assertEqual(['4', 'python string here',  ''], lines, 'Should have same output')


def mock_print(_):
    "Mock function"
    pass


class Adventure(BaseAdventure):
    """Introduction Adventure"""
    title = _('Variables')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
