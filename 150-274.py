class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        temp = sorted(citations, reverse=True)

        for i, c in enumerate(temp):
            if not c >= i+1:
                return i
            
        return len(citations)
            
