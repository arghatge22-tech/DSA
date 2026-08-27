class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x

    def peek(self):
        if self.TOP == -1:
            print("Stack is Empty")
        else:
            print("Top Element =", self.st[self.TOP])

    def display(self):
        if self.TOP == -1:
            print("Stack is Empty")
        else:
            print("Stack Elements:")
            for i in range(self.TOP, -1, -1):
                print(self.st[i], end=" ")
            print()


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = int(input("Enter Element: "))
        s.push(x)

    elif ch == 2:
        x = s.pop()
        if x is not None:
            print("Popped Element =", x)

    elif ch == 3:
        s.peek()

    elif ch == 4:
        s.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
