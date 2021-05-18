# https://leetcode.com/contest/weekly-contest-241/
# https://leetcode.com/meladrama/
# https://leetcode.com/LarryNY/
from typing import List


class Solution:
    def subsetXORSum(self, s: List[int]) -> int:
        a = [0]
        for x in s:
            b = [x ^ y for y in a]
            a += b
        return sum(a)

    def minSwaps(self, s: str) -> int:
        a, b, c, d = s[::2].count('1'), s[1::2].count('0'), s[::2].count('0'), s[1::2].count('1')
        ans = min(a if a == b else 2000, c if c == d else 2000)
        return -1 if ans == 2000 else ans

    def rearrangeSticks(self, n: int, k: int) -> int:
        s, m = [0, 1], 1000000007
        for i in range(1, n):
            s.append(s[-1])
            for j in range(i, 0, -1): s[j] = (s[j - 1] + i * s[j]) % m
        return s[k]


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.a, self.nums2, self.d = nums1, nums2, {}
        for x in nums2: self.d[x] = self.d.get(x, 0) + 1

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.nums2[index] += val
        self.d[x] -= 1
        if not self.d[x]: del self.d[x]
        self.d[x + val] = self.d.get(x + val, 0) + 1

    def count(self, tot: int) -> int:
        return sum([self.d.get(tot - x, 0) for x in self.a])
