class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, new_data):
        self.data.append(new_data)

    def dequeue(self):
        return self.data.pop(0)

    def is_Empty(self):
        return len(self.data) <= 0 and True or False

    def show_front(self):
        return self.data[0]

    def show_rear(self):
        return self.data[len(self.data)-1]

    def print(self):
        print(self.data)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.show_rear())
print(queue.show_front())
queue.print()
