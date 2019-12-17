from Set import *

#2 one dimension arrays that contain the elements of the set for each object
mainarray = [1, 3, 2, 4, 8, 9, 0]
mainarray2 = [1, 3, 7, 5, 4, 0, 7, 5]

#arrays to test the methods
testarray = [1,11,12,3,14,15,4]
barr = [1, 3, 2, 4, 8, 9, 0, 10]

#sending an array to initialize each object
testset = Set(mainarray)
testset2 = Set(mainarray2)

#test each method with each object
testset.findUnion(testarray)
testset2.findUnion(testarray)

testset.findIntersection(testarray)
testset2.findIntersection(testarray)

testset.findDifference(testarray)
testset2.findDifference(testarray)

testset.findCartesian(testarray)
testset2.findCartesian(testarray)

testset.isSubset(barr)
testset2.isSubset(barr)

print(testset.isEmpty())
print(testset2.isEmpty())

print(testset.isElement(100))
print(testset2.isElement(100))

print(testset.isEqual(testarray))
print(testset2.isEqual(testarray))

testset.getCardinality()
testset2.getCardinality()

testset.addElement(10)
testset2.addElement(10)

testset.removeElement(10)
testset2.removeElement(10)

testset.Clear()
testset2.Clear()

testset.toArray()
testset2.toArray()

testset.print()
testset2.print()
