
class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        num = 0
        limit = 2**31 - 1

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if num > limit // 10 or (
                num == limit // 10 and digit > 7
            ):
                return limit if sign == 1 else -(2**31)

            num = num * 10 + digit
            i += 1

        return sign * num