import java.math.*;

class program
{
   public static void main(String args[])
   {    
        //System.out.println(sum_of_digit(6.0));                //Q-1

        //System.out.println(Algorithm𝑋𝑌𝑍(5, 6, 6));              // Q-2

        //System.out.println(XYZ(9));                            // Q-3        
       System.out.println(RecursiveXYZ(7));                    // Q-3


   }

    // queston 1
    static double sum_of_digit(double n) {
        if (n == 0)
            return 0;
        return Math.pow(n, 3) + sum_of_digit(n - 1);
    }


    // Question 2
    public static int Algorithm𝑋𝑌𝑍(int r, int q, int n) {
        if (n == 1) {
            System.out.println("this is r ........." + r);
            System.out.print("The sum of the series: ");
            return r;
        } else if (n % 2 == 1) {
            System.out.println(n+ " is odd........." + ((n - 1) * q));
            return Algorithm𝑋𝑌𝑍(r, q, n - 1) + ((n - 1) * q);
        } else {
            System.out.println(n + " is even........." + (-1 * (n - 1) * q));
            return Algorithm𝑋𝑌𝑍(r, q, n - 1) - ((n - 1) * q);
        }
    }



    // queston 3
    public static int XYZ(int n)
    {
        int a = 0;
        int b = 1;
        int temp = 0;
        if (n == 0 || n == 1)
            return 1;
        else{
            for (int i = 2; i <= n; i++){
                temp = b;
                b = b+a;
                a = temp;
            }
        }
      return b;
    }
    //question 3
    public static int RecursiveXYZ(int n) {
        if ((n == 0) || (n == 1))
            return n;
        else
            System.out.println("..........." + (n-1) + ".." + (n-2));
            return RecursiveXYZ(n - 1) + RecursiveXYZ(n - 2);
    }

}
