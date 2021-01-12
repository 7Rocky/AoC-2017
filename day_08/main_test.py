import io
import sys
import unittest

from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        rescued_stdout = io.StringIO()
        sys.stdout = rescued_stdout

        main()

        want = 'Max value after the process (1): 6611\n' + \
               'Max value held during the process (2): 6619\n'

        sys.stdout = sys.__stdout__
        self.assertEqual(want, rescued_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
