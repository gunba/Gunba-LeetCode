class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # If there's only one string, return it
        if len(strs) == 1:
            return strs[0]

        # Start with the common prefix between the first two strings
        common_prefix = ""
        for a, b in zip(strs[0], strs[1]):
            if a == b:
                common_prefix += a
            else:
                break

        # If no common prefix between the first two strings, return ""
        if not common_prefix:
            return ""

        # Check the common prefix with each subsequent string
        for string in strs[2:]:
            temp_prefix = ""
            for a, b in zip(common_prefix, string):
                if a == b:
                    temp_prefix += a
                else:
                    break
            common_prefix = temp_prefix

        return common_prefix