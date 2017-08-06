"""

Stack: A stack is an ordered collection of items where the addition of new items and the 
removal of existing items always takes place at the same end.

The end is commonly referred to as the 'top'
The end opposite of the top is known as the 'bottom'

The base of the stack is significant since items stored in the stack that are closer to the 
base represent those that have been in the stack the longest.

The most recently added items are the ones that are in the position to be removed first.

This ordering is known as the LIFO (last-in, first-out)
It provides ordering based on the length of time in the collection.

New items are near the top, older items are near the bottom



Oldest(added last, removed last)					Newest(added first, removed first)	

 <- (Bottom, base) ------------------------------------------------------- (Top) ->


The first items that were pushed to the stack are at the base.
The order of insertion is the reverse of removal.

An example of a stack would be a back button in a web browser

"""

# Implementing our own Stack class

class Stack(object):

    def __init__(self):
        # Initiates with an empty list
        self.items = []

    def isEmpty(self):
        # if the list is empty, returns True - if not, returns False
        return self.items == []

    def push(self, item):
    	# Adds items to the Stack class' item list using the append() method
    	# The append method will add new items to the top of the Stack.
    	# https://www.tutorialspoint.com/python/list_append.htm
        self.items.append(item)

    def pop(self):
    	# Removes items from the Stack class's item list using the pop() method.
    	# The pop method will remove the items at the top of stack.
    	# https://www.tutorialspoint.com/python/list_pop.htm
        return self.items.pop()

    def peek(self):
        # Returns last item in the list
        # An index of -1 in a list will return the last item of the list.
        return self.items[-1]
        # Alternative
        # return self.items[len(self.items) - 1]

    def size(self):
    	# Returns the length of item of list
        return len(self.items)

