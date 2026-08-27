# ---------------- Node Class ----------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ---------------- Create Binary Tree ----------------

def create():
    x = int(input("Enter data (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root


# ---------------- Preorder Traversal ----------------

def preorder(temp):
    if temp is not None:
        print(temp.data, end=" ")
        preorder(temp.left)
        preorder(temp.right)


# ---------------- Inorder Traversal ----------------

def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)


# ---------------- Postorder Traversal ----------------

def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")


# ---------------- Main Program ----------------

root = create()

print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)
