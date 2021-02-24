import io
import sys
import unittest

from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        rescued_stdout = io.StringIO()
        sys.stdout = rescued_stdout

        main()

        want = 'First frequency received (1): 3025\n' + \
               'Value of register "h" (2): 915\n'

        sys.stdout = sys.__stdout__
        self.assertEqual(want, rescued_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
