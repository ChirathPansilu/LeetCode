class Solution:
    # Time O(1) | Space O(1)
    def arrangeCoins(self, n: int) -> int:
        return int(((1+8*n)**0.5 - 1)/2)