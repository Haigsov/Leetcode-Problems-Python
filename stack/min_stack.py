class MinStack(object):

    def __init__(self):
        """
        Initializes a new instance of the MinStack class.
        """
        self.stack = []        # This stack keeps track of all elements in the stack.
        self.min_stack = []    # This auxiliary stack keeps track of the minimum value at each level of the stack.

    def push(self, val):
        """
        Pushes a new integer value onto the stack and updates the minimum value stack.
        
        :type val: int  # The integer value to be pushed onto the stack.
        :rtype: None   # This method does not return anything.
        """
        self.stack.append(val)  # Push the value onto the main stack.
        # Determine the new minimum value. If min_stack is not empty, take the smaller of the new value and the current minimum.
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)  # Push the new minimum value onto the min_stack.

    def pop(self):
        """
        Removes the top element from the stack and updates the minimum value stack accordingly.
        
        :rtype: None  # This method does not return anything.
        """
        self.stack.pop()         # Remove the top element from the main stack.
        self.min_stack.pop()     # Remove the corresponding minimum value from the min_stack.

    def top(self):
        """
        Retrieves the top element of the stack without removing it.
        
        :rtype: int  # Returns the top element of the stack.
        """
        return self.stack[-1]    # Return the top element of the main stack.

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        
        :rtype: int  # Returns the minimum element currently in the stack.
        """
        return self.min_stack[-1]  # Return the top element of the min_stack, which is the minimum value.
