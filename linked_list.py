class node:
    def __init__(self,item):
        self.data= item
        self.next= None 
        
class linked_list:
    def __init__(self):
        self.head=None
        self.n=0
        
    def __len__(self):
        return self.n
        
    def insert_head(self,item):
        new_node=node(item)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
        
    def __str__(self):
        result=''
        current= self.head
        while current !=None:
           result=result+ str(current.data) +'->'
           current= current.next
        return result[:-2]
        
    def append(self,item):
        new_node=node(item)
        if self.head== None :
            self.head=new_node
            return
        current=self.head
        while current.next!=None:
            current= current.next
        current.next=new_node
        self.n+=1
        
    def insert_after(self,after,item):
        new_node=node(item)
        current=self.head
        while current!=None:
            if current.data==after:
                break
            current=current.next
        if current==None:
            return 'item not found'
        else :
            new_node.next=current.next
            current.next=new_node
            self.n+=1
            
    def delet_head(self):
        if self.head == None:
            print('no elements in linked list')
            return
        self.head= self.head.next
        self.n-=1
    
    def pop(self):
        current= self.head
        if current== None:
            print("there no elements in linkedlist")
            return 
        if current.next==None:
            self.head=None
            self.n -=1
            return 
        while current.next.next!=None:
            current=current.next
        current.next=None
        self.n -=1
    def delet(self,item):
        current= self.head
        if current==None:
            print('trere no elements in linkedlist')
            return
        if current.data==item:
            self.delet_head()
            return
        while current.next.next!=None:
            if current.next.data==item:
                break
            current=current.next
        if current.next.data==item:
            if current.next.next==None:
                self.pop()
                return
        if current.next.next==None:
            print('item not found')
            return
        current.next=current.next.next
        self.n-=1
    
    def find(self,item):
        curent=self.head
        pos=0
        while curent !=None:
            if curent.data==item:
                break
            curent=curent.next
            pos+=1
        if curent==None:
            print('item not found')
            return
        return pos


ll=linked_list()
ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_head(40)
ll.append(100)
ll.insert_after(10,200)
print(ll)
print(len(ll))
#ll.pop()
#ll.pop()
#ll.pop()
#ll.pop()
#ll.pop()
#ll.delet(40)
#ll.delet(30)
#ll.delet(200)
#ll.delet(100)
#ll.delet(20)
#ll.delet(40)
#ll.delet(10)
print(ll.find(0))


#ll.delet(100)



#print(ll)
#ll.delet_head()
#ll.delet_head()
#ll.delet_head()
#ll.delet_head()
#ll.delet_head()
#print(ll)

#print(len(ll))