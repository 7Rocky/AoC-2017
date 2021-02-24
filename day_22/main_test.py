import io
import sys
import unittest

from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        rescued_stdout = io.StringIO()
        sys.stdout = rescued_stdout

        main()

        want = 'Infected nodes (1): 5404\n' + \
               'Infected nodes (2): 2511672\n'

        sys.stdout = sys.__stdout__
        self.assertEqual(want, rescued_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
