# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# ---------
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# ---------
# Input: head = [1], n = 1
# Output: []

# Example 3:
# ---------
# Input: head = [1,2], n = 1
# Output: [1]


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Greedy Approach
# Time Complexity O(n)
# Space Complexity O(1)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head
        i, traverseTill = 0, length - n - 1

        if traverseTill == -1:
            return head.next

        while i < traverseTill:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head
