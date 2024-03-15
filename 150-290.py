class Solution(object):
    def wordPattern(self, pattern, s):
        word_list = s.split()  # Split the string into words
        if len(pattern) != len(word_list):
            return False  # Early return if lengths differ, ensuring one-to-one correspondence

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, word_list):
            if (char in char_to_word and char_to_word[char] != word) or \
            (word in word_to_char and word_to_char[word] != char):
                return False  # Mismatch found

            char_to_word[char] = word
            word_to_char[word] = char

        return True  # All checks passed
        