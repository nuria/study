import junit.framework.Assert;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.AfterClass;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/30/13
 * Time: 11:03 PM
 * To change this template use File | Settings | File Templates.
 */
public class PercolationTest {

    PercolationExtension p;

    class PercolationExtension extends Percolation {

        private int gridSize;
        private int lastNode;


        public PercolationExtension(int n) {

            super(n);
            this.gridSize = n;
            this.lastNode = n * n;

        }

        /**
         * given a node it returns the node on top of it
         * in the cross of nodes we have to open
         * might return "-1"
         * if node has no top
         * i.e. is part of top row
         *
         * @param k index
         * @return int
         */
        private int top(int k) {


            if (1 <= k && k <= this.gridSize) {
                //node is in top row
                return -1;
            } else {
                return k - this.gridSize;
            }

        }

        /**
         * given a node it returns the node to the left of it
         * in the cross of nodes we have to open
         * might return "-1"
         * if node has no left
         * i.e. is part of left border
         *
         * @param k index
         * @return int
         */
        protected int left(int k) {


            if ((k - 1) % this.gridSize == 0) {
                //node is in left border
                return -1;
            } else {
                return k - 1;
            }

        }


        /**
         * given a node it returns the node under it
         * in the cross of nodes we have to open
         * might return "-1"
         * if node has no bottom
         * i.e. is part of bottom row
         *
         * @param k
         * @return
         */
        private int bottom(int k) {
            if (this.lastNode - this.gridSize < k && k <= this.lastNode) {
                //node is in bottom row
                return -1;
            } else {
                return k + this.gridSize;
            }

        }


        /**
         * given a node it returns the node to the right of it
         * in the cross of nodes we have to open
         * might return "-1"
         * if node has no right
         * i.e. is part of right border
         *
         * @param k
         * @return
         */
        private int right(int k) {
            if (k % this.gridSize == 0) {
                //node is in right border
                return -1;
            } else {
                return k + 1;
            }

        }


        /**
         * Count number of open spaces
         */

        private int getOpenCount() {
            int count = 0;
            for (int i = 1; i <= this.gridSize; i++) {
                for (int j = 1; j <= this.gridSize; j++) {
                    if (this.isOpen(i, j)) {
                        count++;
                    }
                }
            }
            return count;
        }

        private String printGrid() {
            StringBuffer msg = new StringBuffer();

            for (int i = 1; i <= this.gridSize; i++) {
                for (int j = 1; j <= this.gridSize; j++) {
                    if (this.isOpen(i, j)) {
                        msg.append(" o ");
                    } else {
                        msg.append(" - ");
                    }
                }
                msg.append("\n");
            }
            return msg.toString();
        }


    }

    @BeforeClass
    public void setUp() {
        // code that will be invoked when this test is instantiated
        p = new PercolationExtension(2);
    }

    @AfterClass
    public void tearDown() {

    }

    @Test
    public void testOpen() throws Exception {
        Percolation p1 = new Percolation(1);
        Assert.assertFalse(" (1,1) position should be closed", p1.isOpen(1, 1));
        p1.open(1, 1);
        Assert.assertTrue(" (1,1) position should be open by now", p1.isOpen(1, 1));
        Assert.assertTrue(p1.isFull(1, 1));

    }

    @Test(expectedExceptions = IndexOutOfBoundsException.class)
    public void testIndexZero() {
        Percolation p = new Percolation(1);
        p.isOpen(0, 1);
    }

    /**
     * not sure if grid with test size 1 should percolate right away
     * or we need to open the node *
     */
    @Test
    public void testSizeOneSquare() throws Exception {
        Percolation p = new Percolation(1);
        Assert.assertFalse(" (1,1) position should be closed", p.isOpen(1, 1));
        Assert.assertFalse(p.percolates());
        p.open(1, 1);
        Assert.assertTrue(p.percolates());

    }

    @Test
    public void testGetOpenCount() throws Exception {

        Assert.assertTrue(0 == p.getOpenCount());
        p.open(1, 1);
        Assert.assertTrue(1 == p.getOpenCount());
        p.open(2, 2);

        System.out.println("open count" + Integer.valueOf(p.getOpenCount()));
        Assert.assertTrue(2 == p.getOpenCount());
    }

    @Test
    public void testPercolates() throws Exception {
        Percolation p = new Percolation(2);
        p.open(1, 1);
        p.open(2, 1);
        Assert.assertTrue(p.percolates());

    }

    @Test
    public void testNotPercolates() throws Exception {
        Percolation p = new Percolation(2);
        p.open(1, 1);
        Assert.assertFalse(p.percolates());
        p.open(2, 2);
        Assert.assertFalse(p.percolates());
        p.open(2, 1);

        Assert.assertTrue(p.percolates());
    }

