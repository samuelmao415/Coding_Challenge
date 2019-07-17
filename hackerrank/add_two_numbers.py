# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret

        l1_result = []
        while l1:
            print('l1', l1.val)
            l1_result.append(l1.val)
            l1=l1.next

        l2_result = []
        while l2:
            print('l2', l2.val)
            l2_result.append(l2.val)
            l2=l2.next

        l1_result = l1_result[::-1]
        l2_result = l2_result[::-1]
        l1_result = [str(l) for l in l1_result]
        l2_result = [str(l) for l in l2_result]
        l1_numerals = int("".join(l1_result))
        l2_numerals = int("".join(l2_result))
        sum_ = l1_numerals + l2_numerals
        sum_list = list(str(sum_))
        sum_list = sum_list[::-1]
        #ln = ListNode(0)
        print(sum_list)



        for s in sum_list:
            cur.next = ListNode(s)
            cur = cur.next




        return(ret.next)



#better answer
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        cur = ret
        add = 0

        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = val / 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ret.next
