def addOne(head):
    # write your code here
    carry=helper(head)
    if carry==1:
        new_node=Node(1)
        new_node.next=head
        return new_node
    return head

def helper(temp):
    if temp==None:
        return 1
    carry=helper(temp.next)
    temp.data=temp.data+carry
    if temp.data<10:
        return 0
    temp.data=0
    return 1