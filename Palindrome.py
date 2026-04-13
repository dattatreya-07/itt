class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        s=str(x)
        s1=s[::-1]
        if s1==x:
            return True
        else:
            return False
