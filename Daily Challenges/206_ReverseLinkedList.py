# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1
# ---------
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2
# ---------
# Input: head = [1,2]
# Output: [2,1]

# Example 3
# ---------
# Input: head = []
# Output: []


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n)
# Space complexity O(1)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt_val = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_val
        return prev
