class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 
        maxi = 0
        while r < len(prices):
            curr_max = 0
            if prices[l] > prices[r] :
                l = r
                r+=1 
            elif prices[r] > prices[l] :
                curr_max = prices[r] - prices[l]
                r += 1
                if maxi < curr_max :
                    maxi = curr_max 
            else: 
                r+=1
        return maxi