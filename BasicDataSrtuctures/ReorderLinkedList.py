'''
Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as follows:

L0 → L1 → L2 → … → Ln−2 → Ln−1 → Ln

This is how you’ll reorder it:

L0 → Ln → L1 → Ln−1 → L2 → Ln−2 → …
'''

class Solution:
	def reorder_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
	    if not head:
	        return head
	    slow = fast = head
	    
	    # find the middle of linked list
	    while fast and fast.next:  
	        slow = slow.next
	        fast = fast.next.next 
	    prev, curr = None, slow

	    # reverse the second part of the list
    	# convert 1->2->3->4->5->6 into 1->2->3 and 6->5->4
	    while curr:
	        curr.next, prev, curr = prev, curr, curr.next     
	    first, second = head, prev

	    # merge two sorted linked lists
    	# merge 1->2->3 and 6->5->4 into 1->6->2->5->3->4
	    while second.next:
	        first.next, first = second, first.next
	        second.next, second = first, second.next
	    
	    return head