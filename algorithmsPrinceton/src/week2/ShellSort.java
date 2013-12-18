package week2; /**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/15/13
 * Time: 11:18 PM
 * To change this template use File | Settings | File Templates.
 */

/**
 * To have nice semantics note that we are going to use
 * objects that implement comparable interface
 */
public class ShellSort {


    public static void sort(Comparable[] a) {


        int N = a.length;
        System.out.println("length " + a.length);

        // 3x +1 integer sequence
        // we start at  n/3 and keep dividing by three until we have 1.

        int[] sequence = new int[N / 3];


        for (int j = 0; j < N / 3; j++) {
            sequence[j] = 3 * j + 1;     //1,4,7,10,13...
        }


        for (int j = sequence.length - 1; j >= 0; j--) {
            int h = sequence[j];
            int k = h;
            int i = 1;
            //  System.out.println("***** h ="+h);
            while (k < N) {
                //   System.out.println("k ="+k);
                //   System.out.println("comparing "+a[k]+" and "+a[k-h]);
                while (k > 0 && ShellSort.less(a[k], a[k - h])) {
                    //    System.out.println("swapping "+a[k-h]+"with"+a[k] );
                    ShellSort.exch(a, k, k - h);

                    k = k - h;

                }
                i++;
                k = i * h;
            }

        }
    }


    // exchanges two items but changes the object we are passing
    public static void exch(Comparable[] a, int i, int j) {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    public static boolean less(Comparable u, Comparable w) {
        return u.compareTo(w) < 0;
    }


}
