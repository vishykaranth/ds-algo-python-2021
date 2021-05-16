# https://leetcode.com/contest/biweekly-contest-51
import string
from typing import List


def shift(val, i):
    alpha = string.ascii_lowercase
    index = alpha.index(val) + i
    return alpha[index]


class Solution:

    def replaceDigits(self, s: str) -> str:
        l = list(s)
        for i in range(1, len(l), 2):
            l[i] = chr(ord(l[i-1]) + int(l[i]))
        return ''.join(l)

    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        Q = len(queries)
        ans = [-1] * Q

        events = []
        for i, s in rooms:
            events.append((-s, 0, i, -1))

        for index, (p, m) in enumerate(queries):
            events.append((-m, 1, p, index))

        events.sort()
        sl = SortedList()
        for s, t, c, d in events:
            if t == 0:
                sl.add(c)
            else:
                index = sl.bisect_left(c)
                cur = -1
                if 0 <= index < len(sl):
                    cur = sl[index]

                index -= 1
                if 0 <= index < len(sl):
                    if abs(sl[index] - c) <= abs(cur - c):
                        cur = sl[index]
                ans[d] = cur
        return ans

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)

        arr[0] = 1
        for index in range(1, N):
            arr[index] = min(arr[index - 1] + 1, arr[index])
        return arr[-1]


    def replaceDigits2(self, s: str) -> str:
        print(string.ascii_letters)

        index = 0

        result = ""
        l = list(s)
        while index < len(l):
            val = l[index]
            result += val
            index += 1

            if index < len(s):
                i = int(l[index])
                result += shift(val, i)
                index += 1

        print(result)


s = Solution()
s.replaceDigits('a1c1e1')
s.replaceDigits('a1b2c3d4e')
print(s.replaceDigits('a1b2c3z4e'))

from sortedcontainers import SortedList


class SeatManager:

    def __init__(self, n: int):
        self.sl = SortedList()
        for x in range(1, n + 1):
            self.sl.add(x)

    def reserve(self) -> int:
        x = self.sl[0]
        self.sl.remove(x)
        return x

    def unreserve(self, seatNumber: int) -> None:
        self.sl.add(seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

