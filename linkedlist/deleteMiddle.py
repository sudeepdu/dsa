class Solution(object):
    def deleteMiddle(self, head):
        if head is None or  head.next is None:
            return None
        slow=head
        fast=head
        prv=None
        while fast and fast.next:
            prv=slow
            slow=slow.next
            fast=fast.next.next
        prv.next=slow.next
        return head