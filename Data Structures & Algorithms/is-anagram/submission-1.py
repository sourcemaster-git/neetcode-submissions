class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(list(s)) == sorted(list(t)):
            return True
        return False