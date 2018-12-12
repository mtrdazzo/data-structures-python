class Empty(Exception):
    pass


class CircularQueue:
    """Queue implementation using circularly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', 'next'

        def __init__(self, element):
            """Create an empty node"""
            self._element = element
            self.next = None

    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the list is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the first element in the list"""

        if self.is_empty():
            raise Empty("List is empty")
        head = self._tail.next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (FIFO)"""
        if self.is_empty():
            raise Empty("List is empty")
        oldhead = self._tail.next

        if self._size == 1:
            self._tail = None
        else:
            self._tail.next= oldhead.next
        self._size -= 1

        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e)
        if self.is_empty():
            newest.next= newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail.next

    def num_elements(self):
        """Find number of elements in the circularly linked list"""
        result = 0
        current_node = self._tail

        if current_node is not None:
            result = 1
            while current_node.next is not self._tail:
                current_node = current_node.next
                result += 1
        return result

    def get_Node(self, value):
        curr = self._tail

        while curr is not None and curr._element != value:
            curr = curr.next

        return curr

def sameList(a, b):
    """Find out if two nodes are in the same circularly linked list"""
    if a is None or b is None:
        return False
    if a is b:
        return True

    curra = a

    while curra.next is not a:
        if curra is b:
            return True
        curra = curra.next
    return False

if __name__ == "__main__":
    import unittest

    class testCLL(unittest.TestCase):

        def setUp(self):
            self.cq = CircularQueue()

        def test_num_elements(self):
            self.assertTrue(self.cq.num_elements() == 0)
            self.cq.enqueue(1)
            self.assertTrue(self.cq.num_elements() == 1)
            self.cq.enqueue(2)
            self.assertTrue(self.cq.num_elements() == 2)


    cq = CircularQueue()
    cq1 = CircularQueue()
    for i in range(5):
        cq.enqueue(i)
        cq1.enqueue(i)

    a = cq.get_Node(3)
    b = cq1.get_Node(2)

    print(sameList(b, b))
