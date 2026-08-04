# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curious = {}

        if list1 == None and list2 == None:
            return None
        
        while list1 != None:
            curious[list1] = list1.val
            list1 = list1.next

        while list2 != None:
            curious[list2] = list2.val
            list2 = list2.next

        temp = list(sorted(curious.items(), key=lambda item: item[1]))

        for i in range(len(temp) - 1):
            temp[i][0].next = temp[i+1][0]

        temp[-1][0].next = None

        return temp[0][0]

