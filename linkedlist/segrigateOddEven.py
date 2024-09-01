class Solution(object):
    def oddEvenList(self, head):
        if head==None or head.next==None:
            return head
        odd=head
        even=head.next
        ev_head=head.next
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next
        odd.next=ev_head
        return head 