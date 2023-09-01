# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        pointer=head
        res=[]
        while(pointer):
            res.append(pointer.val)
            pointer=pointer.next
            i+=1
        
        node=None
        for j in range(len(res)-1,-1,-1):
            if(j==(i-n)):
                continue
            node=ListNode(val=res[j], next=node)

        return node
