class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}

        def dfs(i):
            if i>=len(nums):
                return 0
            if i in seen:
                return seen[i]
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i+1)
            seen[i] = max(rob,skip)
            return seen[i]
        return dfs(0)
            

2,9,8,3,6




#subproblem- find max of subarray