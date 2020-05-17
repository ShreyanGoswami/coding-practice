# Given a roman numeral, convert it to an integer. 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Input is guaranteed to be within the range from 1 to 3999.
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

class Solution:
    converter_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def romanToInt(self, s: str) -> int:
        # if the value of the next string is greater than the current one 
        # subtract that value from the next string and don't add anything in the current sum
        sum = 0
        num_to_b_subtracted = 0
        for i in range(0, len(s)):
            curr_value = self.converter_map[s[i]]
            if i != len(s) - 1:
                next_value = self.converter_map[s[i + 1]]
                if curr_value < next_value:
                    num_to_b_subtracted = curr_value
                    continue
            sum = sum + curr_value - num_to_b_subtracted
            num_to_b_subtracted = 0
        return sum

sol = Solution()
print(sol.romanToInt('IX'))
print(sol.romanToInt('MCMXCIV'))
        
