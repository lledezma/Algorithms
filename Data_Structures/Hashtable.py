class Node:
    def __init__(self, data, name):
        self.key = data
        self.name = name
        self.link = None


class hashTable:
    def __init__(self):
        self.tableSize = 10;
        self.table = [0 for _ in range(0,self.tableSize)]
        for i in range(10):
            self.table[i] = Node(i,"")
            self.table[i].link = None
        
    def hashing_funct(self,data):
        hashed_node = data % self.tableSize
        return hashed_node

    def add(self, data, name):
        hash_key = self.hashing_funct(data)
        key_exists = True
        n = self.table[hash_key]
        if n.link is None:
            new_node = Node(data,name)
            new_node.link = None
            n.link = new_node
        else:
            n = n.link
            while(key_exists):
                if n.key == data:
                    return("key already exists")
                elif n.link is None:
                    new_node = Node(data,name)
                    new_node.link = None
                    n.link = new_node
                    key_exists = False
                else:
                    n = n.link

    def delete(self,data):
        hash_key = self.hashing_funct(data)
        key_exists = True
        elementList = self.table[hash_key]
        n = elementList.link
        if n == None:
            return("Element " + str(data) +  " doesnt exist")
        else:
            prevNode = elementList
            while(key_exists):
                if n.key == data:
                    if n.link is None:
                        prevNode.link = None
                        return
                    elif n.link is not None:
                        prevNode.link = n.link
                        return
                elif n.link is None:
                    key_exists = False
                else:
                    prevNode = n
                    n = n.link
            print("Element " + str(data) +  " doesnt exist")
        return

    def get(self,data):
        hash_key = self.hashing_funct(data)
        elementList = self.table[hash_key]
        while(elementList.link is not None):
            elementList = elementList.link
            if (elementList.key == data):
                return elementList.name
        return("Element " + str(data) +  " doesnt exist")


newlist = hashTable()