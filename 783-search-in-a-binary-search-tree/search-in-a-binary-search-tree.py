
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None

        curr = root
        while curr != None:
            if curr.val == target:
                return curr
            elif target < curr.val:
                #left
                curr = curr.left
            else:
                #right
                curr = curr.right
        return None

        