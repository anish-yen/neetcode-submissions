class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1) #always one more than length
        dp[0] = 0

        for coin in coins: # loop thru each coin and update value
            for i in range(coin, amount + 1): #range - based on each coin
                dp[i] = min(dp[i], dp[i - coin] + 1) #min use the dp table prefix or whatever pattern

        if dp[amount] != float('inf'):
            return dp[amount] 
        else:
            return -1