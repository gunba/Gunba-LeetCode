class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        holding_price = None

        k = len(prices)

        for i in range(k):
            # Sell: If there is a next elem and it is cheaper than current elem

            # Next elem is more expensive than current elem
            if k > i+1 and prices[i+1] > prices[i]:
                # If we are not holding
                if holding_price is None:
                    holding_price = prices[i]
            # Else, if we are holding we should sell
            elif holding_price is not None and prices[i] > holding_price:
                max_profit += prices[i] - holding_price
                holding_price = None         
        
        return max_profit
    
test = Solution

print(test.maxProfit(test, [2,1,2,1,0,1,2]))