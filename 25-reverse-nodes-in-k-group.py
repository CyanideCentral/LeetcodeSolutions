# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        if k==1:
            return head
        h=head
        l=0
        while True:
            l=l+1
            h=h.next
            if h==None:
                break
        n=head
        last=None
        for i in range(l//k):
            tail=n
            ht=None
            for j in range(k):
                t=n.next
                n.next=ht
                ht=n
                if j==k-1:
                    h=n
                n=t
            if last!=None:
                last.next=h
            last=tail
            tail.next=n
            if tail==head:
                head=h
        return head
                
            