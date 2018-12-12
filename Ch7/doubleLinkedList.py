class Empty(Exception):
    pass


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        """Lightweight, nonpublic class for storing a doubly linked node."""
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty doubly linked list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __str__(self):
        if self.is_empty():
            return ""

        curr = self._header._next
        retstr = str(curr._element)

        while curr._next is not self._trailer:
            retstr += "->" + str(curr._next._element)
            curr = curr._next

        return retstr

    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Insert e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""

        if self.is_empty():
            raise Empty("List is empty!")

        predecessor = node._prev
        successor = node._next

        predecessor._next = successor
        successor._prev = predecessor

        elem = node._element
        node._prev = node._next = node._element = None

        self._size -= 1

        return elem


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list"""

    def __add__(self, other):
        if not isinstance(other, LinkedDeque):
            raise TypeError("Not a doubly linked list")

        new = LinkedDeque()
        if self.is_empty() and other.is_empty():
            return new

        currA = self._trailer._prev
        currB = other._header._next

        while currA != self._header:
            new.insert_first(currA._element)
            currA = currA._prev

        while currB != other._trailer:
            new.insert_last(currB._element)
            currB = currB._next

        return new

    def first(self):
        """Return (but do not delete) the first element in the deque"""
        if self.is_empty():
            raise Empty("List is empty!")
        return self._header._next._element

    def last(self):
        """Return (but do not delete) the last element in the deque"""
        if self.is_empty():
            raise Emtpy("List is empty!")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Insert e into the front of the list"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Insert e at the back of the list"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Delete and return the element from the front of the queue"""
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Delete and return the elemetn at the back of the queue"""
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self.trailer._prev)

    def swap_nodes(self, a, b):
        """Swap nodes a and b"""
        if a == b:
            return
        if len(self) < 2:
            return

        nodeA = nodeB = None
        curr_node = self._header

        while curr_node is not None and not (nodeA and nodeB):
            if curr_node._element == a and not nodeA:
                nodeA = curr_node
            elif curr_node._element == b and not nodeB:
                nodeB = curr_node
            curr_node = curr_node._next

        if curr_node is None:
            raise Empty("Not in list")

        precessorA = nodeA._prev
        successorA = nodeA._next
        precessorB = nodeB._prev
        successorB = nodeB._next

        precessorA._next = successorA._prev = nodeB
        precessorB._next = successorB._prev = nodeA

        nodeA._prev, nodeB._prev = nodeB._prev, nodeA._prev
        nodeA._next, nodeB._next = nodeB._next, nodeA._next

    def link_hopping(self):
        """Find the center node by link hopping

        EX: 1->2->3->4->5, return 3
            1->2->3->4, return 2

        """

        if self.is_empty():
            raise Empty("List is empty")

        fast = slow = self._header

        while fast is not None:
            fast = fast._next
            if fast is not None and fast != self._trailer:
                fast = fast._next
                slow = slow._next
        return slow._element


if __name__ == '__main__':
    import unittest

    class TestDLL(unittest.TestCase):
        def setUp(self):
            self.dll = LinkedDeque()

        def test_add_lls(self):

            dll2 = LinkedDeque()
            dll3 = self.dll + dll2
            self.assertTrue(dll3.is_empty())

            for i in range(10):
                self.dll.insert_first(i)
            dll3 = self.dll + dll2
            self.assertTrue(dll3.first() == 9 and dll3.last() == 0)
            dll3 = dll2 + self.dll
            self.assertTrue(dll3.first() == 9 and dll3.last() == 0)

            for i in range(5):
                dll2.insert_first(i)
            dll3 = self.dll + dll2

            self.assertTrue(dll3.first() == 9 and dll3.last() == 0)


        def test_find_middle(self):
            with self.assertRaises(Empty):
                self.dll.link_hopping()
            self.dll.insert_first(1)
            self.assertTrue(self.dll.link_hopping() == 1)
            self.dll.insert_first(2)
            self.assertTrue(self.dll.link_hopping() == 2)
            self.dll.insert_first(3)
            self.assertTrue(self.dll.link_hopping() == 2)

        def test_add_node(self):
            self.dll.insert_first(10)
            self.assertTrue(self.dll.first() == 10)
            self.assertTrue(self.dll.last() == 10)

            self.dll.insert_first(5)
            self.assertTrue(self.dll.first() == 5)
            self.assertTrue(self.dll.last() == 10)

        def test_swap_nodes(self):
            self.assertIsNone(self.dll.swap_nodes(1, 3))
            self.dll.insert_first(10)
            self.assertIsNone(self.dll.swap_nodes(1 , 10))
            self.dll.insert_last(5)
            self.assertIsNone(self.dll.swap_nodes(5, 5))

            self.dll.insert_first(3)
            self.dll.swap_nodes(3, 5)

            self.assertTrue(self.dll.first() == 5)
            self.assertTrue(self.dll.last() == 3)

    unittest.main()