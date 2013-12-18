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
public class InsertionSort {


    public static void sort(Comparable[] a) {

        int i = 1;

        int exchangeCounter = 0;

        while (i < a.length) {

            int k = i;
            while (k > 0 && InsertionSort.less(a[k], a[k - 1])) {
                InsertionSort.exch(a, k, k - 1);
                exchangeCounter++;
                if (exchangeCounter == 4) {

                    for (Object o : a) {
                        System.out.print(o);
                        System.out.print(" ");
                    }
                }
                k--;
            }
            i++;
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
