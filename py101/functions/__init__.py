""""
Functions Adventure

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

    expected_output = '\n'.join([
        str(element) for element in range(2, 101, 2)
        ]) + '\n'

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

        defined_functions = set([
            node.name
            for node in ast.walk(body)
            if isinstance(node, ast.FunctionDef)
        ])

        called_functions = set([
            node.func.id
            for node in ast.walk(body)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        ])

        self.assertGreater(
            len(defined_functions & called_functions),
            0,
            "Should call at least one defined function"
        )

        code = compile(self.candidate_code, self.file_name, 'exec', optimize=0)
        exec(code)

        self.assertMultiLineEqual(self.expected_output,
                                  self.__mockstdout.getvalue(),
                                  "Output should match expected output"
                                  )


class Adventure(BaseAdventure):
    """Functions Adventure"""

    title = _('Functions')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
