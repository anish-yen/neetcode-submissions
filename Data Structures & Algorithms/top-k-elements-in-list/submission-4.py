from collections import Counter

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_to_freq = Counter(nums)

        #1:1, 2:2, 3:4
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        for num, freq in num_to_freq.items():
            buckets[freq].append(num)
        
        res = []

        for i in range(len(buckets)-1, 0,-1):

            for num in buckets[i]:
                res.append(num)
                if len(res) ==k:
                    return res



        #iterate backwards
        