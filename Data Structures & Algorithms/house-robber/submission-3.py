class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prefix = [0] * (len(nums) +2)

        for i in range(len(nums)):
            prefix[i+2] = max(prefix[i+1] , nums[i] + prefix[i])
        
        return prefix[-1]

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for num in nums:
            current = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current

        return prev1
        reduce space
"""