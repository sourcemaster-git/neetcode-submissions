class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(left + 1, right, s) or self.checkPalindrome(left, right - 1, s)
            left += 1
            right -= 1
        return True

    def checkPalindrome(self, left: int, right: int, s: str) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True