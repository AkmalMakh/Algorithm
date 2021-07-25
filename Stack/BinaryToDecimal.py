# Use a stack data structure to convert integer values to binary

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
        

def decimalToBinary(decimal):
    s = Stack();
    while decimal > 0:
        fraction = decimal%2
        s.push(fraction)
        decimal = decimal // 2
    bin_num =""
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num


print(decimalToBinary(101))