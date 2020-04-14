import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge")

from challenge import ocr_format

class TestChallenge(unittest.TestCase):

    def test(self):
        self.assertEqual(ocr_format(""), "")


if __name__ == '__main__':
    unittest.main()
