# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LL:
    def __init__(self):
        self.head = None

    # Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        if n <= 0:
            print("Enter valid number of nodes.")
            return

        for i in range(1, n + 1):
            value = int(input(f"Enter value {i}: "))
            self.insert(value)

        print("Linked List created successfully.")

    # Insert Node at End
    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Delete Node
    def delete(self, value):
        if self.head is None:
            print("Linked List is empty.")
            return

        # Delete first node
        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                print("Node deleted.")
                return

            prev = temp
            temp = temp.next

        print("Node not found.")

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
obj = LL()

obj.create()

while True:
    print("\n----- MENU -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        value = int(input("Enter value to insert: "))
        obj.insert(value)

    elif ch == 2:
        value = int(input("Enter value to delete: "))
        obj.delete(value)

    elif ch == 3:
        obj.display()

    elif ch == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
