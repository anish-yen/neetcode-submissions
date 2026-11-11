class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        res =[]
        nums.sort()
        #res
        # sort nums
        # two numbers in front for l and r, loop through
        # check if duplicate k
        # while l<r check all triplets but not duplicate nums
        # need to recalc sum evertytime
        #update pounters in all 3 cases

        
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            target= -nums[i]
            

            if i>0 and nums[i] == nums[i-1]:
                continue

            while l<r:
                # need here
                summed = nums[l] + nums[r]
                if summed == target:
                    res.append([nums[l],nums[i],nums[r]])
                    l+=1
                    r-=1

                    #check dupe triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif summed> target:
                    r-=1
                else:
                    l+=1
        return res

                


            
        