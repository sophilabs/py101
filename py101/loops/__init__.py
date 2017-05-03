""""
Loopsgit gi Adventure

Author: Ignacio Avas (iavas@sophilabs.com)
"""
import codecs
import io
import sys
import unittest
import ast
from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _


class TestOutput(unittest.TestCase):
    """Adventure test"""

    correct_output = '\n'.join(
        [str(number) for number in range(1, 100, 2)] +
        ['']
    )

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

        body = ast.parse(self.candidate_code, self.file_name, 'exec')
        code = compile(self.candidate_code, self.file_name, 'exec', optimize=0)
        exec(code)

        if_statements = [
            node
            for node in ast.walk(body)
            if isinstance(node, ast.If)
        ]
        self.assertGreater(len(if_statements),
                           0,
                           "Should have at least on if statement")

        self.assertMultiLineEqual(self.correct_output,
                                  self.__mockstdout.getvalue(),
                                  "Output should be correct")


class Adventure(BaseAdventure):
    """Loops Adventure"""
    title = _('Looping')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
