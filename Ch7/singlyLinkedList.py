class Empty(Exception):
    pass


class linkedStack:
    """Complete implementation of the stack ADT using a singly linked list that includes
       a header sentinel.
    """
    class _Node:
        """Lightweight Node class"""
        __slots__ = '_data', '_next'

        def __init__(self, data):
            """Instantiate an empty node"""
            self._data = data
            self._next = None

    def __init__(self):
        """Create an empty linked list stack ADT"""
        self._header = self._Node(None)
        self._size = 0

    def __len__(self):
        """Return the number of elements inside the linked list stack"""
        return self._size

    def __str__(self):
        """Print the linked list stack"""
        if self.is_empty():
            return ""
        current = self._header._next
        retstr = str(current._data)
        while current._next is not None:
            retstr += "->" + str(current._next._data)
            current = current._next
        return retstr

    def is_empty(self):
        """Return True if there are no elments in the linked list stack"""
        return self._size == 0

    def push(self, e):
        """Push an element e to the top of the stack"""
        new = self._Node(e)
        if not self.is_empty():
            new._next = self._header._next
        self._header._next = new
        self._size += 1

    def pop(self):
        """Pop an element off the top of the stack"""
        if self.is_empty():
            raise Empty
        e = self._header._next
        self._size -= 1

        if self.is_empty():
            self._header._next = None
        else:
            self._header._next = e._next
        e._next = None
        return e._data

    def first(self):
        """Return (but do not remove) the first element in the linked list"""
        if self.is_empty():
            raise Empty("List is empty")
        return self._header._next._data


class linkedQueue:
    """A FILO queue using a linked list data structure that includes a header sentinel"""
    class _Node:
        """Non-public lightweight Node class"""
        __slots__ = '_data', '_next'

        def __init__(self, data, next=None):
            """Create an empty Node"""
            self._data = data
            self._next = next

    def __init__(self):
        """Create an empty linked list queue"""
        self._trailer = None
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        """Return the number of element in the linked queue"""
        return self._size

    def __str__(self):
        """Print the linked list queue"""
        if self.is_empty():
            return ""
        curr = self._header._next
        retstr = str(curr._data)

        while curr._next is not None:
            retstr += "->" + str(curr._next._data)
            curr = curr._next
        return retstr

    def is_empty(self):
        """Return True if no elements exist inside the linked queue ADT"""
        return len(self) == 0

    def enqueue(self, e):
        """Add element e to the back of the queue"""
        new = self._Node(e, None)
        if self.is_empty():
            self._header._next = new
        else:
            self._trailer._next = new
        self._trailer = new
        self._size += 1

    def dequeue(self):
        """Return element e from the front of the queue"""
        if self.is_empty():
            raise Empty("List is empty")
        e = self._header._next
        self._size -= 1
        self._header._next = e._next

        if self._size == 1:
            self._trailer = None

        e._next = None
        return e._data

    def first(self):
        """Return (but do not remove) the first element in the queue"""
        if self.is_empty():
            raise Empty("List is empty")
        return self._header._next._data

    def last(self):
        """Return (but do not remove) the last element in the queue"""
        if self.is_empty():
            raise Empty("List is empty")
        return self._trailer._data

    def concatenate(self, Q2):
        """Concatenate Qt in O(1) time where Q2 is now an empty Queue"""
        if Q2.is_empty():
            return
        self._trailer._next = Q2._header._next
        self._trailer = Q2._trailer
        self._size += len(Q2)
        Q2._header._next = None
        Q2._trailer = None
        Q2._size -= len(Q2)


# if __name__ == '__main__':
#     import unittest
#
#     class testLinkedQueue(unittest.TestCase):
#         def setUp(self):
#             self.lq = linkedQueue()
#
#         def tearDown(self):
#             self.lq = None
#
#         def test_concatenate(self):
#             lq2 = linkedQueue()
#             lq3 = linkedQueue()
#             for i in range(10):
#                 self.lq.enqueue(i)
#                 lq2.enqueue(i)
#             self.lq.concatenate(lq2)
#             self.lq.concatenate(lq3)
#
#         def test_empty_queue(self):
#             with self.assertRaises(Empty):
#                 self.lq.dequeue()
#
#             with self.assertRaises(Empty):
#                 self.lq.first()
#
#             with self.assertRaises(Empty):
#                 self.lq.last()
#
#         def test_enqueue(self):
#             self.lq.enqueue(1)
#             self.assertTrue(self.lq.first() == 1 and self.lq.last() == 1)
#
#             for i in range(10):
#                 self.lq.enqueue(i)
#                 self.assertTrue(self.lq.last() == i)
#
#             self.assertTrue(len(self.lq) == 11)
#
#         def test_dequeue(self):
#             for i in range(10):
#                 self.lq.enqueue(i)
#                 self.assertTrue(self.lq.last() == i)
#
#             for i in range(10):
#                 num = self.lq.dequeue()
#                 self.assertTrue(num == i)
#             self.assertTrue(self.lq.is_empty())
#
#     class testSingleLinkedList(unittest.TestCase):
#
#         def setUp(self):
#             self.ll = linkedStack()
#
#         def testEmptyStack(self):
#             with self.assertRaises(Empty):
#                 self.ll.pop()
#
#             with self.assertRaises(Empty):
#                 self.ll.first()
#
#             self.assertTrue(self.ll.is_empty())
#
#         def testSingleElementStack(self):
#             self.ll.push(1)
#             self.assertFalse(self.ll.is_empty())
#             self.assertTrue(self.ll.first() == 1)
#             self.assertTrue(self.ll.pop() == 1)
#
#         def testMultipleElementsStack(self):
#             for i in range(5):
#                 self.ll.push(i)
#                 self.assertTrue(self.ll.first() == i)
#             self.assertTrue(len(self.ll) == 5)
#             for i in range(5):
#                 self.ll.pop()
#             self.assertTrue(self.ll.is_empty())
#
