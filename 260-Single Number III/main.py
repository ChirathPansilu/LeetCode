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

class Solution:
    # Time O(n) | Space O(n)
    # Using hash map - Have O(1) lookup and remove
    def singleNumber(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in nums:
            if not mp.get(i):
                mp[i] = True
            else:
                mp.pop(i)
        return mp.keys()