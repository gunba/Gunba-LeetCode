class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Convert Roman numeral to list of integers
        integer_list = [roman_dict[char] for char in s]

        k = len(integer_list)

        total = 0
        for i in range(len(k)):
            # If the current value is less than the next value, subtract it from the total
            if i < k - 1 and integer_list[i] < integer_list[i + 1]:
                total -= integer_list[i]
            else:
                # Otherwise, add it to the total
                total += integer_list[i]

        return total