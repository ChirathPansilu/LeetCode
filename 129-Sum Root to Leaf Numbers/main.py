# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    # Time O(N) PreOrder Traversal
    # Space O(Height of the tree) | Worst Case O(N) 
    # N - Number of Nodes
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.preOrder(root, '') 
        return self.total
        
    def preOrder(self, root, path):
        path += str(root.val)

        if not root.left and not root.right:
            self.total += int(path)
            return 
        
        if root.right:
            self.preOrder(root.right, path)
            
        if root.left:
            self.preOrder(root.left, path)