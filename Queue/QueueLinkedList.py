class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # mean add new node in the end of list
    def enqueue(self, new_data):
        # init new node
        new_node = Node(new_data)
        # check if the node is empty
        if self.is_Empty():
            self.head = self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node

    # delete from head of list
    def dequeue(self):
        if self.is_Empty():
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def is_Empty(self):
        return self.head is None and True or False

    def show_front(self):
        return self.head.data

    def show_rear(self):
        return self.tail.data

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


queue = Queue()
print(queue.is_Empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(30)
print("rear : ", queue.show_rear())
print("front : ", queue.show_front())
queue.print()
