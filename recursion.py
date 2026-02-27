# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(curr, prev):
    # 1. Base Case: If we hit the end, the previous node is our new head
    if not curr:
        return prev
    
    # 2. Save the next node before we sever the link
    next_node = curr.next
    
    # 3. Reverse the pointer
    curr.next = prev
    
    # 4. Move forward recursively
    return reverse(next_node, curr)

class Solution(object):
    def reverseList(self, head):
        # Handle empty list or single node
        if not head:
            return head
        return reverse(head, None)
