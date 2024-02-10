class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        delta = 0
        delta_min = float('inf')

        prices = [prices[i] for i in range(len(prices) - 1) if prices[i] != prices[i + 1]] + [prices[-1]]

        def prune(delta, delta_min, prices):
            k = len(prices)
            for i in range(k-1):
                if delta_min > prices[i]:
                    temp_max = max(prices[i+1:k])
                    temp_delta = temp_max - prices[i]
                    if temp_delta > delta:
                        return temp_delta, prices[i], [x for x in prices[i:] if prices[i] > x or x >= temp_delta]
            return True
        
        while (True):
            temp = prune(delta, delta_min, prices)
            if isinstance(temp, tuple):
                delta, delta_min, prices = temp
            else:
                return delta
               