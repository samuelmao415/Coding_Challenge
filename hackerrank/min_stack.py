class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.min_stack.insert(0,x)


    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop(0)


    def top(self):
        """
        :rtype: int
        """
        return(self.min_stack[0])

    def getMin(self):
        """
        :rtype: int
        """
        return(min(self.min_stack))




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
