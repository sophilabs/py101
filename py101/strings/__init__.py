""""
Strings Adventure

Author: Ignacio Avas (iavas@sophilabs.com)
"""
import codecs
import io
import sys
import unittest
from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _


class TestOutput(unittest.TestCase):
    """Adventure test"""

    expected_output = [
        "17",
        "THIS IS MY STRING",
        "this is my string",
        "['This', 'Is', 'MY', 'string']",
        ""
    ]

    def __init__(self, candidate_code, file_name='<inline>'):
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

        self.assertIn('len',
                      code.co_names,
                      'Should have called the len function')
        self.assertIn('split',
                      code.co_names,
                      'Should have called the split function')
        self.assertIn('upper',
                      code.co_names,
                      'Should have called the upper function')
        self.assertIn('lower',
                      code.co_names,
                      'Should have called the lower function')
        exec(code)
        lines = self.__mockstdout.getvalue().split('\n')
        self.assertEqual(self.expected_output,
                         lines,
                         'Should have same output'
                         )


class Adventure(BaseAdventure):
    """String Adventure"""

    title = _('String Operations')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
