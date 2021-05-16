import unittest

from leet_code_contests.weekly_contest_237 import Weekly_Contest_237


class Test_Weekly_Contest_237(unittest.TestCase):

    def test_check_if_pangram(self):
        weekly_Contest = Weekly_Contest_237()
        pangram = weekly_Contest.ispangram('thequickbrownfoxjumpsoverthelazydog')
        print(pangram)
        # assert pangram is True
