# Time O(n) | Space O(1)
# Using XOR bit manipulation
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        missing = 0
        for i in s+t:   missing ^= ord(i)
        return chr(missing)