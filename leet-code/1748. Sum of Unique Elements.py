# https://leetcode.com/problems/sum-of-unique-elements/


from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # ##collections.Counter##
        count = Counter(nums)
        return sum(x for x in count if count[x] == 1)

    def sumOfUnique2(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if nums.count(num) == 1:
                unique.append(num)
        return sum(unique)

    def sumOfUnique3(self, nums: List[int]) -> int:
        unique = []
        # ##List_Comprehension##
        [unique.append(num) for num in nums if nums.count(num) == 1]
        return sum(unique)


s = Solution()
print(s.sumOfUnique3([1, 2, 3, 2]))
print(s.sumOfUnique3([1, 1, 1, 1, 1]))
print(s.sumOfUnique3([1, 2, 3, 4, 5]))
