# Time O(n) | Space O(1)
# Using the XOR bit manipulations

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums: result ^= i
        return result