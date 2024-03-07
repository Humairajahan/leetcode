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


# Two Pointer Approach
# Time Complexity O(n)
# Space Complexity O(1)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next_val = curr.next
            curr.next = prev
            prev = curr
            curr = next_val
        return prev


# Example
# ---------
# Input: head = [1, 2, 3]

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

case = Solution().reverseList(node1)
print(case)
