
class HashTable:
    def __init__(self, size, replacement=False):
        self.size = size
        self.table = [None] * size
        self.replacement = replacement

    def hash_function(self, key):
        return key % self.size

    def insert_without_replacement(self, key):
        index = self.hash_function(key)

        for step in range(self.size):
            pos = (index + step) % self.size

            if self.table[pos] == key:
                print("Duplicate key:", key)
                return False

            if self.table[pos] is None:
                self.table[pos] = key
                return True

        print("Hash table is full. Cannot insert", key)
        return False

    def insert_with_replacement(self, key):
        home = self.hash_function(key)

        if key in self.table:
            print("Duplicate key:", key)
            return False

        if self.table[home] is None:
            self.table[home] = key
            return True

        occupant = self.table[home]
        occupant_home = self.hash_function(occupant)

        if occupant_home != home:
            self.table[home] = key
            displaced = occupant
            start = (home + 1) % self.size

            for step in range(self.size - 1):
                pos = (start + step) % self.size

                if self.table[pos] is None:
                    self.table[pos] = displaced
                    return True

            self.table[home] = occupant
            print("Hash table is full. Cannot insert", key)
            return False

        for step in range(1, self.size):
            pos = (home + step) % self.size

            if self.table[pos] is None:
                self.table[pos] = key
                return True

        print("Hash table is full. Cannot insert", key)
        return False

    def insert(self, key):
        if self.replacement:
            return self.insert_with_replacement(key)
        return self.insert_without_replacement(key)

    def search(self, key):
        home = self.hash_function(key)

        for step in range(self.size):
            pos = (home + step) % self.size

            if self.table[pos] is None:
                return -1

            if self.table[pos] == key:
                return pos

        return -1

    def display(self):
        print("\nIndex\tKey")
        print("----------------")

        for index, key in enumerate(self.table):
            print(index, "\t", key if key is not None else "EMPTY")


def main():
    size = int(input("Enter hash table size: "))

    choice = int(input(
        "Choose collision handling "
        "(1: Without replacement, 2: With replacement): "
    ))

    ht = HashTable(size, replacement=(choice == 2))

    while True:
        print("\n----- HASH TABLE MENU -----")
        print("1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            key = int(input("Enter key to insert: "))
            ht.insert(key)

        elif ch == 2:
            key = int(input("Enter key to search: "))
            result = ht.search(key)

            if result != -1:
                print("Key found at index:", result)
            else:
                print("Key not found")

        elif ch == 3:
            ht.display()

        elif ch == 4:
            print("Program terminated.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
