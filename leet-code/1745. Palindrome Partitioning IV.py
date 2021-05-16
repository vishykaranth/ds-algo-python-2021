# https://leetcode.com/problems/palindrome-partitioning-iv/

# Let isp(i, j) be true iff s[i..j] is a palindrome.  We can find it with a simple dp.
# Now for each i <= j, we can just check if isp(0, i-1) and isp(i, j) and isp(j+1, n-1).



class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # @cache
        def isp(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and isp(i + 1, j - 1)

        n = len(s)
        for i in range(1, n):
            for j in range(i, n - 1):
                if isp(0, i - 1) and isp(i, j) and isp(j + 1, n - 1):
                    return True
        return False


s = Solution()
print(s.checkPartitioning('abcbdd'))
