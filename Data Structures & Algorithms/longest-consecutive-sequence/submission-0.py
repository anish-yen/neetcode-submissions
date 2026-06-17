class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        start = 0
        count = 1
        currlen =0
        maxlen =0 

        numset = set(nums)
        maxlen = 0
        if not nums:
            return 0

        for num in numset:
            if num-1 not in numset:
                curr=num
                currlen=1
            while curr+1 in numset:
                curr+=1
                currlen+=1
            maxlen = max(maxlen, currlen)

        return maxlen