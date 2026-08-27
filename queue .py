class Queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.qt = [0] * 100

    def insert(self, x):
        if self.R == 99:
            print("Queue Overflow")
            return

        self.R += 1
        self.qt[self.R] = x

        if self.F == -1:
            self.F = 0

    def delete(self):
        if self.F == -1:
            print("Queue Underflow")
            return

        x = self.qt[self.F]

        if self.F == self.R:
            self.F = self.R = -1
        else:
            self.F += 1

        return x

    def peek(self):
        if self.F == -1:
            print("Queue is Empty")
        else:
            print("Front Element =", self.qt[self.F])

    def display(self):
        if self.F == -1:
            print("Queue is Empty")
        else:
            for i in range(self.F, self.R + 1):
                print(self.qt[i], end=" ")
            print()


q = Queue()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = int(input("Enter Element: "))
        q.insert(x)

    elif ch == 2:
        x = q.delete()
        if x is not None:
            print("Deleted Element =", x)

    elif ch == 3:
        q.peek()

    elif ch == 4:
        q.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
