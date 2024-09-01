class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_node=ListNode(-1)
        curr=dummy_node
        t1=l1
        t2=l2
        carry=0
        while t1 or t2:
            sum=carry
            if t1:
                sum+=t1.val
            if t2:
                sum+=t2.val
            new_node=ListNode(sum%10)
            carry=sum//10
            curr.next=new_node
            curr=curr.next

            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        if carry==1:
            new_node=ListNode(1)
            curr.next=new_node
        return dummy_node.next 
        