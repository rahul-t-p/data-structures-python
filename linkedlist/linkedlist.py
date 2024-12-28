class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes_data=None):
        self.head = None
        if isinstance(nodes_data, list):
            for data in nodes_data[::-1]:
                self.add_first(data)
        
    def add_first(self, data):
        ptr = self.head
        self.head = Node(data)
        self.head.next = ptr

    def add_last(self, data):
        ptr = self.head
        if ptr is None: return self.add_first(data)
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(data)

    def insert_before(self, target_data, data):
        ptr = self.head
        if ptr.data == target_data: return self.add_first(data)
        while ptr.next is not None:
            if (ptr.next.data == target_data):
                node = Node(data)
                node.next = ptr.next
                ptr.next = node
                return
            ptr = ptr.next
        raise Exception("Target data {} not found !".format(target_data))

    def insert_after(self, target_data, data):
        ptr = self.head
        while ptr is not None:
            if ptr.data == target_data:
                node = Node(data)
                node.next = ptr.next
                ptr.next = node
                return
            ptr = ptr.next
        raise Exception("Target data {} not found !".format(target_data))

    def del_first(self):
        self.head = self.head.next

    def del_last(self):
        ptr = self.head
        if ptr.next is None: self.head = None; return
        while ptr.next is not None:
            if (ptr.next.next) is None: break
            ptr = ptr.next
        ptr.next = None

    def del_data(self, target_data):
        ptr = self.head
        if ptr.data == target_data: return self.del_first()
        while ptr is not None:
            if ptr.next.data == target_data:
                ptr.next = ptr.next.next
                return
            ptr = ptr.next
        
    def __iter__(self):
        ptr = self.head
        while ptr is not None:
            yield ptr.data
            ptr = ptr.next
        
    def __repr__(self):
        return '->'.join(map(str, self))

ll = LinkedList(nodes_data=[1, 3])
ll.add_first(5)
ll.add_last(8)
ll.del_first()
ll.del_last()
ll.insert_before(3, 2)
ll.insert_before(1, 0)
ll.del_data(2)
ll.insert_after(1, 5)