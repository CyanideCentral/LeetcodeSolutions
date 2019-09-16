# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t=head
        r=head
        rl=None
        for i in range(n-1):
            t=t.next
        while True:
            if t.next==None:
                if r==head:
                    return r.next
                rl.next=r.next
                return head
            t=t.next
            if r==head:
                rl=r
            else:
                rl=rl.next
            r=r.next
        return head