    @Test
    public void testNotPercolatesSize4() throws Exception {
        Percolation p = new Percolation(4);
        p.open(1, 1);
        Assert.assertFalse(p.percolates());
        p.open(2, 2);
        Assert.assertFalse(p.percolates());


        p.open(2, 3);
        Assert.assertFalse(p.percolates());
        p.open(4, 1);
        Assert.assertFalse(p.percolates());
        p.open(3, 1);
        Assert.assertFalse(p.percolates());
        p.open(2, 1);
        Assert.assertTrue(p.percolates());
    }

    @Test
    public void testNotPercolatesSize5() throws Exception {
        Percolation p = new Percolation(5);
        p.open(1, 1);
        Assert.assertFalse(p.percolates());
        p.open(2, 2);
        Assert.assertFalse(p.percolates());

        p.open(2, 3);
        Assert.assertFalse(p.percolates());
        p.open(4, 1);
        Assert.assertFalse(p.percolates());
        p.open(3, 1);
        Assert.assertFalse(p.percolates());
        p.open(2, 1);
        Assert.assertFalse(p.percolates());
        p.open(5, 5);
        Assert.assertFalse(p.percolates());
        p.open(5, 1);
        Assert.assertTrue(p.percolates());

    }


    @Test
    public void testTop() throws Exception {
        /**
         * 1->1  2->2
         * 3->3  4->4
         */
        //11 is node 1

        //should be null
        Assert.assertTrue(p.top(1) == -1);
        //12 is node '3', thus top should be 1
        Assert.assertTrue(p.top(3) == 1);
        Assert.assertTrue(p.top(2) == -1);


    }


    @Test
    public void testBottom() throws Exception {

        //11 is node 1
        int bottom = p.bottom(1);
        //should be null
        Assert.assertTrue(bottom == 3);


    }

    @Test
    public void testLeft() throws Exception {

        //11 is node 1
        int left = p.left(1);
        //should be null
        Assert.assertTrue(left == -1);
    }

    @Test
    public void testLeftBiggerGrid() throws Exception {
        PercolationExtension p = new PercolationExtension(6);
        //11 is node 1
        int left = p.left(7);
        //should be null
        Assert.assertTrue(left == -1);
    }

    @Test
    public void testRight() throws Exception {

        //11 is node 1
        int right = p.right(1);
        //should be null
        Assert.assertTrue(right == 2);
    }

    @Test
    public void testIsFull() throws Exception {
        Percolation p = new Percolation(2);
        Assert.assertFalse(p.isFull(1, 1));
        p.open(1, 1);
        Assert.assertFalse(!p.isFull(1, 1));
    }

    @Test
    public void testPercolationStats() {
        PercolationStats ps = new PercolationStats(10, 20);
        System.out.println(ps.mean());

        Assert.assertTrue(ps.mean() < 0.8); //rough estimate
    }

    //test that an exception is thrown if indexes are out of bounds
    @Test(expectedExceptions = IndexOutOfBoundsException.class)
    public void testOutOfBounds() {
        Percolation p = new Percolation(2);
        p.isOpen(3, 3);

    }

    //test that an exception is thrown if indexes are out of bounds
    @Test(expectedExceptions = IndexOutOfBoundsException.class)
    public void testOutOfBounds2() {
        Percolation p = new Percolation(2);
        p.open(3, 3);

    }

    //test that an exception is thrown if indexes are out of bounds
    @Test(expectedExceptions = IndexOutOfBoundsException.class)
    public void testOutOfBounds3() {
        Percolation p = new Percolation(10);
        p.isFull(6, 12);

    }

    @Test
    public void testIsFullBiggerGrid() {
        PercolationExtension p = new PercolationExtension(6);
        Assert.assertFalse(" (1,1) should not be full", p.isFull(1, 1));
        p.open(1, 6);
        p.open(2, 6);
        p.open(3, 6);
        p.open(4, 6);
        p.open(5, 6);
        p.open(5, 5);
        p.open(4, 4);
        p.open(3, 4);
        p.open(2, 4);
        p.open(2, 3);
        p.open(2, 2);


        p.open(2, 1);

        Assert.assertFalse("(2,1) should not be full", p.isFull(2, 1));

        p.open(3, 1);
        p.open(4, 1);
        p.open(5, 1);
        p.open(5, 2);
        p.open(6, 2);
        p.open(5, 4);
        System.out.println(p.printGrid());
        Assert.assertTrue(p.percolates());
    }


    @Test
    public void testInput2() {
        PercolationExtension p = new PercolationExtension(2);
        Assert.assertFalse(" (1,1) should not be full", p.isFull(1, 1));
        p.open(1, 1);

        p.open(2, 2);

        System.out.println(p.printGrid());
        p.open(1, 2);

        System.out.println(p.printGrid());

        Assert.assertTrue(p.percolates());
        Assert.assertTrue(p.isFull(2, 2));
        Assert.assertFalse(p.isFull(2, 1));

    }

}
