class Node:
    # Step 1: Create Node
    """
      This class creates node
      _________ ___________
     | element| nextPointer|
     |________|____________|

    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # Step 2: Linking of nodes
    def __init__(self):
        self.head = None

    # Adds new element at start

    def addFirst(self, data):
        newNode = Node(data)  # You can add self.head as a 2nd parameter because
        # 2nd parameter expects us to pass address of next node
        newNode.next = self.head
        self.head = newNode

    def addLast(self, data: object) -> object:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = newNode

    # Takes list of data as input and creates link out of it
    def insertValues(self, data_list):
        # self.head = None
        for data in data_list:
            self.addLast(data)

    # Function to insert a node at given position
    def insert_at_position(self, position, data):
        if self.head is None:
            return

        if position == 0 or position > ll.get_len():
            raise Exception("Insertion failed!!")
            return

        if position == 1:
            ll.addFirst(data)
            return

        newNode = Node(data)
        itr = self.head
        for i in range(1, position - 1):
            itr = itr.next
        newNode.next = itr.next
        itr.next = newNode

    # Removing element from the end Method 1 (Same logic as method 2)

    # def del_start(self):
    #     if self.head is None:
    #         return
    #
    #     del_node = self.head
    #     self.head = del_node.next
    #     del_node.next = None

    # Removing element from the end Method 1 (Same logic as method 2)

    # def del_end(self):
    #     if self.head is None:
    #         return
    #
    #     prev_node = self.head
    #     del_last_node = self.head.next
    #     while del_last_node.next is not None:
    #         del_last_node = del_last_node.next
    #         prev_node = prev_node.next
    #     prev_node.next = None

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_start(self):
        if self.head is None:
            raise Exception("Linked List is empty can't remove the element from the start")
        else:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            raise Exception("linked list is empty can't remove the element from the end")
        elif self.head.next is None:
            self.head = None
        else:
            itr = self.head
            while itr.next.next is not None:
                itr = itr.next

            itr.next = None

    def remove_at_loc(self, index):
        if index <= 0 or index > ll.get_len():
            raise Exception("Invalid index")
            return

        if index == 1:
            ll.remove_start()
            return

        oneLessThanIndex = 1
        itr = self.head
        while itr:
            if oneLessThanIndex == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            oneLessThanIndex += 1

    # Inserting value next to a data existing in a linked list
    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head
        while itr.data is not None:
            if itr.data != data_after:
                itr = itr.next
            else:
                break

        if itr.data is None:
            raise Exception(data_after, " value not found!!")
            return

        newNode = Node(data_to_insert)
        newNode.next = itr.next
        itr.next = newNode

    def remove_by_value(self, rm_data):

        if rm_data == self.head.data:
            ll.remove_start()
            return

        itr = self.head
        count = 1
        while itr.next is not None:
            if itr.next.data != rm_data:
                itr = itr.next
                count += 1
            else:
                break

        if count == ll.get_len() - 1:
            itr.next = itr.next.next
        else:
            raise Exception(rm_data, " value not found!!")
            return

    # Displays the list
    def displayList(self):
        if self.head is None:
            raise Exception("List is empty")
            return
        else:
            itr = self.head
            llstr = ''

            while itr is not None:
                # print(itr.data, "----> ", end='')
                llstr += str(itr.data) + '----->'
                itr = itr.next

            print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.addFirst(12)
    # ll.addFirst(2)
    # ll.addFirst(34)
    # ll.addFirst(56)
    ll.insertValues(['Ankit', 'Prakash', 'Jalaja', 'Aniket', 'Sonu'])
    # ll.addLast(45)
    # ll.insert_at_position(5, 'Pjaa')
    # ll.addFirst('Ankit')
    # # ll.remove_start()
    # ll.remove_end()
    # ll.remove_at_loc(5)
    # ll.insert_after_value('Ankit', 'Pjaa')
    ll.remove_by_value('Sonu')
    ll.displayList()

    print("length: ", ll.get_len())
