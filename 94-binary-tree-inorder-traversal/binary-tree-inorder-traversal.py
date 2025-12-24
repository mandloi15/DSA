class Solution:
    def __init__(self):
        self.ans=[]
    def inorder(self,root):
        #base case
        if root is None:
            return
        #recursive case
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.inorder(root)
        return self.ans
        