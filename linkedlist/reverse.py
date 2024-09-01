# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        itr=head
        prv=None
        while itr:
            frnt=itr.next
            itr.next=prv
            prv=itr
            itr=frnt
        return prv