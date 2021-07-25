class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(sum_values(node2))
