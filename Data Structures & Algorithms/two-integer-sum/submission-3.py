class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #mydict = dict(enumerate(nums))
        #print(mydict)
        mydict = {}
        for i in range(len(nums)):
            
            difference = target - nums[i]
            if difference in mydict:
                return [ mydict[difference],i]
            else:
                mydict[nums[i]] = i