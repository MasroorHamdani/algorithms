class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    # Function to initialize head 
    def __init__(self, head=None): 
        self.head = head

    # This function prints contents of linked list 
    # starting from head 
    def print_list(self): 
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.next

    def insert_from_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append_on_end(self, data):
        new_node = Node(data)
        curr = self.head
        if self.head == None:
            self.head = new_node
        else:
            while (curr.next != None):
                curr = curr.next
            curr.next = new_node

    def find_element(self, data):
        curr = self.head
        while (curr and curr.data != data):
            curr = curr.next
        if curr:
            print(curr.data)
        else:
            print('None')

if __name__=='__main__': 
    # Start with the empty list 
    llist = LinkedList()
    # Insert from Head List
    llist.insert_from_head(1)
    llist.insert_from_head(2)
    llist.insert_from_head(3)
    llist.print_list()

    print('************')
    # Start with the empty list 
    llist2 = LinkedList()
    # Insert on End of List
    llist2.append_on_end(1)
    llist2.append_on_end(2)
    llist2.append_on_end(3)
    llist2.print_list()

    print('************')
    llist2.find_element(2)
    llist2.find_element(4)