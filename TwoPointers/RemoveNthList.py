'''
Given a singly linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data, next=None):
#         self.data = val
#         self.next = next

class Solution:
    def remove_nth_last_node(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        
        # move right n steps forward
        for i in range(n):
            right = right.next

        if not right:
            return head.next

        while right.next:
            right = right.next
            left = left.next

        # at this point, left pointer points to (n-1)th element.
        left.next = left.next.next
        
        return head