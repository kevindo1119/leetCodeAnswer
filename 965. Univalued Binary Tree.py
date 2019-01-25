# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    res = True
    
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        vals = []
        
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        return len(set(vals)) is 1
