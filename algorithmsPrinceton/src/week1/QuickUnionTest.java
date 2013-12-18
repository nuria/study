package week1;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.Assert;
import junit.framework.TestCase;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/23/13
 * Time: 3:21 PM
 * To change this template use File | Settings | File Templates.
 */
public class QuickUnionTest extends TestCase {
    QuickUnion qu;

    @BeforeMethod
    public void setUp() throws Exception {
        qu = new QuickUnion(10);

    }


    @AfterMethod
    public void tearDown() throws Exception {
        qu = null;

    }


    @Test
    public void testConnected() throws Exception {

        qu.union(4, 3);
        Assert.assertTrue(qu.connected(4, 3));
        qu.union(3, 8);
        qu.union(6, 5);
        qu.union(9, 4);
        System.out.println(qu);
        Assert.assertTrue(qu.connected(4, 8));
        qu.union(2, 1);
        qu.union(5, 0);
        qu.union(7, 2);
        qu.union(6, 1);
        qu.union(7, 3);
        System.out.println(qu);

        //should be
        //{6,2,6,4,6,6,6,2,4,4,}
        Assert.assertTrue(qu.connected(7, 0));

    }

    @Test
    public void testConnected2() throws Exception {
        // 2-5 0-1 2-0 6-4 4-9 4-8 6-3 3-0 2-7
        qu.union(2, 5);

        qu.union(0, 1);
        qu.union(2, 0);
        qu.union(6, 4);
        Assert.assertFalse(qu.connected(6, 0));
        Assert.assertTrue(qu.connected(5, 0));
        qu.union(4, 9);
        qu.union(4, 8);
        qu.union(6, 3);
        qu.union(3, 0);
        qu.union(2, 7);
        //System.out.println(">>>");
        //System.out.println(qu);

        //should be
        //{2,0,6,6,6,2,6,6,6,6,}
        Assert.assertTrue(qu.leaders[0] == 2);
        Assert.assertTrue(qu.leaders[1] == 0);
        Assert.assertTrue(qu.leaders[2] == 6);

        Assert.assertTrue(qu.connected(7, 0));

    }

}
