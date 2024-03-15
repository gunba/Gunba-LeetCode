class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in "([{":  
                stack.append(char)
            elif not stack or bracket_map[char] != stack.pop(): 
                return False

        return len(stack) == 0
