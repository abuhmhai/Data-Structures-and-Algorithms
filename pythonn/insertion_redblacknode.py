class Node:
    def __init__(self, data, color='R'):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(None)
        self.root = self.TNULL

    # Preorder traversal
    def preorder_helper(self, node):
        if node != self.TNULL:
            print(node.data, end=" ")
            self.preorder_helper(node.left)
            self.preorder_helper(node.right)

    # Rotate left
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotate right
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Balance the tree after insertion
    def balance_insert(self, k):
        while k.parent.color == 'R':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'B'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'R'
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 'B'
            return
        if node.parent.parent == None:
            return
        self.balance_insert(node)

    # Print the tree using preorder traversal
    def preorder(self):
        self.preorder_helper(self.root)


# Example usage
if __name__ == "__main__":
    rbt = RedBlackTree()

    rbt.insert(2)
    rbt.insert(1)
    rbt.insert(4)
    rbt.insert(5)
    rbt.insert(9)
    rbt.insert(3)
    rbt.insert(6)
    rbt.insert(7)

    print("Preorder traversal:")
    rbt.preorder()
