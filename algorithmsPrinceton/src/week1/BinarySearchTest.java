package week1;

import junit.framework.Assert;
import org.testng.annotations.Test;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/26/13
 * Time: 9:01 AM
 * To change this template use File | Settings | File Templates.
 */
public class BinarySearchTest {
    @Test
    public void testFind() throws Exception {

        int[] testArray = new int[]{1, 2, 11, 12, 34, 45, 134};
        Assert.assertFalse(BinarySearch.find(testArray, 0));
        Assert.assertTrue(BinarySearch.find(testArray, 1));

    }
}
