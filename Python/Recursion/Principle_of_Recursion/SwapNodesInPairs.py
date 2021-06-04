class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # Recursion
        # if not head or not head.next:
        #     return head
        
        # first_node = head
        # second_node = head.next

        # first_node.next = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # return second_node

        # Recursive review1
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

        # Iterative


# test #

n1 = ListNode()
n2 = ListNode()
n3 = ListNode()
n4 = ListNode()

n1.value = 1
n2.value = 2
n3.value = 3
n4.value = 4

n1.next = n2
n2.next = n3
n3.next = n4

sp = Solution()
sp.swapPairs(n1)

