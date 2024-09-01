# Definition for singly-linked list.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head