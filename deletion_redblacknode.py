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

    def search(self, node, key):
        if node == self.TNULL or key == node.data:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'B' and w.left.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'

    def delete(self, key):
        z = self.search(self.root, key)
        if z == self.TNULL:
            print("Node not found.")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'B':
            self.delete_fixup(x)

    def preorder_helper(self, node):
        if node != self.TNULL:
            print(node.data, end=" ")
            self.preorder_helper(node.left)
            self.preorder_helper(node.right)

    def preorder(self):
        self.preorder_helper(self.root)

if __name__ == "__main__":
    rbt = RedBlackTree()

    rbt.insert(55)
    rbt.insert(40)
    rbt.insert(65)
    rbt.insert(60)
    rbt.insert(75)
    rbt.insert(57)

    print("Preorder traversal:")
    rbt.preorder()

    rbt.delete(55)
    rbt.delete(65)

    print("\nPreorder traversal after deletion:")
    rbt.preorder()
