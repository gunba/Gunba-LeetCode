class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if t == s:
            return True

        subseq_len = len(s)
        count = 0

        for char in t:
            if count < subseq_len and char == s[count]:
                count += 1
            if count == subseq_len:
                return True

        return False