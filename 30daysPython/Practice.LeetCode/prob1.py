# PALINDROME 

class Solution(object):
    def isPalindrome(self, x):

        num = x
        result = 0

        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10

        return x == result
        
# REVERSE A STRING 

class Solution(object):
    def reverseString(self, s):
        
        left = 0
        right = len(s)-1

        while left < right :

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1    