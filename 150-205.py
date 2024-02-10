class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        mapped_values = set()

        for char_s, char_t in zip(s, t):
            if char_s in char_map:
                if char_map[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_values:
                    return False
                char_map[char_s] = char_t
                mapped_values.add(char_t)

        return True