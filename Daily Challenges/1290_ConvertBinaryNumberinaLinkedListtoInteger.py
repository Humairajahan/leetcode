# 1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.


# Example 1
# ---------
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2
# ---------
# Input: head = [0]
# Output: 0


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Array (Power of 2)
# Time complexity O(n)
# Space complexity O(n)


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        while head:
            binary.append(head.val)
            head = head.next

        length = len(binary)
        bin_num = 0
        for i in range(length):
            bin_num += binary[i] * 2 ** (length - 1 - i)
        return bin_num


# Greedy approach
# Time complexity O()
# Space complexity O()


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_num = 0
        while head:
            bin_num = bin_num * 2 + head.val
            head = head.next
        return bin_num


node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)

node1.next = node2
node2.next = node3


print(Solution().getDecimalValue(node1))
