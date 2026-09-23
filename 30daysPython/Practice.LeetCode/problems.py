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


# VALID PALINDROME 

class Solution(object):
    def ispalindrome(self, s):

        left = 0
        right = len(s)-1

        while left < right :

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True 


#count the digits that divide the number


class Solution(object):
    def countDigits(self, num):
        
        type num = int
        rtype = int
        original = num
        count = 0
        while num > 0 :
            digit = num % 10
            if  digit != 0 :
                if  original % digit == 0 :
                    count = count + 1
                    
            num = num // 10
        return count 