package week4;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/28/13
 * Time: 9:30 PM
 * To change this template use File | Settings | File Templates.
 */
public class MaxPQ<Key extends Comparable<Key>> {

    private Key[] pq = (Key[]) new Comparable[]{};

    /**
     * let's keep track of current, we do not use index 0, start at index 1 *
     */
    private int current = 0;


    public MaxPQ(int capacity) {

        pq = (Key[]) new Comparable[capacity + 1];

    }

    /**
     * insert at the end (leaf).
     * keep on bubbling it up
     *
     * @param k
     */
    public void insert(Key key) {
        //insert at the end
        current++;
        pq[current] = key;
        swim(current);

    }


    /**
     * exchange node with one at the end
     * bubble until heap property is satisfied
     *
     * @return
     */
    Key delMax() {
        Key max = pq[1];
        // exchange with node at the bottom
        exch(pq, 1, current);
        sink(1);

        pq[current] = null;
        current--;
        return max;
    }


    boolean isEmpty() {
        return this.current == 0;
    }


    /**
     * If Child becomes larger than its parent
     * Exchange kid with parent until order is restaured
     * for node k parent is at k/2
     *
     * @param k child node *
     */
    private void swim(int k) {
        while (k > 1 && less(k / 2, k)) {

            exch(pq, k, k / 2);
            k = k / 2;
        }
    }

    /**
     * Parent becomes smaller than one of its children
     * Trade parent with the largest children until that is no longer the case
     *
     * @param k parent node
     */
    private void sink(int k) {

        while (2 * k < current) {
            //make sure children are actually bigger
            // if not just break
            if (!(less(k, 2 * k + 1) || less(k, 2 * k))) {
                break;
            }

            //see what children is smaller
            if (less(2 * k, 2 * k + 1)) {
                exch(pq, k, 2 * k + 1);
                k = 2 * k + 1;
            } else {
                exch(pq, k, 2 * k);
                k = 2 * k;
            }

        }
    }

    public boolean less(int u, int w) {
        return pq[u].compareTo(pq[w]) < 0;
    }

    // exchanges two items but changes the object we are passing
    public static void exch(Comparable[] a, int i, int j) {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }


    public String toString() {
        StringBuffer sb = new StringBuffer();
        sb.append("{");
        for (int i = 0; i < pq.length; i++) {
            sb.append(" " + i + "=>" + pq[i] + ",");

        }
        sb.append("}");
        return sb.toString();
    }
}
