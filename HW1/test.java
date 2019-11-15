import java.util.*;

public class test {

    public static void main(String[] args) {
        //array to send to the Setclass
        Integer [] aArray = new Integer[]{ 1, 3, 2, 4, 8, 9, 0 };
        Integer [] bArray = new Integer[]{1, 3, 7, 5, 4, 0, 7, 5 };

        //Set to test the methods
        Set<Integer> b = new HashSet<Integer>();
        b.addAll(Arrays.asList(new Integer[] { 1, 4, 2, 9, 14, 8, 3, 0 }));

        //initializing two constructors with two diff arrays
        Setclass testSet = new Setclass(aArray);
        Setclass testSet2 = new Setclass(bArray);

        //testing each method with both constructors
        testSet.findUnion(b);
        testSet2.findUnion(b);

        testSet.findIntersection(b);
        testSet2.findIntersection(b);

        testSet.findDifference(b);
        testSet2.findDifference(b);

        testSet.findCartesian(b);
        testSet2.findCartesian(b);

        testSet.isSubset(b);
        testSet2.isSubset(b);

        testSet.isEmpty();
        testSet2.isEmpty();

        testSet.isElement(4);
        testSet2.isElement(4);

        testSet.isEqual(b);
        testSet2.isEqual(b);

        testSet.getCardinality();
        testSet2.getCardinality();

        testSet.addElement(10);
        testSet2.addElement(10);

        testSet.removeElement(10);
        testSet2.removeElement(10);

        testSet.Clear();
        testSet2.Clear();

        testSet.toArray();
        testSet2.toArray();

        testSet.print();
        testSet2.print();
    }

}
