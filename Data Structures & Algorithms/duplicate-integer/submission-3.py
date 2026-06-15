from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        value_counts = Counter(nums)
        #print(value_counts)
        count = 0
        for value in value_counts.values():
            #print(value)
            if value >= 2:
                #print(value)
                return True
        
        return False
        