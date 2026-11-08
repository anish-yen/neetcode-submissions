from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]


        #create buckets
        #count freq
        #put nums into correct bucket
        
        for num, count in counts.items():
            buckets[count].append(num)
        
       # print(buckets)
        # scan backwards bucket index = frequency and value = the 
        #want most frequent so scan backwards
        res = []
        for i in range(len(nums), 0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) ==k:
                    return res


