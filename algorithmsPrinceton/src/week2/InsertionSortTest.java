package week2;

import org.testng.annotations.Test;

import org.testng.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/16/13
 * Time: 10:26 PM
 * To change this template use File | Settings | File Templates.
 */
public class InsertionSortTest {

    @Test
    public void testHappyCase() {
        // we assume String implements comparable
        String[] testArray = new String[]{"a", "w", "e", "m", "g", "y"};
        InsertionSort.sort(testArray);
        Assert.assertTrue(testArray[0].equals("a"));
        Assert.assertTrue(testArray[1].equals("e"));
    }

    @Test
    public void testSixIterations() {
        Integer[] l = new Integer[]{34, 64, 16, 81, 59, 15, 72, 47, 58, 37};
        InsertionSort.sort(l);
        Assert.assertTrue(l[0].equals(15));
        Assert.assertTrue(l[1].equals(16));

    }
}
