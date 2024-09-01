def lenLoop(self,head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return findLen(slow,fast)
    return 0
def findLen(slow,fast):
    count=1
    while fast and fast.next:
        fast=fast.next
        if fast==slow:
            return count
        count+=1