class Solution:
    # Time O(n) | Space O(1)
    # Using bit manipulation
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for i in nums:
            total ^= i
            
        rightMostBit = total & (-total)
        
        n1 = n2 = 0
        
        for i in nums:
            if i & rightMostBit:
                n1 ^= i
            else:
                n2 ^= i
                
        return [n1, n2]