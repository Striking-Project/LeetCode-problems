# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_twin_sum = float('-inf')

        # Use a stack to store the values of the first half of the linked list
        stack = []

        # Traverse the linked list to find the middle
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # Traverse the second half of the linked list and calculate twin sums
        while slow:
            twin_sum = slow.val + stack.pop()
            max_twin_sum = max(max_twin_sum, twin_sum)
            slow = slow.next

        return max_twin_sum
