import java.util.*;

public class Setclass {
    private Set<Integer> a;

    public Setclass(Integer[] Array) {
        a = new HashSet<Integer>();
        a.addAll(Arrays.asList(Array));
    }

    public void findUnion(Set<Integer> b) {
        Set<Integer> union = new HashSet<Integer>(a);
        union.addAll(b);
        System.out.print("Union of the two Set");
        System.out.println(union);
    }

    public void findIntersection(Set<Integer> b) {
        Set<Integer> intersection = new HashSet<Integer>(a);
        intersection.retainAll(b);
        System.out.print("Intersection of the two Set");
        System.out.println(intersection);
    }

    public void findDifference(Set<Integer> b) {
        Set<Integer> difference = new HashSet<Integer>(a);
        difference.removeAll(b);
        System.out.print("Difference of the two Set");
        System.out.println(difference);
    }

    public void findCartesian(Set<Integer> b) {
        System.out.print("the cartesian product is: ");
        for (int stock1 : a) {
            for(int stock2: b)
            {
                System.out.print("{" + stock1 + ", " + stock2 + "}, ");
            }
        }
        System.out.println();
    }

    public void isSubset(Set<Integer> b) {
        System.out.println(b.containsAll(a));
    }

    public void isEmpty() {
        System.out.println("Is it empty? " + a.isEmpty());
    }

    public void isElement(int b) {
        System.out.println(a.contains(b));
    }

    public void isEqual(Set<Integer> b) {
        System.out.println(a.equals(b));
    }

    public void getCardinality() {
        System.out.println(a.size());
    }

    public void addElement(int b) {
        if(a.contains(b))
            System.out.println("Element already is the set");
        else
            a.add(b);
        System.out.println(a);
    }

    public void removeElement(int b) {
        a.remove(b);
        System.out.println("the remove is: " + a);
    }

    public void Clear() {
        Set<Integer> aClear = new HashSet<Integer>(a);
        // a.clear();
        aClear.clear();
        System.out.println("The clear method is: " + aClear);
    }

    public void toArray() {
      Integer[] array = a.stream().toArray(Integer[]::new);
      System.out.println("This is the toArray method: " + Arrays.toString(array));
    }

    public void print() {
      System.out.println("This is the printmethod: " + a);
    }

}
