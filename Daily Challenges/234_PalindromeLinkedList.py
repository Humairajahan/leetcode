# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1
# ---------
# Input: head = [1,2,2,1]
# Output: true

# Example 2
# ---------
# Input: head = [1,2]
# Output: false


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Array
# Time complexity O(n)
# Space complexity O(n)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]


# Tortoise-Hare algorithm
# Reverse Linked List
# Two pointer approach

# Time complexity O(n)
# Space complexity O(1)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Find middle node (slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half (slow - fast)
        prev = None
        while slow:
            nxt_node = slow.next
            slow.next = prev
            prev = slow
            slow = nxt_node

        # Check palindrome
        left, right = head, prev
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

print(Solution().isPalindrome(node1))
