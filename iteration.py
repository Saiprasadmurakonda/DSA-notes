# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def reverseList(self, head):
        if head==None:
            return head
        prev=None
        curr=head
        while curr!=None:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next
        return prev




