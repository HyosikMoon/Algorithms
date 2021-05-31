class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        # if root.val == val:
        #     return root
        # if root.left != None:
        #     out = self.searchBST(root.left, val)
        #     if out != []:
        #         return out
        # if root.right != None: #  root.right != None
        #     out = self.searchBST(root.right, val)
        #     if out != []:
        #         return out
        # return []

        if root == None or root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

node1 = TreeNode(4, left = None, right = None)
node2 = TreeNode(2, left = None, right = None)
node3 = TreeNode(7, left = None, right = None)
node4 = TreeNode(1, left = None, right = None)
node5 = TreeNode(3, left = None, right = None)
node6 = TreeNode(5, left = None, right = None)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

Solution().searchBST(node1, 7)