class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(i):
            if i == n:
                return 1
            if i>n:
                return 0 
            if i in memo:
                return memo[i]
            memo[i] = ways(i + 1) + ways(i + 2)

            return memo[i]

        return ways(0)
'''
def climbStairs(n):
    if n <= 2:
        return n

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
'''