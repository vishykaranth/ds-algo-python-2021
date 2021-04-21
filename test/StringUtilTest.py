import unittest

from strings.StringUtil import StringUtil

class TestStringUtilMethods(unittest.TestCase):

    def test_intToRoman(self):
        s = StringUtil()
        result = s.intToRoman(3)
        self.assertEqual(result, 'III')
        result = s.intToRoman(4)
        self.assertEqual(result, 'IV')
        result = s.intToRoman(11)
        self.assertEqual(result, 'XI')
        result = s.intToRoman(20)
        self.assertEqual(result, 'XX')
        result = s.intToRoman(58)
        self.assertEqual(result, 'LVIII')
        result = s.intToRoman(1994)
        self.assertEqual(result, 'MCMXCIV')



if __name__ == '__main__':
    unittest.main()
