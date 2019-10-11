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

    def get_head_element(self):
        return self.head

    # This function prints contents of linked list 
    # starting from head 
    def print_list(self): 
        temp = self.head 
        while (temp): 
            print temp.data,
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

    def reverse_list(self):
        curr = self.head
        next_node = None
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        self.print_list()

    def remove(self, data):
        curr = self.head
        prev = None
        while (curr and curr.data != data):
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            # Free the curr link node

    def delete_with_location_pointer(self, node):
        if(node == None):
            return
        else:
            if(node.next):
                node.data = node.next.data
                node.next = node.next.next
            else:
                print("This is last node, require head, can't be freed"); 
                return; 

    def find_mid_element(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while (fast_ptr and fast_ptr.next != None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print("Middle point:", slow_ptr.data)
        return slow_ptr

    def find_mid_element_using_counter(self):
        mid_ptr = self.head
        curr = self.head
        counter = 0
        while (curr):
            if counter%2 != 0:
                mid_ptr = mid_ptr.next
            counter +=1
            curr = curr.next
        if mid_ptr != None:
            print("Middle point:", mid_ptr.data)
            return mid_ptr

    def get_list_count(self):
        curr = self.head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count

    def get_kth_from_mid_to_left(self, k):
        curr = self.head
        count = 1
        n = self.get_list_count()
        if n <= 0:
            return -1
        element_position = ((n/2 + 1) - k)
        while (curr != None):
            if count == element_position:
                return curr.data
            count+=1
            curr = curr.next

    def get_kth_from_mid_to_right(self, k):
        curr = self.head
        count = 1
        n = self.get_list_count()
        if n <= 0:
            return -1
        element_position = ((n/2 + 1) + k)
        while (curr != None):
            if count == element_position:
                return curr.data
            count+=1
            curr = curr.next

    def replace_head_by_mid(self):
        curr = self.head
        mid_ptr = self.find_mid_element()
        temp = curr.data
        curr.data = mid_ptr.data
        mid_ptr.data = temp

    def insert_middle(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            ptr = self.head
            length = 0
            while (ptr != None):
                ptr = ptr.next
                length += 1
            if(length%2 == 0):
                count = length/2
            else:
                count = (length + 1) /2
            ptr = self.head
            while (count >1):
                ptr = ptr.next
                count -= 1

            new_node.next = ptr.next
            ptr.next = new_node

    def insert_middle_double_ptr(self, data):
        new_node = Node(data)
        mid_ptr = self.find_mid_element()
        new_node.next = mid_ptr.next
        mid_ptr.next = new_node

    def insert_at_position(self, pos, data):
        if pos < 1:
            print ('Pass valid position')
        else:
            new_node = Node(data)
            curr = self.head
            count = 1
            while curr and count < pos-1:
                curr = curr.next
                count += 1
            new_node.next = curr.next
            curr.next = new_node

if __name__=='__main__': 
    # Start with the empty list 
    llist = LinkedList()
    # Insert from Head List
    print('*****Linked List 1 Prepand*******')
    llist.insert_from_head(1)
    llist.insert_from_head(2)
    llist.insert_from_head(3)
    llist.print_list()

    print('******Linked list 2 Append******')
    # Start with the empty list 
    llist2 = LinkedList()
    # Insert on End of List
    llist2.append_on_end(1)
    llist2.append_on_end(2)
    llist2.append_on_end(3)
    llist2.append_on_end(4)
    llist2.append_on_end(5)
    llist2.print_list()

    print('******Find Element******')
    llist2.find_element(2)
    llist2.find_element(4)
    llist2.find_element(6)

    print('***Reverse List***')
    llist2.reverse_list()

    print('***Reverse List***')
    llist2.reverse_list()

    print("*** Middle Element***")
    llist2.print_list()
    llist2.find_mid_element()

    print("*** Middle Element Using Counter***")
    llist2.print_list()
    llist2.find_mid_element_using_counter()

    print('***Delete Element***')
    llist2.remove(2)
    llist2.remove(8)
    llist2.print_list()

    print("*** Find Kth Element left to Mid***")
    llist3 = LinkedList()
    # Insert on End of List
    llist3.append_on_end(1)
    llist3.append_on_end(2)
    llist3.append_on_end(3)
    llist3.append_on_end(4)
    llist3.append_on_end(5)
    llist3.append_on_end(6)
    llist3.append_on_end(7)
    llist3.append_on_end(8)
    llist3.append_on_end(9)
    llist3.print_list()
    print('1 to left of mid', llist3.get_kth_from_mid_to_left(1))
    print('2 to left of mid', llist3.get_kth_from_mid_to_left(2))
    print('1 to right of mid', llist3.get_kth_from_mid_to_right(1))
    print('2 to right of mid', llist3.get_kth_from_mid_to_right(2))

    print('**** Replace Head by Middle node****')
    llist3.print_list()
    llist3.replace_head_by_mid()
    print('*** After Replacement***')
    llist3.print_list()


    print('*** Delete without Header pointer***')
    llist3.print_list()
    del_node = llist3.get_head_element().next.next.next.next.next.next.next
    llist3.delete_with_location_pointer(del_node)
    print('*** After Deletion***')
    llist3.print_list()

    print('**** Replace Head by Middle node****')
    llist3.print_list()
    llist3.replace_head_by_mid()
    print('*** After Replacement***')
    llist3.print_list()

    print('****Insert node in middle - Odd List****')
    llist4 = LinkedList()
    llist4.append_on_end(5)
    llist4.append_on_end(10)
    llist4.append_on_end(4)
    llist4.append_on_end(32)
    llist4.append_on_end(16)
    
    llist4.print_list()
    llist4.insert_middle(41)
    print('*** After Insert node in middle***')
    llist4.print_list()

    print('****Insert node in middle - Even List****')
    llist5 = LinkedList()
    llist5.append_on_end(1)
    llist5.append_on_end(2)
    llist5.append_on_end(4)
    llist5.append_on_end(5)
    llist5.print_list()
    # llist5.insert_middle(3)
    llist5.insert_middle_double_ptr(3)
    print('*** After Insert node in middle after node len/2,***')
    llist5.print_list()

    print('****Insert node in middle -Using double pointer****')
    llist6 = LinkedList()
    llist6.append_on_end(1)
    llist6.append_on_end(2)
    llist6.append_on_end(4)
    llist6.append_on_end(5)
    llist6.print_list()
    llist6.insert_middle_double_ptr(3)
    print('*** After Insert node in middle,***')
    llist6.print_list()

    print('***Insert element at given position***')
    llist6.print_list()
    llist6.insert_at_position(3, 9)
    print('***After Insert element at position 3, element 9***')
    llist6.print_list()
