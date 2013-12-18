package week4;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/29/13
 * Time: 1:34 PM
 * To change this template use File | Settings | File Templates.
 */
public class Heapsort {


    public static void sort(Comparable[] a) {
        // go through array bottoms up
        int N = a.length;

        //bring array into heap ordering
        for (int i = N - 1; i >= 0; i--) {
            sink(a, i, N);
        }

        System.out.println(Heapsort._toString(a));

        //now keep extracting max and putting it at the bottom of the array
        //max would be the first element of the array
        while (N > 0) {
            //exchange 1st element with last
            exch(a, 0, N - 1);
            N--;
            sink(a, 0, N);
        }


    }

    private static String _toString(Comparable[] a) {
        StringBuffer sb = new StringBuffer();
        sb.append("{");
        for (int i = 0; i < a.length; i++) {
            sb.append(" " + i + "=>" + a[i] + ",");

        }
        sb.append("}");
        return sb.toString();
    }

    /**
     * Parent becomes smaller than one of its children
     * Trade parent with the largest children until that is no longer the case
     *
     * @param k parent node
     */
    private static void sink(Comparable[] a, int k, int N) {

        int lChild = 2 * k;
        int rChild = 2 * k + 1;

        //   System.out.println("index k "+k+" with value"+a[k]);

        if (!(lChild < N)) {
            return; //leaf nodes, we have reached the end
        }

        if (rChild < N && (less(a, k, rChild) || less(a, k, lChild))) {
            //compare right and left  nodes
            if (less(a, rChild, lChild)) {
                exch(a, k, lChild);
                sink(a, lChild, N);
            } else {
                exch(a, k, rChild);
                sink(a, rChild, N);
            }

        } else if (less(a, k, lChild)) {
            //only left node, it's a leaf
            exch(a, k, lChild);

        }


    }

    private static boolean less(Comparable[] a, int u, int w) {
        return a[u].compareTo(a[w]) < 0;
    }

    // exchanges two items but changes the object we are passing
    public static void exch(Comparable[] a, int i, int j) {

        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }


}
