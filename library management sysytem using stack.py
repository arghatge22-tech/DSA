class Library:
    def __init__(self):
        self.TOP = -1
        self.st = [""] * 100

    def add_book(self, x):
        if self.TOP == 99:
            print("Library Full")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def issue_book(self):
        if self.TOP == -1:
            print("No Books Available")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x

    def peek(self):
        if self.TOP == -1:
            print("Library is Empty")
        else:
            print("Next Book to Issue =", self.st[self.TOP])

    def display(self):
        if self.TOP == -1:
            print("Library is Empty")
        else:
            print("Books in Library:")
            for i in range(self.TOP, -1, -1):
                print(self.st[i], end=" | ")
            print()


s = Library()

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Peek (Next Book)")
    print("4. Display Books")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter Book Title: ")
        s.add_book(x)

    elif ch == 2:
        x = s.issue_book()
        if x is not None:
            print("Issued Book =", x)

    elif ch == 3:
        s.peek()

    elif ch == 4:
        s.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
