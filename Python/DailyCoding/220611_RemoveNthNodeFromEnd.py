class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next == None and n == 1: return None        

        # Find the number of nodes
        count = 1
        item = head
        while item.next != None:
            count += 1; item = item.next

        # Find the (N-1)th node from the end
        index = 1
        preIndex = count - n
        if preIndex == 0:
            head = head.next
            return head
        item = head
        while index != preIndex:
            item = item.next
            index += 1

        # Fix (N-1).next to (N+1)th node or None
        if item.next != None:
            item.next = item.next.next

        return head

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print("Node3's next1:", node3.next.val)

sol = Solution()
sol.removeNthFromEnd(node1, 2)
print("Node3's next2:", node3.next.val)