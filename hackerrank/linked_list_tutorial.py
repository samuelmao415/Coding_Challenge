#coding a linked-list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('None')
        else:
            cur_node = self.head
            while cur_node:
                print(cur_node.data)
                #print('next.data:', cur_node.next.data)
                cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next: #go to the end of the list
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """
        add new node to the beginning
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            print('previous node not in the list')
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """
        delete by key
        """
        cur_node = self.head
        #scenario 1: if head is the key
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        #scenario 2: if head is not the key
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self,pos):
        cur_node = self.head
        #scenario 1: if head is the key
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        #scenario2: if head is not the key
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return(count)

    def len_recursive(self, node): #node is self.head
        if node is None:
            return(0)
        return(1 + self.len_recursive(node.next))

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        cur_node_1 = self.head
        while cur_node_1 and cur_node_1.data != key_1:
            prev_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        prev_2 = None
        cur_node_2 = self.head
        while cur_node_2 and cur_node_2.data != key_2:
            prev_2 = cur_node_2
            cur_node_2 = cur_node_2.next

        if not cur_node_1 or not cur_node_2:
            return

        if prev_1:
            prev_1.next = cur_node_2
        else:
            prev_1 = cur_node_1

        if prev_2:
            prev_2.next = cur_node_1
        else:
            prev_2 = cur_node_2

        cur_node_1.next, cur_node_2.next = cur_node_2.next, cur_node_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:

            nxt = cur.next
            print('nxt:', cur.next)
            cur.next = prev
            prev = cur
            print('prev: ', prev.data)
            cur = nxt
        self.head = prev

    def reverse_recursive(self): #write later
        pass

    def merge_sorted(self,llist):
        p = self.head
        q = llist.head
        s = None
        if p.data<=q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return(new_head)

    def remove_duplicates(self):
        cur = self.head
        no_dup = {}
        prev = None
        while cur:
            if cur.data in no_dup:
                prev.next = cur.next
                cur = None
            else:
                no_dup[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):
        nth_from_last = self.len_iterative()
        cur = self.head
        while cur:
            if n == nth_from_last:
                print(cur.data)
                return
            else:
                nth_from_last -= 1
                cur = cur.next

    def rotate(self, k):
        cur = self.head
        first_cur = self.head
        length = self.len_iterative()
        order = 1
        while cur:
            if order == k:
                cur_after_k = cur.next
                cur.next = None
                break
            else:
                cur = cur.next
                order += 1
        self.head = cur_after_k

        rotate_order = 1
        while rotate_order < length - k:
            cur_after_k = cur_after_k.next
            rotate_order += 1


        cur_after_k.next = first_cur

    def sum_two_lists(self, llist):
        #new_node = Node(None)
        new_list = LinkedList()
        l1 = self.head
        l2 = llist.head

        while l1 and l2:
            new_list.append(l1.data + l2.data)
            l1 = l1.next
            l2 = l2.next

        return(new_list)


llist = LinkedList()

llist.append('A')
llist.append('B')
#llist.prepend('C')
llist.append('C')
llist.append('D')
llist.append('A')
llist.append('D')
llist.print_nth_from_last(2)
llist.reverse_iterative()
#llist.insert_after_node(llist.head.next, 'E')
#llist.delete_node_at_pos(2)
llist.len_iterative()
llist.swap_nodes('B','C')
llist.print_list()
llist.remove_duplicates()


llist_1 = LinkedList()
llist_2 = LinkedList()


llist_1.append(1)
llist_1.append(2)
llist_1.append(3)
llist_1.append(4)
llist_1.append(5)


llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

res = llist_1.sum_two_lists(llist_2)
res.print_list()

llist_1.merge_sorted(llist_2)
llist_1.data()
