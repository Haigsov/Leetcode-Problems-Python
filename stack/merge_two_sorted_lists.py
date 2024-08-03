# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1, curr2 = list1, list2

        if curr1 >= curr2:
            res = ListNode(val = curr2.val, next = None)
            curr2 = curr2.next
        else:
            res = ListNode(val = curr1.val, next = None)
            curr1 = curr1.next

        while curr1 and curr2:


        