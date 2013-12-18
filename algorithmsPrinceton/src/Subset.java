/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/20/13
 * Time: 7:13 AM
 * To change this template use File | Settings | File Templates.
 */

/**
 * Write a client program Subset.java that takes a command-line integer k,
 * reads in a sequence of N strings from standard input using StdIn.readString(),
 * and prints out exactly k of them, uniformly at random.
 * Each item from the sequence can be printed out at most once.
 * You may assume that k ≥ 0 and no greater than the number of string on standard input.
 */
public class Subset {


    /**
     * Note <Ctrl-d> signifies the end of file on Unix.
     * On windows use <Ctrl-z>.
     */
    public static void main(final String[] args) {

        final int k = Integer.parseInt(args[0]);

        RandomizedQueue<String> q = new RandomizedQueue<String>();

        while (!StdIn.isEmpty()) {
            String value = StdIn.readString();
            q.enqueue(value);
        }


        //deque? or rather just use the iterator
        for (int i = 1; i <= k; i++) {
            StdOut.println(q.dequeue());
        }

    }
}
