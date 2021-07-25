# "Use a stack to check wheather or not a string has balanced usage of paranthesis "
# " Example "
#  (), ()()   ({[]}) <- balanced
#  ((), {{{)}}, [][]]] <- not Balanced

# Balanced Example: {[]}

# Non-Balanced Example: (()

# Non-Balanced Example:))

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
        



def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False


def is_parem_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:


