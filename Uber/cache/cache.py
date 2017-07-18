#
# Implementing Cache using LRU replacement algorithm
#
class node:
    def __init__(self, location):
        self.location = location
        self.drivers = []
        self.prev = None
        self.next = None


class DLL:
    head = None
    tail = None

    # Inserts at the end of the Linked List
    def insertEnd(self, newnode):
        if self.head is None:
            self.head = newnode
            self.tail = self.head
            return
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    # Removes the head of the Linked List
    def removeFront(self):
        if self.head is None:
            return None
        t = self.head
        p = self.head.next
        self.head.next = None
        if p:
            p.prev = None
        self.head = p
        return t

    # Removes the current node and inserts it at the end
    def adjust(self, n):
        if n is None or n == self.tail:
            return
        if n == self.head:
            t = self.removeFront()
            self.insertEnd(t)
            return
        # node is neither head nor tail
        p, t = n.prev, n.next
        n.prev, n.next = None, None
        if p:
            p.next = t
        if t:
            t.prev = p
        self.insertEnd(n)

    def display(self):
        curr = self.head
        while curr is not None:
            print curr.data,
            curr = curr.next
        print


class Cache:
    def __init__(self, maxsize, dll):
        self.currsize = 0
        # maxsize of cache
        self.maxsize = maxsize
        self.dll = dll
        self.hmap = {}

    def set(self, location, driver):
        if location in self.hmap:
            node = hmap[location]
            node.drivers.append(driver)
            self.dll.adjust(node)
            return

        newnode = node(location)
        newnode.drivers.append(driver)
        if self.currsize >= self.maxsize:
            t = self.dll.removeFront()
            self.hmap.pop(t.location)
            self.currsize -= 1

        self.dll.insertEnd(newnode)
        self.hmap[location] = newnode
        self.currsize += 1

    def get(self, location):
        if location not in self.hmap:
            return None
        return self.hmap[location].drivers