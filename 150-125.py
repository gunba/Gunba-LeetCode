class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char for char in s if char.isalnum()).lower() 
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[-i - 1]:
                return False
        return True