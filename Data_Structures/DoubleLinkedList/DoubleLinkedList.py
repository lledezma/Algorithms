class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def Search(self, value):
        current = self.start_node
        while current:
            if current.item == value:
                print("record in the list")
                return True
            else:
                current = current.next
        print("record not in the list")
        return False

    def AppendHead(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("List initiated \n")
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.previous = new_node
        self.start_node = new_node

    def AppendTail(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.previous = n

    def RemoveHead(self):
        if self.start_node is None:
            print("There are no elements to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def RemoveEnd(self):
        if self.start_node is None:
            print("The list is empty")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.previous.next = None

    def Delete(self, x):
        if self.start_node is None:
            print("The list is empty")
            return
        if self.start_node.next is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item deleted")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.next
            self.start_node.previous = None
            return

        n = self.start_node
        while n.next is not None:
            if n.item == x:
                break
            n = n.next
        if n.next is not None:
            n.previous.next = n.next
            n.next.previous = n.previous
        else:
            if n.item == x:
                n.previous.next = None
            else:
                print("Element not found")

    def PrintList(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                for x in n.item:
                    print(x)
                print("")
                n = n.next
