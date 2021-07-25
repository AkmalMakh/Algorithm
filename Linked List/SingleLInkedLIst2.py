class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,data):

        new_Node = Node(data)
        if self.head is None:
            self.head = self.tail = new_Node;
        else:
            self.tail.next = new_Node
            self.tail = new_Node

    def print_list(self):
        temp = self.head
        while temp:
            print("My list data is ",temp.data)
            temp = temp.next


    def length(self):
        temp = self.head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        return count
    
    def delete_begining(self):
        
        if self.head is not None:
            print("I am deleting data : ",self.head.data)
            self.head = self.head.next
    
    def delete_end(self):
        if self.head is not None:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
                
            self.tail = temp
            temp.next = None
                
    def delete_at_index(self, index):
        if self.head is not None:
            if index > self.length() and index<0:
                print("Out of list")
                return
            if index is 1:
                self.delete_begining()
                return
            
            temp = self.head;
    
            while index-2 and index>0:
                temp = temp.next
                index -=1 
                
            if index is self.length:
                self.delete_end()
                return

            if temp.next.next is not None:
                temp.next = temp.next.next
            else:
                temp.next=None        
    def get_at_index(self, index):
        temp = self.head
        while index-1:
            temp = temp.next
            index -=1
        return temp;    
    def length_between(self,left_node, right_node):
        temp = left_node
        stop = right_node
        count = 1;
        while temp is not stop:
            count +=1
            temp = temp.next
            
        return count
    def is_empty(self): 
        return self.head is None

    def get(self, index):
        if self.is_empty():
            return -1
        if index > self.length() or index < 0:
            return -1
        elif index == 0:
            return self.head.data
        elif index == self.length():
            return self.tail.data
        else:
            temp = self.head
            while index:
                temp=temp.next
                index -=1
            return temp.data

    def reverseBetween(self, left, right):
        left_node = self.get_at_index(left)
        right_node = self.get_at_index(right)
        middle = (self.length_between(left_node, right_node)/2)
        if left is right:
            return  
        print(self.length_between(left_node, right_node))    
        if self.length_between(left_node, right_node) is 1:
            left_node.data, right_node.data = right_node.data, left_node.data
            return
        count = 0
        while count < middle:
        
            left_node.data, right_node.data = right_node.data, left_node.data
            left_node = left_node.next
            right -=1
            right_node = self.get_at_index(right)
            count +=1
            
        return
            
        



        

list = LinkedList()

# [4,-2,-4,0,-2,-2,-1,-2]

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)


list.print_list()
list.delete_at_index(8)
print("After Deletion")
list.print_list()
# print(list.get(12))
# list.reverseBetween(2,5)
# print("After reverse")
# list.print_list()

