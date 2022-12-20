data = open('input/day20_small.txt').read().splitlines()
# data= open('input/day20.txt').read().splitlines()
data = [int(d) for d in data]


# %% Build a circular linked list which can move its node to left or right
class Node:
    def __init__(self, data, id):
        self.data = data
        self.next = None
        self.prev = None
        self.id = id

    def __repr__(self):
        return f'Node({self.data})'

    def __str__(self):
        return f'Node({self.data})'


class CircularLinkedList:
    def __init__(self):
        self.head = None
        size = 0

    def add_node(self, data_, id_):
        new_node = Node(data_, id_)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            self.size = 1
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node
            self.size += 1

    def move_node_right(self, node, steps):
        """

        :param node:
        :param steps:
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        # move the
        for i in range(steps):
            node.next = node.next.next

        node.prev = node.next.prev
        node.next.prev = node
        node.prev.next = node

    def move_node_left(self, node, steps):
        node.next.prev = node.prev
        node.prev.next = node.next
        for i in range(steps):
            node.prev = node.prev.prev
        node.next = node.prev.next
        node.prev.next = node
        node.next.prev = node

    def find_node_with_id(self, id_):
        current = self.head
        for i in range(self.size):
            if current.id == id_:
                return current
            current = current.next
        return None

    def __repr__(self):
        current = self.head
        l = []
        for i_ in range(self.size):
            l.append(current.data)
            current = current.next

        return str(l)

#%%
# Part 1
# Build a circular linked list
c = CircularLinkedList()
for i, d in enumerate(data):
    c.add_node(d, i)
#%%
#%%
