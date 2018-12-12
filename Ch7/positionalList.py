from doubleLinkedList import _DoublyLinkedBase
from doubleLinkedList import Empty


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other is a Position representing a different location"""
            return not (self == other)

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong in this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ----------------- accessors ----------------- #
    def first(self):
        """Return position of first element in the list"""
        return self._make_position(self._header._next)

    def last(self):
        """Return position of last element in the list"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return position of element before p"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return position of element after p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def find(self, e):
        """Return the first position of the element e"""
        curr = self.first()
        while curr is not None:
            if curr.element() == e:
                return curr
            curr = self.after(curr)
        return None

    def find_recursive(self, e, curr=None):
        if self.is_empty():
            return
        if not curr:
            curr = self.first()
        """Recursively return the first position of the element e"""
        if curr.element() == e:
            return curr
        if curr == self.last():
            return
        return self.find_recursive(e, self.after(curr))

    def __iter__(self):
        """Generate a forward iteration of the elements in the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Generate a backward iteration of the elements in the list"""
        cursor = self.last()
        while cursor is not self.first():
            yield cursor.element()
            cursor = self.before(cursor)

    # ----------------- mutators ----------------- #
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """"Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last_new(self, e):
        """Insert element e at the back of the list and return new Position"""
        if self.is_empty():
            return self.add_first(e)
        return self.add_after(self.last(), e)

    def add_before_new(self, p, e):
        """Insert element e at the beginning of the list and return new Position"""
        if self.is_empty():
            raise Empty("List is empty")
        return self.add_after(self.before(p), e)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p ,e):
        """Insert element e before Position p"""
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        """Remove and return the element at Position p"""
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """Replace the element at Position p with e"""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def max(self):
        """Return the maximum positional element in the Positional List L"""
        if self.is_empty():
            raise Empty("List is empty")

        maxvalue = 0
        value = self.first()
        while value is not None:
            if value.element() > maxvalue:
                maxvalue = value.element()
            value = self.after(value)
        return maxvalue


def insertion_sort(L):
    """Sort PositionalList of comparable elements"""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


def insertion_sort2(L):
    """Insertion Sort"""
    for i in range(1, len(L)):
        curr = L[i]
        j = i

        while j > 0 and L[j-1] > curr:
            L[j] = L[j-1]
            j -= 1
        L[j] = curr

def max(L):
    """Return the maximum positional element in the Positional List L"""
    if L.is_empty():
        raise Empty("List is empty")

    maxvalue = 0
    for e in L:
        if e > maxvalue:
            maxvalue = e
    return maxvalue


if __name__ == '__main__':
    import unittest

    class TestPositionalList(unittest.TestCase):

        def setUp(self):
            self.pl = PositionalList()

        def tearDown(self):
            self.pl = None

        def test_adding_nodes(self):
            for i in range(10):
                self.pl.add_first(i)
                self.assertTrue(self.pl.first().element() == i)

        def test_deleting_nodes(self):
            for i in range(10):
                self.pl.add_first(i)

        def test_find_recursive(self):
            #Empty list
            self.assertIsNone(self.pl.find_recursive(1))

            #Find first, last, and a middle element
            for i in range(1,10):
                self.pl.add_first(i)
            self.assertTrue(self.pl.find_recursive(2).element() == 2)
            self.assertTrue(self.pl.find_recursive(1).element() == 1)
            self.assertTrue(self.pl.find_recursive(9).element() == 9)

            #Add duplicate element, remove, find other
            self.pl.add_last(5)
            self.assertTrue(self.pl.before(self.pl.find_recursive(5)).element() == 6)
            self.pl.delete(self.pl.find_recursive(5))
            self.assertTrue(self.pl.before(self.pl.find_recursive(5)).element() == 1)

    unittest.main()






























