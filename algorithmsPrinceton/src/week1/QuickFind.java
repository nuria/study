package week1;

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/23/13
 * Time: 2:56 PM
 * To change this template use File | Settings | File Templates.
 */

/**
 * we can have a large number of operations but also a large number of objects *
 */
public class QuickFind implements UnionFindInterface {

    /**
     * Number of objects we are dealing with *
     */
    protected int cardinal;


    /**
     * keeps track of leaders for each node, we are always falling back to
     * the 2nd node in union(a,b) *
     */
    protected int[] leaders;

    /**
     * Initialize data structure with "n" objects
     *
     * @param n
     */
    public QuickFind(int n) {
        this.cardinal = n;
        // we are going to initialize assuming we have 'n' nodes
        // numbered 1 to n

        this.leaders = new int[n];

        for (int i = 0; i < n; i++) {

            this.leaders[i] = i;
        }


    }

    /**
     * are p and q connected ?*
     */
    public boolean connected(int p, int q) {
        return leaders[p] == leaders[q];

    }

    /**
     * add connection between p and q
     * we change the id of the nodes to the second node id
     * for the first node and all nodes that have the same leader than the 1st
     * *
     */
    public void union(int p, int q) {
        if (connected(p, q)) {
            return;
        }

        int oldLeader = leaders[p];
        for (int i = 0; i < this.cardinal; i++) {
            if (leaders[i] == oldLeader) {
                leaders[i] = leaders[q];
            }
        }

    }


    /**
     * identifier for p between 1 and n-1
     * not sure what to do here
     * *
     */
    public int find(int p) {
        return p;
    }

    public String toString() {
        StringBuffer msg = new StringBuffer("{");
        for (int i = 0; i < this.cardinal; i++) {
            msg.append(this.leaders[i] + ",");
        }
        return msg.append("}").toString();
    }
}
