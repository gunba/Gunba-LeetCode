class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        k = len(ratings)
        kr = range(k)
        candy = [1 for _ in kr]

        for i in kr:
            if i-1 >= 0 and ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        for i in reversed(kr):
            if k > i+1 and ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1

        return sum(candy)



test = Solution()
print(test.candy([1,6,10,8,7,3,2]))
#print(test.candy([1,2,2]))
#print(test.candy([1,2,87,87,87,2,1]))
#print(test.candy([1,3,4,5,2]))