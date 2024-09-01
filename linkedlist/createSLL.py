class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=new_node
    def insert_at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_index(self,index,data):
        count=0
        if index<0:
            raise IndexError('Index out of range')
        new_node=Node(data)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return
        count=0
        itr=self.head
        while itr is not None and count<index-1:
            itr=itr.next
            count+=1
        if itr is None:
            raise IndexError("Index out of range")
        new_node.next=itr.next
        itr.next=new_node
        
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def print(self):
        itr=self.head
        while itr:
            print(itr.data, end="-->")
            itr=itr.next
    
    def delete_node(self,data):
        if self.head is None:
            print('List id=s empty')
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next



ll=SLL()
ll.append(67)
ll.append(45)
ll.append(42)
ll.append(44)
ll.insert_at_begining(12)
ll.insert_at_begining(32)
ll.insert_at_index(0,11)
ll.insert_at_index(1,12)
ll.print()
print('')
ll.delete_node(32)
ll.print()
print('')
print(ll.get_length())