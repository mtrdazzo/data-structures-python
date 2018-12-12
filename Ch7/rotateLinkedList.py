class LinkedList:
    class Node:
        __slots__ = "data", "next"

        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            retstr = str(self.data)
            curr = self

            while curr.next is not None:
                retstr += "->" + str(curr.next.data)
                curr = curr.next
            return retstr

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return ""
        retstr = str(self.head.data)
        curr = self.head

        while curr.next is not None:
            retstr += "->" + str(curr.next.data)
            curr = curr.next
        return retstr

    def add(self, e):
        new = self.Node(e)
        if self.head is None:
            self.head = new
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new

    def reverse_list(self):
        curr = self.head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverse_list_recursive(self, node):
        #Exit criteria
        if node.next is None:
            self.head = node
            return
        self.reverse_list_recursive(node.next)
        node.next.next = node
        node.next = None


def rotate(head, k):
    if head is None:
        return

    prev = head
    curr = head.next

    while (k - 1) and curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        k -= 1

    head.next = rotate(curr, k)

    return prev


def rotate_non_recursive(ll, k):
    if ll.head is None:
        return

    k0 = k
    prev = ll.head
    curr = ll.head.next
    ll.head = None
    prev_first = None

    while curr is not None and k0 > 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        k0 -= 1
    prev.next = cur

    if ll.head is None:
        ll.head = prev

def rotate_ll(ll, k):
    if ll.head is None:
        return
    if k < 1:
        return
    pivot = q = ll.head

    while pivot.next is not None and k > 1:
        pivot = pivot.next
        k -= 1

    if pivot.next is None and k >= 1:
        raise ValueError("Not enough indexes")

    old_head = ll.head
    ll.head = pivot.next
    pivot.next = None

    curr = ll.head
    while curr.next is not None:
        curr = curr.next
    curr.next = old_head






# rotate_non_recursive(ll, 3)
for i in range(0, 11):
    ll = LinkedList()
    for j in range(10):
        ll.add(j)
    rotate_ll(ll, i)
    print(i)
    print(ll)
