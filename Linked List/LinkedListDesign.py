class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.prev = None
    
        
class MyLinkedList:

    def __init__(self):
       self.head = self.tail = None
        

    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count +=1
        return count
    
    def is_empty(self): 
        return self.head is None
        
    def get(self, index: int) -> int:
        
        if self.is_empty():
            return -1
        if index > self.get_length() or index < 0:
            return -1
        elif index == 0:
            return self.head
        elif index == self.get_length():
            return self.tail.val
        else:
            temp = self.head
            while index:
                temp=temp.next
                index -=1
            return temp.val    
    def get_node(self, index: int):
        
        if self.is_empty():
            return -1
        if index > self.get_length() or index < 0:
            return -1
        elif index == 0:
            return self.head
        elif index == self.get_length():
            return self.tail
        else:
            temp = self.head
            while index:
                temp=temp.next
                index -=1
            return temp    

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next =self.head;
            self.head = new_node    
       
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node;
        else:
            self.tail.next = new_node
            self.tail = self.tail.next   
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp= temp.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        if self.get_length() < index or index < 0:
            return -1
        elif self.get_length() == index:
            self.addAtTail(val)
        elif index is 0:
            self.addAtHead(val)
        else:
            prev_node = self.get_node(index-1)
            current_node = prev_node.next
            new_node.next = current_node
            prev_node.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.get_length() < index or index < 0:
            return
        elif index == 0:
            self.head = self.head.next;    
        elif index == self.get_length():
            prev_node = self.get_node(index-1)
            self.tail = prev_node
        else:
            prev_node = self.get_node(index-1)
            prev_node.next = prev_node.next.next



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtTail(1)
obj.addAtTail(0)
obj.print()
obj.addAtIndex(3,99);
print("After index")
obj.print()

obj.deleteAtIndex(3)
print("After Del")
obj.print()

# param_1 = obj.get(4)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)