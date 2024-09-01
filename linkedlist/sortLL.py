#Brute force apporch
class Solution(object):
    def sortList(self, head):
        arr=[]
        itr=head
        while itr:
            arr.append(itr.val)
            itr=itr.next
        arr.sort()
        itr=head
        i=0
        while itr:
            itr.val=arr[i]
            i+=1
            itr=itr.next
        return head
        