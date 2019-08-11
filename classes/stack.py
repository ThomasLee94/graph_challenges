#!python

from classes.linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # ll class method
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    # ─── TOP IS HEAD ─────────────────────────────────────────────────

    # ─── BOTTOM IS TAIL ──────────────────────────────────────────────

    def push(self, item):
        """Insert the given item on the top of this stack."""
        # ! Best & worst case runtime = O(1), not dependent on length of ll

        # append node to the tail
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""

        # case: tail node is empty
        if self.list.is_empty():
            return None
        # return tail data
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""

        # ! Worst & best case runtime = O(1), not dependent on length of ll

        # case: ll length is 0
        if self.list.length() == 0:
            raise ValueError('Linked list length is 0')
        # case: top node is empty
        if self.list.is_empty():
            raise ValueError("Node is empty")
        # delete tail node
        item = self.list.head.data
        self.list.delete(item)
        return item

