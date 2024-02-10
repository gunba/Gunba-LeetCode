class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine, ransomNote = sorted(magazine), sorted(ransomNote)

        if magazine == ransomNote:
            return True

        count = 0
        ransom_len = len(ransomNote)

        for char in magazine:
            if count < ransom_len:
                if char > ransomNote[count]:
                    return False
                if char == ransomNote[count]:
                    count += 1
            if count == ransom_len:
                return True

        return False
