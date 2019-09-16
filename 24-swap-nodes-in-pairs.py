# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        t=head
        l=None
        while True:
            if t==None or t.next==None:
                return head
            tt=t.next
            t.next=tt.next
            tt.next=t
            if l==None:
                head=tt
            else:
                l.next=tt
            l=t
            t=t.next
        return head
        