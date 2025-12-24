class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self,root):
        #Base Case
        if root is None:
            return
        #Recursive Case
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)    
        return self.ans