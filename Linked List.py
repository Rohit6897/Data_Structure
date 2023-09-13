class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        
        elif self.head==self.tail:
            self.tail=new_node
            self.head.next=self.tail

        else:
            temp=self.tail
            self.tail=new_node
            temp.next=self.tail
        self.length+=1
        return True
    
    def 
    
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next

my_linked_list=Linked_List()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(33)
my_linked_list.print_list()
