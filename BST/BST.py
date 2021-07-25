class Node:
    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
class BST:
    def __init__(self):    
        self.root=None

    def insert(self, value):
        if self.root == None:
            self.root =Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child =Node(value)
            else:
                self._insert(value, cur_node.left_child)    
        elif value>cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)  
        else:
            print( "Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)





def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree    

tree = BST()
tree = fill_tree(tree)
tree.print_tree()

print("Tree height is "+str(tree.height()))
