class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder_print':
            return(self.preorder_print(self.root, ''))
    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + '--'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return(traversal)



tree = BinaryTree(3)
tree.root.left = Node(5)
tree.root.left.left = Node(10)
tree.root.right = Node(4)

tree.root.left.left.value
print(tree.print_tree('preorder_print'))
