class Solution
    # Using binary search
    # Time O(log n) | Space O(1)
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            k = (left+right)//2
            curr = k*(k+1)//2
            
            if curr==n:
                return k
            if curr < n:
                left = k+1
            else:
                right = k-1
                
        return left-1 