# create a class on here and  that class main purpose is cretae node 
class Node:
    def __init__(self,value): #define a constructor of class 
        # these are instance variable
        self.value = value
        self.next = None

# create a class on here with instance methods and that class main purpose is performs operations on node 
class OpeartionsNode:
    def __init__(self): #define a constructor of class 
        # these are instance variable
        self.head = None
    
    # define a instance method with required arguments after checking conditions return some value to called place
    def create_node(self,value,position):
        if type(value) ==int:
            if position == -1 :
                create_new_node = Node(value)  # create a object to the Node class assign to a reference variable
                # if node is empty
                if self.head is None:
                    self.head = create_new_node # create node assign to head
                    return value

                temp = self.head # main head node assign to a variable
                # if the head Node is not empty then while condition is exists
                while True:
                    if temp.next is None:
                        temp.next = create_new_node
                        return value
                    temp = temp.next    
            elif position == 0:
                # define a instance method with required arguments after checking conditions return some value to called place
                # def create_node_first(self,value):
                create_new_node = Node(value) # create a object to the Node class assign to a reference variable
                if self.head is not None:
                    self.head.prev = create_new_node # create node assign to head
                    create_new_node.next = self.head # create node next assign a head_node
                    create_new_node.prev = None # create node previous node makes None

                self.head =  create_new_node # create node assign to head
                return value
            else:
                return (" you can assign the 0 or -1th position ")
        else:
            print(" This Application is Developing for integers only ")
            return False             

    # define a instance method with required arguments after checking conditions return some value to called place
    def delete_node(self,position):
        if position == -1:
            # If node is empty
            if self.head is None:
                print(" nodes are not on here for delete puropse ")
                return ("No nodes are delete purpose")
            
            temp = self.head # main head node assign to a variable
            if temp is None:
                temp = None
                return ("No nodes are delete purpose")

            temp = self.head
            # temp1 = temp.next
            # if the head Node is not empty then while condition is exists 
            while True: 
                if temp.next.next is None:
                    temp.next = None
                    return True
                temp = temp.next
            return True
            
        elif position == 0:
            # define a instance method with required arguments after checking conditions return some value to called place
            # def delete_node_first(self,position):
            # If node is empty
            if self.head is None:
                print(" nodes are not on here for delete purpose ")
                return ("No nodes are delete purpose")
            else: # if the head Node is not empty then else condition is exists
                temp = self.head # main head node assign to a variable
                self.head = self.head.next
                temp = None
                return True 
        else:
            return None          


    # Define a instance method with required arguments after checking conditions return some value to called place
    def display_node(self):
        l1 = []
        # If node is empty
        if self.head is None:
            print("still we don't have any nodes yet ")
            return ("we don't have any nodes yet for Display Purpose")
        temp = self.head # main head node assign to a variable
        # If the head Node is not empty then while condition is exists
        while True:
            if temp is None:
                print("None")
                return l1
            else:
                print(temp.value,end="===>") # display the values are linked list format
                l1.append(temp.value)
                temp = temp.next


# create a objects on here wrt to class and call the methods wrt to refrence objects
# o = OpeartionsNode()  
# o.create_node(5,-1)
# o.create_node(4,0)
# o.create_node(3,0)
# o.create_node(2,0)
# o.create_node(1,0)
# o.create_node(6,-1)
# o.display_node()
# o.delete_node(-1)
# o.display_node()
# o.delete_node(0)
# o.display_node()