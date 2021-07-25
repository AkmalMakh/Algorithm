class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.current = self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            self.head.prev = newnode
            newnode.next = self.head
            newnode.prev = None
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def forward(self):
        if self.is_empty():
            return None
        else:

            if self.head.next is not None:
                self.head = self.head.next
                return self.head.data

    def backward(self):
        if self.is_empty():
            return None
        else:

            if self.head is not None:
                self.head = self.head.prev
                return self.head.data
            else:
                print("invalid")
    def display(self):

        iternode = self.head
        if self.is_empty():
            print("Stack Underflow")

        else:
            while iternode is not None:
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return


MyStack = Stack()

MyStack.push("Google")
MyStack.push("Youtube")
MyStack.push("Amazon")
MyStack.push("Netflix")

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())

print("\nforward :", MyStack.forward())
print("\nbackword :", MyStack.backward())

print("\nforward :", MyStack.forward())
print("\nbackword :", MyStack.backward())

print("\nforward :", MyStack.forward())

print("\nbackword :", MyStack.backward())
print("\nbackword :", MyStack.backward())