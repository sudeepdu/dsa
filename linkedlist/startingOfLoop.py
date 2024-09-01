class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow