def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    def helper(ls, acc):
        if len(ls) == 0:
            return acc
        # this is a tail recursion because the final instruction is a recursive call.
        return helper(ls[1:], ls[0] + acc)
    
    return helper(ls, 0)

sum_tail_recursion([0,1,2])


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def helper(root, dept):
            if not root:
                return dept

            return max(helper(root.left, 1 + dept), helper(root.right, 1 + dept))

        return helper(root, 0)


        ## Solution DFS
        # if not root:
        #     return 0
        # else:
        #     left_dept = self.maxDepth(root.left)
        #     right_dept = self.maxDepth(root.right)

        # return max(left_dept, right_dept) + 1


        ## Solution Iteration
        # stack = []
        # if stack is not None:
        #     stack.append((1, root))

        # dept = 0
        # while stack != []:
        #     current_dept, root = stack.pop()
        #     if root is not None:
        #         dept = max(current_dept, dept)
        #         stack.append((current_dept + 1, root.left))
        #         stack.append((current_dept + 1, root.right))

        # return dept



        ## Solution else.
        # return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0

node2 = TreeNode(val = 10)
node3 = TreeNode(val = 30)
node1 = TreeNode(0, node2, node3)

Solution().maxDepth(node1)