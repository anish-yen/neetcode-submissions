class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:  # ← key fix: compare mid to hi, not to a "min"
                lo = mid + 1
            else:
                hi = mid              # ← variable name was "high", must be "hi"

        return nums[lo]