class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self, root, name=''):
        self.root=root
        self.name=name
        

node = Node(10)

node.left_child = Node(7)
node.right_child= Node(15)

# left childs of node tree
node.left_child.left_child = Node(5)
node.left_child.right_child= Node(8)

# right childs of node tree
node.right_child.left_child= Node(11)
node.right_child.right_child= Node(17)

# printing data 
print(node.right_child.data)
print(node.left_child.data)

myTree = Tree(node,'Akmal\'s tree')
