class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        new_head=reverse(slow.next)
        first=head
        second=new_head
        while second:
            if first.val!=second.val:
                reverse(new_head)
                return False
            first=first.next
            second=second.next
        reverse(new_head)
        return True

def reverse(itr):
        prv=None
        while itr:
            frnt=itr.next
            itr.next=prv
            prv=itr
            itr=frnt
        return prv