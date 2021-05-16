# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/contest/weekly-contest-237/problems/check-if-the-sentence-is-pangram/
import string


class Weekly_Contest_237:
    def checkIfPangram(self, sentence: str) -> bool:
        pass

    def ispangram(self, sentence, alphabet=string.ascii_lowercase):
        return set(alphabet) <= set(sentence.lower())


