class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def count(self):
        cnt = 0
        if self.left:
            cnt +=1
        if self.right:
            cnt +=1
        return cnt

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                print("No record found")
                return None, None
            return self.left.Search(data, self)
        elif data > self.data:
            if self.right is None:
                print("No record found")
                return None, None
            return self.right.Search(data, self)
        else:
            print("record found")
            return self, parent

    def delete(self, data):
        node, parent = self.Search(data)
        if node is not None:
            count = node.count()
        if count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None

        elif count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.data = n.data

        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        for x in self.data:
            print(x)
        print("")
        if self.right:
            self.right.print_tree()

########################################### Depth-first Search
    def dfs_preorder(self):
        print(self.data)
        if self.left:
            self.left.DFS_PreOrder()
        if self.right:
            self.right.DFS_PreOrder()

    def dfs_in_order(self):
        if self.left:
            self.left.DFS_InOrder()
        print(self.data)
        if self.right:
            self.right.DFS_InOrder()

    def dfs_posorder(self):
        if self.left:
            self.left.DFS_PosOrder()
        if self.right:
            self.right.DFS_PosOrder()
        print(self.data)
########################################### Breadth-first Search
    def BFS(self,root):
        if root.data == None:
            print("Tree is empty")
        queue = []
        queue.append(root)
        while(queue):
            node = queue.pop(0)
            print(node.data)
            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)
        return
