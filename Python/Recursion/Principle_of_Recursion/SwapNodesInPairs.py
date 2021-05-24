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
        if head == None:
            return
        
        temp = head.next
        next_head = head.next.next
        if head.next.next == None:
            head.next = None
            temp.next = head
        elif head.next.next.next == None:
            head.next = None
            temp.next = head
        else:
            head.next = head.next.next.next
            temp.next = head
        
        return self.swapPairs(next_head)


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

