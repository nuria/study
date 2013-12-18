package week4;

import org.testng.annotations.Test;
import junit.framework.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/29/13
 * Time: 12:21 PM
 * To change this template use File | Settings | File Templates.
 */
public class MaxPQTest {

    @Test
    public void TestIsEmptyHappyCase() {
        MaxPQ<Integer> maxh = new MaxPQ<Integer>(10);
        Assert.assertTrue(maxh.isEmpty());
        maxh.insert(10);
        maxh.insert(9);
        Assert.assertTrue(!maxh.isEmpty());
        maxh.delMax();
        maxh.delMax();
        Assert.assertTrue(maxh.isEmpty());

    }

    @Test
    public void TestMaxHappyCase() {
        MaxPQ<Integer> maxh = new MaxPQ<Integer>(10);
        Assert.assertTrue(maxh.isEmpty());
        maxh.insert(10);
        maxh.insert(9);
        Assert.assertTrue("Max should be 10", maxh.delMax() == 10);
        Assert.assertTrue("Max should be 9", maxh.delMax() == 9);
        Assert.assertTrue(maxh.isEmpty());

    }

    @Test
    public void testSequence() {
        MaxPQ<Integer> maxh = new MaxPQ<Integer>(10);
        maxh.insert(86);
        maxh.insert(69);
        maxh.insert(72);
        maxh.insert(42);
        maxh.insert(63);
        maxh.insert(43);
        maxh.insert(46);
        maxh.insert(40);
        maxh.insert(27);
        maxh.insert(50);
        maxh.delMax();
        maxh.delMax();
        maxh.delMax();
        System.out.println(maxh.toString());
    }
}
