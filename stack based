# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def reverseList(self, head):
        # 1. Base case - Easy peesy
        if head==None:
            return
        st=[]

        # 2. Add all nodes to stack
        curr=head
        while curr!=None:
            st.append(curr)
            # 3. Current node is added. Add next node
            curr=curr.next
        
        # 4. Last added node will become the new head in reversed Linked List
        head=st.pop()

        # 5. For better clarity to the next node, we store head as prev. 
        prev=head
        while len(st)!=0:
            # pop the top most node. That node should be our current node and prev popped node should point to this.
            # This is the reason we pointed prev to head which is already popped. 
            curr=st.pop()
            prev.next=curr
            # To continue the process across the linkedlist, this will help
            prev=curr
        # Why? Because the last node, 2 in our case is pointing to 3. We did not change it to point to null.
        # If we dont, it will make it to a cyclic linked list.
        prev.next=None
        return head
