class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # FIX 1: skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                curr_sum = nums[left] + nums[right]

                # FIX 2: use if / elif / else (not while/while/else)
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # FIX 3: append triplet (not dict assignment)
                    result.append([nums[i], nums[left], nums[right]])

                    # FIX 4: move pointers after finding match
                    left += 1
                    right -= 1

                    # FIX 5: skip duplicate left/right values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
