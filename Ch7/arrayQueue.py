class Empty(Exception):
    pass


import collections

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue of size DEFAULT_CAPACITY"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._data = collections.deque(list(), ArrayQueue.DEFAULT_CAPACITY)
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def __str__(self):
        """Print the queue"""
        return str(self._data)

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._data[self._front]

    # def dequeue(self):
    #     """Return the first element off the front of the queue"""
    #     if self.is_empty():
    #         raise Empty("Queue is empty!")
    #     elem = self._data[self._front]
    #     self._data[self._front] = None
    #     self._front = (self._front + 1) % len(self._data)
    #     self._size -= 1
    #
    #     return elem

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        self._size -= 1
        return self._data.popleft()

    # def enqueue(self, e):
    #     """Add an element e to the end of the queue"""
    #     if (self._front + self._size) == len(self._data):
    #         self._resize(2 * len(self._data))
    #     next_avail = self._front + self._size
    #     self._data[next_avail] = e
    #     self._size += 1

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def _resize(self, size):
        """Resize list to length size"""
        old = self._data
        self._data = [None] * size
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[k]
            walk = (1 + walk) % len(old)
        self._front = 0


if __name__ == '__main__':
    import unittest

    class testArrayQueue(unittest.TestCase):
        def setUp(self):
            self.q = ArrayQueue()

        def tearDown(self):
            pass

        def test_empty_queue(self):
            self.assertTrue(self.q.is_empty(), "Queue is empty")

            with self.assertRaises(Empty):
                self.q.dequeue()

        def test_resize(self):
            for i in range(10):
                self.q.enqueue(i)
            self.q.enqueue(10)
            self.q.dequeue()
            self.assertTrue(len(self.q) == 10)
            print(self.q)

    # unittest.main()
