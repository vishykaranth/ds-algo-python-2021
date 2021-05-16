from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        startYear = 1950
        yearIndex = [0] * 100
        for start, end in logs:
            for c in range(start, end):
                yearIndex[c - startYear] += 1

        m = max(yearIndex)
        for index in range(len(yearIndex)):
            if m == yearIndex[index]:
                return index + startYear

        return -1


s = Solution()

print(s.maximumPopulation([[1993, 1999], [2000, 2010]]))
print(s.maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]))
