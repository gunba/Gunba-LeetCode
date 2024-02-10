class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        k = len(gas)
        start = 0

        net = [a - b for a, b in zip(gas, cost)]

        sum_gas = 0
        sum_net = sum(net)

        print(sum_net)

        if sum_net >= 0:
            for i in range(k):
                # add net gas change for stop
                sum_gas += net[i]

                # if we ran out of gas (this start doesnt work)
                if sum_gas < 0:
                    sum_gas = 0
                    start = i+1

            return start
        else:
            return -1
           
test = Solution()

print(test.canCompleteCircuit([2,3,4], [3,4,3]))
