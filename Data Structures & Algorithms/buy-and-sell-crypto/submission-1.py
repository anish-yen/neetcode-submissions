class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        curmax = 0

        while right<len(prices):
            profit = prices[right] - prices[left]
            if not prices[right] > prices[left]:
                left = right

            else:
                if profit>curmax:
                    curmax=profit
            right+=1
        return curmax
