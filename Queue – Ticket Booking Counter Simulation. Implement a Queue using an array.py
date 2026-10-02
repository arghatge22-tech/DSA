class Queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.qt = [""] * 100

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
            print("Next Customer =", self.qt[self.F])

    def display(self):
        if self.F == -1:
            print("Queue is Empty")
        else:
            print("Customers Waiting:")
            for i in range(self.F, self.R + 1):
                print(self.qt[i], end=" ")
            print()


q = Queue()
tickets_booked = 0

while True:
    print("\n--- Ticket Booking Counter ---")
    print("1. Join Queue (Insert Customer)")
    print("2. Book Ticket (Serve Customer)")
    print("3. Peek (Next Customer)")
    print("4. Display Queue")
    print("5. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter Customer Name: ")
        q.insert(x)

    elif ch == 2:
        x = q.delete()
        if x is not None:
            tickets_booked += 1
            print("Ticket Booked for", x)

    elif ch == 3:
        q.peek()

    elif ch == 4:
        q.display()

    elif ch == 5:
        print("Total Tickets Booked =", tickets_booked)
        break

    else:
        print("Invalid Choice")
