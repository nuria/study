package week1;


/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/24/13
 * Time: 7:43 PM
 * To change this template use File | Settings | File Templates.
 */
public interface UnionFindInterface {


    /**
     * are p and q connected ?*
     */
    public boolean connected(int p, int q);

    /**
     * add connection between p and q*
     */
    public void union(int p, int q);

    /**
     * identifier for p between 1 and n-1
     * not sure what to do here
     * *
     */
    public int find(int p);
}
