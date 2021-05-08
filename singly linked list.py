class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link
class LinkedList:
    def __init__(self,head = None):
        self.head = head
    def Check_is_empty(self):
        if self.head is None:
            print("LL is Empty")
        else:
            print("LL is not empty")
            while self.head != None:
                print(self.head.data,end="---->")
                #print(self.head.link)
                self.head = self.head.link
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node2 = Node(data)
        if self.head is None:
            self.head = new_node2
        else:
            while self.head.link != None:
                self.head = self.head.link
            self.head.link = new_node2

    def add_between(self,data):
        new_node3 = Node(data)
        new_node3.link = self.head
        self.head = new_node3
    
    def del_begin(self):
        self.head = self.head.link
    
    def del_end(self):
        if self.head is None:
            print("LL is empty u cant remove any nodes")
        else:
            n = self.head
            while n.link.link != None:
                n = n.link
            n.link = None
                
    def del_by_value(self,x):
        if self.head.data == x:
             return L1.del_begin()
        else:
            n=self.head
            
            """while n.data!=y:
                n = n.link
            n.link = n.link.link"""
            
            while n.link.data != x:
                n = n.link
        n.link = n.link.link
                    
            
#n1 = Node(10,1011)
#print(n1)
L1=LinkedList()
L1.add_begin(10)
L1.add_end(40)
L1.add_between(50)
L1.add_begin(20)
L1.add_between(60)
L1.add_begin(30)
#L1.del_begin()
#L1. del_end()
L1.del_by_value(20)
L1.Check_is_empty()

