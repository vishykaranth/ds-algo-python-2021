import unittest

from strings.StringAlgorithms import StringAlgorithms


class TestStringAlgorithmsMethods(unittest.TestCase):

    def test_findNonRepeatingChar(self):
        stringAlgorithms = StringAlgorithms()
        str = "ABCDBAGHC"
        n = len(str)
        char = stringAlgorithms.findNonRepeatingChar(str, n)
        print(char)
        assert char == 'D'
