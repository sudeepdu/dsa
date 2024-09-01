class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def arrayToLL(self,arr):
        if not arr:
            return
        self.head=Node(arr[0])
        frnt=self.head
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            frnt.next=new_node
            frnt=frnt.next

    def print(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next


arr=[1,2,3,4,5,6]
obj=SLL()
obj.arrayToLL(arr)
obj.print()
