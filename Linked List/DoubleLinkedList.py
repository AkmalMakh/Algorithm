class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def iterate(self):
        temp = self.head
        while temp:
            val = temp.data
            temp = temp.next
            yield val

    def length(self):
        count = 0
        if self.is_empty():
            return
        else:
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
            return count

    def is_empty(self):
        return self.head is None

    def add_node(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data, self.tail)
            self.tail = self.tail.next

    def insert_node(self, index, data):
        if self.is_empty():
            return
        else:
            if index >= self.length() or self.length() <= 0:
                print("out of range")
                return
            else:
                if index == self.length():
                    self.add_node(data)
                else:
                    temp = self.head
                    while index - 1:
                        temp = temp.next
                        index = index - 1
                    newData = Node(data)
                    temp.prev.next = newData
                    newData.prev = temp.prev
                    temp.prev = newData
                    newData.next = temp

    def deletion_index(self, index):
        if self.is_empty():
            print("List is empty")
        elif index >= self.length() or self.length() <= 0:
            print("Out of range")
        else:
            i = 1
            temp = self.head
            # deletion from head
            if index == i and temp.next is not None:
                self.head = temp.next
            while temp is not None and i < index:
                temp = temp.next
                index = index-1

            if temp is None:
                return

            if temp.next is not None:
                temp.next.prev = temp.prev
            if temp.prev is not None:
                temp.prev.next = temp.next


    def print_list(self):
        if self.is_empty():
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
            print("")

    def print_reverse(self):
        if self.is_empty():
            print("Empty")
        else:
            temp = self.tail
            while temp:
                print(temp.data)
                temp = temp.prev


a = Linkedlist()
a.add_node(1)
a.add_node(6)
a.add_node(3)
a.add_node(4)
a.add_node(2)
a.insert_node(2, 46)
a.print_list()
print("Length", a.length())
# print("_________ Reversed __________")
# a.print_reverse()
print("Deletion ")
a.deletion_index(2)
a.print_list()
