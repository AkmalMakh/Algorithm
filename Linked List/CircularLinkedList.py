class Node:
     
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def push(self, data):
        
        # 1 creating new node 
        new_node = Node(data)
        temp = self.head
        
        
        # 2 Linking new node next to head 
        new_node.next = self.head
        
        
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node    
        else:
            # if it is first node link them 
            new_node.next = new_node 
        
        
        # 3 Moving head back to new node 
        self.head = new_node
        
    def printList(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
                
# Initialize list as empty
cllist = CircularLinkedList()
 
# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)
 
print( "Contents of circular Linked List")
cllist.printList()
        