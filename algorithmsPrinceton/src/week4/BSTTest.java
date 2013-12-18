package week4;

import org.testng.annotations.Test;
import junit.framework.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 10/5/13
 * Time: 9:32 AM
 * To change this template use File | Settings | File Templates.
 */
public class BSTTest {
    @Test
    public void testPut() throws Exception {


        BST bst = new BST<Integer, Integer>();
        bst.put(5, 5);
        System.out.println(bst.toString());
        Assert.assertTrue(bst.get(5).equals(5));
        bst.put(2, 2);
        System.out.println(bst.toString());
        bst.put(4, 4);
        bst.put(6, 6);
        System.out.println(bst.toString());
        Assert.assertTrue(bst.get(6).equals(6));
        bst.put(3, 3);
        System.out.println(bst.toString());


    }


    @Test
    public void testFloor() throws Exception {
        BST bst = new BST<Integer, Integer>();
        bst.put(5, 5);
        Assert.assertTrue(bst.get(5).equals(5));
        bst.put(6, 6);
        Assert.assertTrue(bst.floor(5).equals(5));
        Assert.assertTrue(bst.floor(6).equals(6));
        Assert.assertTrue(bst.floor(7).equals(6));
    }

    @Test
    public void testRank() throws Exception {
        BST bst = new BST<Integer, Integer>();
        bst.put(5, 5);
        Assert.assertTrue(bst.get(5).equals(5));
        bst.put(6, 6);
        //   System.out.println(bst.toString());
        bst.put(7, 7);
        bst.put(4, 4);
        bst.put(3, 3);
        System.out.println(bst.toString());

        Assert.assertTrue(bst.rank(5) == 2);
        System.out.println(bst.rank(7));
        Assert.assertTrue(bst.rank(7) == 4);
        Assert.assertTrue(bst.rank(2) == 0);
    }
}
