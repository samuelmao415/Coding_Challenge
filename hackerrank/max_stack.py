class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_list.insert(0,x)


    def pop(self):
        """
        :rtype: int
        """

        return(self.stack_list.pop(0))


    def top(self):
        """
        :rtype: int
        """
        return(self.stack_list[0])


    def peekMax(self):
        """
        :rtype: int
        """
        return(max(self.stack_list))

    def popMax(self):
        """
        :rtype: int
        """
        return(self.stack_list.pop(self.stack_list.index(max(self.stack_list))))




# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
