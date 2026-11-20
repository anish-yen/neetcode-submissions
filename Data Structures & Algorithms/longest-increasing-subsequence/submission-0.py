class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Find the length of the longest increasing subsequence.
      
        Args:
            nums: List of integers
          
        Returns:
            Length of the longest increasing subsequence
        """
        n = len(nums)
        #1111111
        #1
      
        # dp[i] represents the length of the longest increasing subsequence 
        # ending at index i
        dp = [1] * n
      
        # For each position i, check all previous positions j
        for i in range(1, n):
            for j in range(i):
                # If nums[j] < nums[i], we can extend the subsequence ending at j
                if nums[j] < nums[i]:
                    # Update dp[i] to be the maximum of current value or 
                    # the length of subsequence ending at j plus 1
                    dp[i] = max(dp[i], dp[j] + 1)
      
        # Return the maximum length among all subsequences
        return max(dp)
