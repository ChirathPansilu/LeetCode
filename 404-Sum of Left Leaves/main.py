# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.preOrder(root)
        return self.total
    
    # Using preOrder traversal 
    # Time O(n) | Space O(Height of the tree) - Worst Case O(n)
    def preOrder(self, root):
        if (not root.left) and (not root.right):
            return
        
        if root.left:
            #Check if left node is a leaf
            if (root.left.left == None) and (root.left.right == None):
                self.total += root.left.val
                
            self.preOrder(root.left)
        
        if root.right:
            self.preOrder(root.right)