class Link:
    def __init__(self,value):
        self.data=value
        self.next=None
        
def print_ll(head):
    temp=head
    while(temp!=None):
        print(temp.data,end="-->")
        temp=temp.next
            
    print("None")
    return
    
def Input_ll():
    value=int(input("Enter the node value"))
    head=None
    while(value!=-1):
        new=Link(value)
        if(head==None):
           head=new
        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new
                
        value=int(input("Enter the node"))
    return head
    
new_head=Input_ll()
print(new_head)