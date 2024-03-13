# GOOGLE

# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Example 1
# ---------
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2
# ---------
# Input: head = [], val = 1
# Output: []

# Example 3
# ---------
# Input: head = [7,7,7,7], val = 7
# Output: []


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n)
# Space complexity O(1)


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

print(Solution().removeElements(node1, val=1))
