# Let's answer each query individually.
# Looking at the slowest and fastest possible time we could eat candy,
# we can figure out whether it is possible (as any rate between slowest and fastest is possible.)


class Solution:
    def canEat(self, A, queries):
        from itertools import accumulate
        P = list(accumulate(A, initial=0))

        def query(typ, day, cap):
            # P[typ + 1] : all candies including favorite
            # P[typ] + 1 : all candies before the favorite, plus 1 of the favorite

            # note1: eating slow, must have at least 1 fave candy left
            # note2: eating fast, must be able to eat 1 of the fave candy in time
            return (
                    (day + 1) <= P[typ + 1] and  # note1
                    (day + 1) * cap >= P[typ] + 1  # note2
            )

        return [query(*q) for q in queries]


s = Solution()
print(s.canEat([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))
