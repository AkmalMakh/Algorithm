class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = self.tail = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.tail
    
        # 6. Change the next of last node
        last.next =  new_node

        self.tail = last.next
        
        
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def printRecursively(self,head):
        
        if head:
            self.printRecursively(head.next)
            print(head.data)
        else:
            return
            
    def deletion(self, data):
        # if node is empty
        if self.head == None:
            return
        # deletion from head
        temp = self.head
        if temp.data == data:
            self.head = self.head.next
            return
        
        # deletion from middle 
        temp = self.head.next
        prev = self.head
        while temp.data != data:
            temp = temp.next
            prev = prev.next
        prev.next = temp.next

    def length_list(self):
        temp = self.head
        count = 0;
        while temp:
            count+=1
            temp=temp.next
        return count    

    def delete_at_index(self, index):
        if self.head == None:
            return
        if index > self.length_list() and index<0:
            print("Given index out of range")
            return
        if index == 1:
            self.head = self.head.next
            return
        temp = self.head
        count = index-2
        while count and index>0:
            temp = temp.next
            count -=1    
        if index == self.length_list():
            temp.next = None
            self.tail = temp
            return
        if temp.next.next is not None:
            temp.next = temp.next.next
    def reverse_between(self, left, right):

        
        
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    llist.append(6)
    llist.append(4)
    llist.append(3)
    llist.append(2)

    
    llist.printList()

    llist.delete_at_index(4)
    print("after deletion")
    llist.printList()
    # print("Reversed order print ")
    # llist.printRecursively(llist.head)
