""""
Operators Adventure

Author: Ignacio Avas (iavas@sophilabs.com)
"""
import codecs
import io
import sys
import unittest
from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _
import ast


class TestOutput(unittest.TestCase):
    """Variables Adventure test"""
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
        code = compile(self.candidate_code, self.file_name, 'exec')

        mult_instructions = [node for node in ast.walk(body) if isinstance(node, ast.Mult)]
        self.assertTrue(len(mult_instructions) > 0, "It should have at least one duplication")

        exec(code)
        self.assertMultiLineEqual('ka'*10+'\n', self.__mockstdout.getvalue(), "Should have printed ka 10 times")


class Adventure(BaseAdventure):
    title = _('Operators')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
