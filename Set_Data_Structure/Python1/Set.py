
class Set:
    a = []
    def __init__(self, array):
        self.a = array

    def findUnion(self, b):
        unionlist = self.a + b
        print(unionlist)

    def findIntersection(self, b):
        interArray = []
        for x in (self.a):
            for y in (b):
                if(x == y):
                    if(x not in interArray):
                        interArray.append(x)
                    else:
                        pass
        print(interArray)

    def findDifference(self, b):
        diffArray = [item for item in self.a if item not in b]
        print(diffArray)

    def findCartesian(self,b):
        cartArray = []
        for x in (self.a):
            for y in (b):
                cartArray.append("(" + str(x) + "," + str(y) + ")")
        print(cartArray)

    def isSubset(self, b):
        count = []
        for x in (b):
            for y in (self.a):
                if(x == y):
                    if (x not in count):
                     count.append(x)
        if(len(count) == len(self.a)):
            print("true")
        else:
            print("false")


    def isEmpty(self):
        counter = 0
        for x in (self.a):
            counter+=1
        if counter == 0:
            return True
        else:
            return False

    def isElement(self, element):
        for x in (self.a):
            if(x == element):
                return True
        return False

    def isEqual(self, b):
        counta = 0
        countb = 0
        for x in (self.a):
            counta+=1
        for y in (b):
            countb+=1
        if (counta == countb):
            return True
        else :
            return False

    def getCardinality(self):
        array = []
        counter = 0
        for x in self.a:
            if (x not in array):
                array.append(x)
                counter +=1
        print(counter)

    def addElement(self,element):
        counter =0
        for x in self.a:
            if x == element:
                counter +=1
        if counter <= 0:
            self.a.append(element)

    def removeElement(self, element):
        newarray = []
        for x in self.a:
            if x != element:
                newarray.append(x)
        self.a = newarray
        print (self.a)

    def Clear(self):
        self.a = []

    def toArray(self):
        self.a

    def print(self):
        for x in self.a:
            print(x)
