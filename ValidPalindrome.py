class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        for c in s:
            if c.isalnum():
                s1 += c.lower()
        return s1 == s1[::-1]
