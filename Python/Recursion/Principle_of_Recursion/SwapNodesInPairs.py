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
        ## Recursion solution
        # # If the list has no node or has only one node left.
        # if not head or not head.next:
        #     return head

        # # Nodes to be swapped
        # first_node = head
        # second_node = head.next

        # # Swapping
        # first_node.next  = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # # Now the head is the second node
        # return second_node


        # ## Recursive review1
        # if not head or not head.next:
        #     return head
        
        # first_node = head
        # second_node = head.next

        # first_node.next = self.swapPairs(second_node.next)
        # second_node.next = first_node

        # return second_node


        ## Recursion review 2
        # Base case
        if not head or not head.next:
            return head

        # Setting
        first_node = head
        second_node = head.next

        # Swap
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


        ## Iteration Solution
        # # Dummy node acts as the prevNode for the head node
        # # of the list and hence stores pointer to the head node.
        # dummy = ListNode(-1)
        # dummy.next = head

        # prev_node = dummy

        # while head and head.next:

        #     # Nodes to be swapped
        #     first_node = head;
        #     second_node = head.next;

        #     # Swapping
        #     prev_node.next = second_node
        #     first_node.next = second_node.next
        #     second_node.next = first_node

        #     # Reinitializing the head and prev_node for next swap
        #     prev_node = first_node
        #     head = first_node.next

        # # Return the new head node.
        # return dummy.next


        # ## Iteration review 
        # dummy = ListNode(-1)
        # dummy.next = head

        # prev_node = dummy
        # while head and head.next:
        #     # Setting
        #     first_node = head
        #     second_node = head.next

        #     # Swap
        #     prev_node.next = second_node
        #     first_node.next = second_node.next
        #     second_node.next = first_node
            
        #     # Preparation for next step
        #     prev_node = first_node
        #     head = first_node.next

        # return dummy.next

        ## Interation review 2
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # Setting
            first_node = head
            second_node = head.next
            prev_node.next = second_node

            # Swap
            first_node.next = second_node.next
            second_node.next = first_node

            # Preparation for next step
            prev_node = first_node
            head = first_node.next

        return dummy.next


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

