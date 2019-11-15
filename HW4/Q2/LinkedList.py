class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def Push(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def Pop(self):
        if self.start_node is None:
            print("The list has no elements to Pop")
            return
        self.start_node = self.start_node.ref

    def Search(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def PrintList(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                for x in n.item:
                    print(x)
                print("")
                n = n.ref
