# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Example 1
# ---------
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2
# ---------
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Greedy Approach
# Time Complexity O(n)
# Space Complexity O(1)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length % 2 == 0:
            middle_node = int(length / 2) + 1
        else:
            middle_node = int(length / 2 + 0.5)

        curr = head
        for i in range(middle_node - 1):
            curr = curr.next
        return curr


# Set Approach
# Time Complexity O(n)
# Space Complexity O(n)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        z = {}
        curr = head

        while curr:
            length += 1
            z[length] = curr
            curr = curr.next

        if length % 2 == 0:
            middle_node = int(length / 2) + 1
        else:
            middle_node = int(length / 2 + 0.5)

        return z[middle_node]


# Two Pointers
# Time Complexity O(n/2) simplifying to O(n)
# Space Complexity O(1)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Example
# ---------
# Input: head = [1, 2, 3]

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

case = Solution().middleNode(node1)
print(case)
