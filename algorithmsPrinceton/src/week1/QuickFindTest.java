package week1;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/24/13
 * Time: 11:30 PM
 * To change this template use File | Settings | File Templates.
 */
public class QuickFindTest {

    QuickFind qf;

    @BeforeMethod
    public void setUp() throws Exception {
        qf = new QuickFind(10);

    }

    @Test
    public void testConnected() throws Exception {
        qf.union(0, 5);
        qf.union(7, 0);
        qf.union(6, 8);
        qf.union(5, 2);
        qf.union(1, 9);
        qf.union(9, 6);

        System.out.println(qf);
        Assert.assertTrue(qf.connected(0, 5));


    }

    @Test
    public void testUnion() throws Exception {

    }
}
