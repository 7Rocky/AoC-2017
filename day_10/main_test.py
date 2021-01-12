import io
import sys
import unittest

from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        rescued_stdout = io.StringIO()
        sys.stdout = rescued_stdout

        main()

        want = 'Result (1): 23874\n' + \
               'Knot Hash (2): e1a65bfb5a5ce396025fab5528c25a87\n'

        sys.stdout = sys.__stdout__
        self.assertEqual(want, rescued_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
