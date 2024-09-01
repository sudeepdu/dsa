class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        current=head
        length=1
        while current.next:
            length+=1
            current=current.next
        current.next=head
        k=k%length
        steps=length-k-1
        new_tail=head
        for _ in range(steps):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head
