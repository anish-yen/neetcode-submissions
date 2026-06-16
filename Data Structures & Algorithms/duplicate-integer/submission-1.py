from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict_nums = dict(enumerate(nums))
        value_counts = Counter(dict_nums.values())
        print(value_counts)
        