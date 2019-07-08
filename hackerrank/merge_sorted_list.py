#https://leetcode.com/problems/merge-two-sorted-lists/discuss/9989/Python-easy-to-understand-solution

# class SingleLinkedList:
#     def __init__(self):
#         "constructor to initiate this object"
#
#         self.head = None
#         self.tail = None
#         return
#     def add_list_item(self, item):
#         "add an item at the end of the list"
#
#         if not isinstance(item, ListNode):
#             item = ListNode(item)
#
#         if self.head is None:
#             self.head = item
#         else:
#             self.tail.next = item
#
#         self.tail = item
#
#         return
#     def output_list(self):
#         "outputs the list (the value of the node, actually)"
#         current_node = self.head
#
#         while current_node is not None:
#             print('current node: ',current_node.data)
#
#             # jump to the linked node
#             current_node = current_node.next
#
#         return
#
# track = SingleLinkedList()
# for current_item in [node1, node2, node3, node4]:
#     track.add_list_item(current_item)
#     #print("track length: %i" % track.list_length())
#     track.output_list()

# l1 =1->2->4
# l2 = '1->3->4'

#define listnode class
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6




class Solution(object):
    def linkedlistsolution(self,head,node):
        currentNode = head
        currentNode = node
        #node_array = []
        while currentNode is not None:
            #node_array.append(currentNode.value)
            print(currentNode.val)
            currentNode = currentNode.next
        #return(node_array)
        return

head = node1
while head is not None:
    print(head.val)
    head = head.next


###come back to it
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #dummy is necessary for the initial state
        dummyHead = ListNode(None)
        curNode   = dummyHead
        while True:
            # When one node becomes empty
            if not l1:
                curNode.next = l2
                l2 = None
                break
            if not l2:
                curNode.next = l1
                l1 = None
                break

            if l1.val > l2.val:
                curNode.next = l2
                l2 = l2.next
            else:
                curNode.next = l1
                l1 = l1.next
            curNode = curNode.next

        return dummyHead.next
# wrong solution:
def mergeTwoLists(l1, l2):
    l1 = l1.
    l1_list = l1.split('->')
    l2_list = l2.split('->')

    concat_list = l2_list + l1_list

    concat_list = sorted(concat_list)

    output = '->'.join(concat_list)

return(output)
