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



#finding the kth factor

class Solution(object):
    def kthFactor(self, n, k):
        
        
        result = []
        for i in range (1 , n+1):
            if n % i == 0:
                result.append(i)
        if len(result) < k:
            return -1
        
        return result[k-1]


# Self Dividing Numbers

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False


        addition = 1

        for i in range (2, int(num ** 0.5) + 1):

            if num % i == 0:
                addition += i

                if i != num // i:
                    addition += num // i
        
        return addition == num

# Finding Fibonnacci number

class Solution(object):
    def func(self,num):
        if num==0 or num==1 :
            return num
        return self.func(num-1)+ self.func(num-2)

    def fib(self, n):
        answer = self.func(n)
        return answer