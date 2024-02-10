class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        # Check if the string contains spaces
        if ' ' in s:
            # Split the string into words and return the length of the last word
            words = s.split()
            return len(words[-1])
        else:
            # If no spaces, return the length of the string
            return len(s)
