# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lis =[]
        while head:
            lis.append(head.val)
            head = head.next


        ret = ListNode(0)
        cur = ret
        for s in lis[::-1]:
            cur.next = ListNode(s)
            cur = cur.next

        return(ret.next)
        
