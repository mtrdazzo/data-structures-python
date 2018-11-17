class Empty(Exception):
    pass


class LinkedStack:
    """LIFO Stack implementation using a linked list"""

    class _Node:
        """Lightweight, non-public class for storing a singly linked node"""
        __slots__ = '_data', '_next'

        def __init__(self, data, next = None):
            """Create an empty Node"""
            self._data = data
            self._next = next

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def _len(self):
        """Return number of elements in the linked stack"""
        return self._size

    def is_empty(self):
        """Return True if no elements in the linked stack"""
        return self._size == 0

    def push(self, e):
        """Push an element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._data

    def pop(self):
        """Pop the element off the top of the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        top = self._head._data
        self._head = self._head._next
        self._size -= 1
        return top

class LinkedQueue:
    """FIFO Queue ADT using a linked list internal data structure"""
    class _Node:
        """Lightweight, non-public class for storing a singly linked list"""
        __slots__ = '_data', '_next'

        def __init__(self, data):
            """Create an empty node"""
            self._data = data
            self._next = next

    def __init__(self):
        """Create an empty linked queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def enqueue(self, e):
        """Add an element e to the tail of the queue"""
        new = self._Node(e)

        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new

        self._size += 1

    def front(self):
        """Return (but do not remove) the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._data

    def back(self):
        """Return (but do not remove) the back of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._tail._data

    def dequeue(self):
        """Remove element e from the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        e = self._head._data
        self._size -= 1
        self._head = self._head._next

        if self.is_empty():
            self._tail = None
        return e


if __name__ == '__main__':
    import unittest

    class TestLinkedStack(unittest.TestCase):

        def setUp(self):
            self.ls = LinkedStack()

        def tearDown(self):
            self.ls = None

        def test_no_nodes(self):

            #Verify no nodes in linked list
            self.assertTrue(self.ls.is_empty())

            #Try to pop node off top of empty stack
            with self.assertRaises(Empty):
                self.ls.pop()

            #Try to return the top node off top of empty stack
            with self.assertRaises(Empty):
                self.ls.top()

        def test_adding_nodes(self):

            #Add element to the top of the stack
            self.ls.push(1)
            self.assertFalse(self.ls.is_empty())
            self.assertTrue(self.ls.top() == 1)

            #Add more elements
            for i in range(2, 11):
                self.ls.push(i)
                self.assertTrue(self.ls.top() == i)

        def test_removing_nodes(self):

            for i in range(1, 11):
                self.ls.push(i)
                self.assertTrue(self.ls.top() == i)
                self.ls.pop()
                self.assertTrue((self.ls.is_empty()))

            with self.assertRaises(Empty):
                self.ls.pop()


    class TestLinkedQueue(unittest.TestCase):
        """Test the Linked Queue class"""

        def setUp(self):
            self.lq = LinkedQueue()

        def tearDown(self):
            pass

        def test_empty_queue(self):
            """Test empty queue functions"""
            self.assertTrue(self.lq.is_empty())

            with self.assertRaises(Empty):
                self.lq.back()

            with self.assertRaises(Empty):
                self.lq.front()

        def test_enqueue(self):
            """Test adding elements to the end of the queue"""
            self.lq.enqueue(1)
            self.assertTrue(self.lq.front() == 1 and self.lq.back() == 1)

            for i in range(2, 11):
                self.lq.enqueue(i)
                self.assertTrue(self.lq.front() == 1 and self.lq.back() == i)

        def test_dequeue(self):
            """Test removing element from the front of the queue"""
            for i in range(1, 11):
                self.lq.enqueue(i)

            for i in range(1, 10):
                self.assertTrue(self.lq.front() == i)
                self.assertTrue(self.lq.dequeue() == i)
                self.assertTrue(self.lq.front() == i + 1)
                self.assertTrue(self.lq.back() == 10)

            self.assertTrue(self.lq.dequeue() == 10)

            with self.assertRaises(Empty):
                self.lq.dequeue()

    unittest.main()
