class Heap:
    def __init__(self):
        self.MinHeap = []
        self.LastIndex = -1

    def BuildHeap(self):
        len = self.LastIndex
        for i in range(len, -1 ,-1):
            self.Heapify(i)

    def Insert(self, value):
        self.MinHeap.append(value)
        self.LastIndex += 1
        if self.LastIndex < len(self.MinHeap):
            self.MinHeap[self.LastIndex] = value
        else:
            self.MinHeap.append(value)
        self.Heapify(self.LastIndex)

    def Extract(self):
        temp = []
        if self.LastIndex == -1:
            print("List is empty")
        for x in self.MinHeap:
          temp.append(x[4])
        index = temp.index(min(temp))
        self.MinHeap.pop(index)
        self.Heapify(0)

    def Heapify(self,index):
        if index == 0:
          while True:
              index_value = self.MinHeap[index]
              left_child_index, left_child_value = self.getLeftChild(
                  index, index_value)
              right_child_index, right_child_value = self.getRightChild(
                  index, index_value)
              if index_value <= left_child_value and index_value <= right_child_value:
                  break
              if left_child_value < right_child_value:
                  new_index = left_child_index
              else:
                  new_index = right_child_index
              self.MinHeap[new_index], self.MinHeap[index] =\
                  self.MinHeap[index], self.MinHeap[new_index]
              index = new_index
        else:
          while index > 0:
              parent_index, parent_value = self.getParent(index)
              if parent_value <= self.MinHeap[index]:
                  break
              self.MinHeap[parent_index], self.MinHeap[index] =\
                  self.MinHeap[index], self.MinHeap[parent_index]
              index = parent_index


    def getParent(self, index):
        if index == 0:
            return None, None
        parent_index = (index - 1) // 2
        return parent_index, self.MinHeap[parent_index]

    def getLeftChild(self, index, default_value):
        left_child_index = 2 * index + 1
        if left_child_index > self.LastIndex:
            return None, default_value
        return left_child_index, self.MinHeap[left_child_index]

    def getRightChild(self, index, default_value):
        right_child_index = 2 * index + 2

        if right_child_index > self.LastIndex:
            return None, default_value

        return right_child_index, self.MinHeap[right_child_index]

    def len(self):
        return self.LastIndex + 1

    def printHeap(self):
        for car in self.MinHeap:
            for info in car:
                print (info)
            print("")
