class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # cur = dummy = ListNode()

        # while list1 and list2:               
        #     if list1.val < list2.val:
        #         cur.next = list1
        #         list1, cur = list1.next, list1
        #     else:
        #         cur.next = list2
        #         list2, cur = list2.next, list2
                
        # if list1 or list2:
        #     cur.next = list1 if list1 else list2
            
        # return dummy.next

        temp = ListNode()
        head = ListNode()
        temp = head

        if (not list1) and (not list2): return head.next

        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                temp.next = list2
                temp = temp.next
                if list2.next == None: 
                    list2 = list2.next
                    break
                else: list2 = list2.next
            else:
                temp.next = list1
                temp = temp.next
                if list1.next == None:
                    list1 = list1.next
                    break
                else: list1 = list1.next

        if list1 or list2: temp.next = list1 if list1 else list2

        return head.next

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)
node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
list1 = node1
list2 = node4
node = ListNode()
# leftL = node
# leftL = node1
# print("leftL:", leftL.val)
# print("node:", node.val)

print(type(node))

sol = Solution()
print(sol.mergeTwoLists(list1, list2).val)
