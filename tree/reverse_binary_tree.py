class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):


        #DFS recursively

        #base case
        if not root:
            return None
        
        #swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        #recursion invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root