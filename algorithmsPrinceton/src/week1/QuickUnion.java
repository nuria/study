package week1;

import java.util.ArrayList;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/24/13
 * Time: 7:42 PM
 * To change this template use File | Settings | File Templates.
 */
public class QuickUnion implements UnionFindInterface {

    /**
     * Array in which each element points to its preceding node
     * Thus if we connect 1 and 2 1->1 2->1, if we connect 2 and 3
     * 2->1, 3->2
     */
    protected int[] leaders;
    int cardinal;

    //stores sizes of clusters, keyed by node
    int[] size;

    public QuickUnion(int n) {
        this.cardinal = n;
        // we are going to initialize assuming we have 'n' nodes
        // numbered 1 to n

        this.leaders = new int[n];
        this.size = new int[n];

        for (int i = 0; i < n; i++) {

            leaders[i] = i;
            size[i] = 1;
        }
    }

    @Override
    public boolean connected(int p, int q) {
        //traverse up and see if p is in the line of q or viceversa
        return root(p) == root(q);

    }

    private int root(int p) {
        int i = p;

        while (i != leaders[i]) {
            i = leaders[i];


        }

        return i;
    }


    @Override
    public void union(int p, int q) {
        //we assume p is the leader
        int proot = root(p);
        int qroot = root(q);

        if (size[proot] >= size[qroot]) {
            //when joining two trees of equal size, our weighted quick union convention
            //is to make the root of the second tree point to the root of the first tree.
            leaders[qroot] = proot;
            size[proot] = size[proot] + size[qroot];

        } else {

            leaders[proot] = qroot;
            size[qroot] = size[proot] + size[qroot];
        }
    }

    /* mmmm... not so sure what to do here **/
    @Override
    public int find(int p) {
        return 0;  //To change body of implemented methods use File | Settings | File Templates.
    }

    public String toString() {
        StringBuffer msg = new StringBuffer("{");
        for (int i = 0; i < this.cardinal; i++) {
            msg.append(this.leaders[i] + ",");
        }
        return msg.append("}").toString();
    }
}
