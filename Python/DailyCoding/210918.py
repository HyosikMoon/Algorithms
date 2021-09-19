class Solution:
    def addTwoNumbers(self, l1, l2):
        # l1V
        d1 = len(l1) - 1
        l1.reverse()
        l1V = 0
        for i, n in enumerate(l1):
            l1V += pow(10, d1 - i) * n
            
        # l2V
        d1 = len(l2) - 1
        l2.reverse()
        l2V = 0
        for i, n in enumerate(l2):
            l2V += pow(10, d1 - i) * n
            
        # l1V + l2V
        val = l1V + l2V
        
        # l3
        s_val = str(val)
        output = []
        for i, n in enumerate(s_val):
            output.append(int(n))
        output.reverse()
        
        return output

sol = Solution()
sol.addTwoNumbers([2,4,3], [5,6,4])
sol.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def addTwoNumbers2(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

sol2 = Solution2()
l1 = ListNode(3)
l1.next = ListNode(9)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(8)
l2.next.next = ListNode(7)

sol2_val = sol2.addTwoNumbers2(l1, l2)
# sol.addTwoNumbers2([9,9,9,9,9,9,9], [9,9,9,9])