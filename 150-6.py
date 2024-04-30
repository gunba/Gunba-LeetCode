class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        row_index = 0
        step = 1
        
        for char in s:
            rows[row_index] += char
            
            if row_index == 0:
                step = 1
            elif row_index == numRows - 1:
                step = -1
            
            row_index += step
        
        return ''.join(rows)