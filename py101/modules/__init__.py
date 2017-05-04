""""
Modules Adventure

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
    """Adventure test"""

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

        import_statements = [
            node
            for node in ast.walk(body)
            if isinstance(node, ast.Import) and
            len(node.names) > 0 and
            len([name for name in node.names if name.name == 'numbers']) > 0
        ]

        self.assertGreater(
            len(import_statements),
            0,
            "It should be at least one import statement for numbers"
        )

        call_statements = [
            node
            for node in ast.walk(body)
            if isinstance(node, ast.Call) and
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == 'numbers' and
            node.func.attr == 'tangent'
        ]

        self.assertGreater(
            len(call_statements),
            0,
            "It should be at least one call statement for numbers.tangent"
        )

        code = compile(self.candidate_code, self.file_name, 'exec', optimize=0)
        exec(code)

        self.assertEqual(
            2,
            len(self.__mockstdout.getvalue().split('\n')),
            "Should have output one line"
        )

        returned_value = float(self.__mockstdout.getvalue())

        self.assertAlmostEqual(
            returned_value,
            1.5574077246549025,
            4,
            "The output number should be near 1.557")


class Adventure(BaseAdventure):
    """Modules Adventure"""
    title = _('Modules')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
