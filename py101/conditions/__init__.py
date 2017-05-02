""""
Conditions Adventure

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

    inmutable_code_str = """
if first_number > 15:
    print("1")
    if second_number > 15:
        print("2")

if first_number < second_number:
    print("3")
else:
    print("Error")
"""

    def __init__(self, candidate_code, file_name='<inline>'):
        """Init the test"""
        super(TestOutput, self).__init__()
        self.candidate_code = candidate_code
        self.file_name = file_name
        self.inmutable_code = ast.parse(self.inmutable_code_str, file_name, 'exec')

    def setUp(self):
        self.__old_stdout = sys.stdout
        sys.stdout = self.__mockstdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.__old_stdout
        self.__mockstdout.close()

    def runTest(self):
        """Makes a simple test of the output"""

        body = ast.parse(self.candidate_code, self.file_name, 'exec')

        # Looks if the code is the same as the provided code.
        body_dump = ast.dump(body)
        for node in self.inmutable_code.body:
            self.assertTrue(body_dump.find(ast.dump(node)) >= 0, "Provided code should not be modified")

        code = compile(self.candidate_code, self.file_name, 'exec')
        exec(code)
        self.assertMultiLineEqual('1\n2\n3\n',
                                  self.__mockstdout.getvalue(),
                                  'Output is not correct')



class Adventure(BaseAdventure):
    """Conditions Adventure"""
    title = _('Conditions')

    @classmethod
    def test(cls, sourcefile):
        """Test against the provided file"""
        suite = unittest.TestSuite()
        raw_program = codecs.open(sourcefile).read()
        suite.addTest(TestOutput(raw_program, sourcefile))
        result = unittest.TextTestRunner().run(suite)
        if not result.wasSuccessful():
            raise AdventureVerificationError()
