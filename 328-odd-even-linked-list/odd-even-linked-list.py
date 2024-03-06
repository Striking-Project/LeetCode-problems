# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        odd_tail = odd_head
        even_tail = even_head
        
        while even_tail and even_tail.next:
            odd_tail.next, odd_tail = even_tail.next, even_tail.next
            even_tail.next, even_tail = odd_tail.next, odd_tail.next
        
        odd_tail.next = even_head
        
        return odd_head
