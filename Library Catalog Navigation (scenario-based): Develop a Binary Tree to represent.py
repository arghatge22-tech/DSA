class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert at the first free position (level order), keeps the tree complete
    def insert(self, x):
        new = Node(x)

        if self.root is None:
            self.root = new
            return

        q = [self.root]
        while q:
            temp = q.pop(0)

            if temp.left is None:
                temp.left = new
                return
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = new
                return
            else:
                q.append(temp.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def levelorder(self):
        if self.root is None:
            print("Catalog is Empty")
            return

        q = [self.root]
        while q:
            temp = q.pop(0)
            print(temp.data, end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        print()

    def search(self, x):
        if self.root is None:
            return False

        q = [self.root]
        while q:
            temp = q.pop(0)
            if temp.data == x:
                return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False


t = BinaryTree()

while True:
    print("\n--- Library Catalog Navigation ---")
    print("1. Insert Section/Book")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Level Order")
    print("6. Search")
    print("7. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter Section/Book Name: ")
        t.insert(x)

    elif ch == 2:
        if t.root is None:
            print("Catalog is Empty")
        else:
            t.inorder(t.root)
            print()

    elif ch == 3:
        if t.root is None:
            print("Catalog is Empty")
        else:
            t.preorder(t.root)
            print()

    elif ch == 4:
        if t.root is None:
            print("Catalog is Empty")
        else:
            t.postorder(t.root)
            print()

    elif ch == 5:
        t.levelorder()

    elif ch == 6:
        x = input("Enter Name to Search: ")
        print("Found" if t.search(x) else "Not Found")

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
