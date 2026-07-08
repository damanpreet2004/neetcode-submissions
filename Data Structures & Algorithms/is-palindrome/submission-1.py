class Solution:
    def isPalindrome(self, s: str) -> bool:
        Ls = "".join(char.lower() for char in s if char.isalnum())
        reversed_s = Ls[::-1]
        return Ls == reversed_s