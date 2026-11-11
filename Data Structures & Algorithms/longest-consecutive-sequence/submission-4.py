class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        vals = set(nums)

        best = 0
        for num in nums:
            currlen = 1
            if num-1 in vals:
                continue
            while num+1 in vals:
                currlen+=1
                num +=1
            best= max(currlen, best)
        return best

        #set to see all nums
        # keep track start of sequenec if num-1 not in set
        # compare best and currlen to find and return best if its consecturive

