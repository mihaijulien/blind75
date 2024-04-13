'''
The task is to reverse the nodes in groups of k in a given linked list, where k is a positive integer, and at most the length of the linked list. If any remaining nodes are not part of a group of k, they should remain in their original order.

It is not allowed to change the values of the nodes in the linked list. Only the order of the nodes can be modified.

eg.

Input

k=3
head -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL

Output:

head -> 3 -> 2 -> 1 -> 4 -> 5 -> NULL
'''

from typing import Optional
from typing import Tuple

class Solution:
    def reverse_k_groups(self, head: Optional[ListNode], k: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        dummy = LinkedListNode(0)
        dummy.next = head
        ptr = dummy


        while(ptr != None):

            tracker = ptr

            for i in range(k):

                if tracker == None:
                    break
           
                tracker = tracker.next

            if tracker == None:
                break

            previous, current = self.reverse_linked_list(ptr.next, k)

            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = current
            ptr.next = previous
            ptr = last_node_of_reversed_group

        return dummy.next



    def reverse_linked_list(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        previous, current, next = None, head, None

        for _ in range(k):
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        return previous, current
