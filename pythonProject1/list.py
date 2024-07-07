class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        if not self.head:
            self.head = Node(data)
        else:
            if position == 0:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                prev = self.head
                for _ in range(position - 1):
                    if prev is not None:
                        prev = prev.next
                if prev is None:
                    print("Position out of range")
                else:
                    new_node = Node(data)
                    new_node.next = prev.next
                    prev.next = new_node

    def delete(self, position):
        if self.head:
            if position == 0:
                self.head = self.head.next
            else:
                prev = self.head
                for _ in range(position - 1):
                    if prev is not None:
                        prev = prev.next
                if prev is None or prev.next is None:
                    print("Position out of range")
                else:
                    prev.next = prev.next.next
        else:
            print("List is empty")

    def traverse(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


# User input
ll = LinkedList()
while True:
    print("\n1. Insert\n2. Delete\n3. Traverse\n4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the value to insert: "))
        position = int(input("Enter the position to insert at: "))
        ll.insert(data, position)
    elif choice == 2:
        position = int(input("Enter the position to delete from: "))
        ll.delete(position)
    elif choice == 3:
        print("The linked list is: ")
        ll.traverse()
    elif choice == 4:
        break
