class Solution:
    # Using binary search
    # Time O(log n) | Space O(1) 
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            curr = nums[mid]
            
            if curr==target:
                return mid
            if curr < target:
                left = mid + 1
            else:
                right = mid - 1 
                
        return left