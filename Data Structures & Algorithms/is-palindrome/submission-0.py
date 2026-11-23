class Solution:
    def isPalindrome(self, s: str) -> bool:
        sa="".join(c.lower() for c in s if c.isalnum())
        
        return sa==sa[::-1]
        