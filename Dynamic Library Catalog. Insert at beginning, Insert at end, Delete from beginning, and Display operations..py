class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new

    def delete_beginning(self):
        if self.head is None:
            print("Catalog is Empty")
            return

        x = self.head.data
        self.head = self.head.next
        return x

    def display(self):
        if self.head is None:
            print("Catalog is Empty")
        else:
            print("Library Catalog:")
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")


ll = LinkedList()

while True:
    print("\n--- Library Catalog ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter Book Title: ")
        ll.insert_beginning(x)

    elif ch == 2:
        x = input("Enter Book Title: ")
        ll.insert_end(x)

    elif ch == 3:
        x = ll.delete_beginning()
        if x is not None:
            print("Deleted Book =", x)

    elif ch == 4:
        ll.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
