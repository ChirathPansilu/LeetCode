# Time O(n) | Space O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        requiredTotal = n*(n+1)//2
        
        total = 0
        for i in nums:  total += i
        
        if total != requiredTotal:
            return requiredTotal - total
        else:
            return 0