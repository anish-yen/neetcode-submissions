from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set(nums)
        
        if not nums:
            return 0

        best =0
        
        for num in nums:
            currlen = 0
            curr=num
            while curr in counts:
                currlen+=1
                curr+=1
            best = max(currlen, best)
        return best



        