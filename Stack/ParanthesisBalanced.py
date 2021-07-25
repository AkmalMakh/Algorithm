# Complete the braces function below.
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

    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    for x in paren_string:
        while index < len(x) and is_balanced:
            paren = x[index]
            if paren in "([{":
                s.push(paren)
            else:
                if s.is_empty():
                    is_balanced = False
                else:
                    top = s.pop()
                    if not is_match(top, paren):
                        is_balanced = False
            index += 1

        n = s.is_empty()
        if n and is_balanced:
            return True
        else:
            return False


def braces(values):
    m = is_balanced(values)
    if m == True:
        return 'YES'
    else:
        return 'NO'


values = []
for x in range(2):
    values_item = input()
    values.append(values_item)

    res = braces(values)
    print(res)
