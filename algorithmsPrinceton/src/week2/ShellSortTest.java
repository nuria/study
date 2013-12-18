package week2;

import org.testng.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/18/13
 * Time: 7:58 PM
 * To change this template use File | Settings | File Templates.
 */
public class ShellSortTest {

    @org.testng.annotations.Test
    public void testHappyCase() {
        String[] a = new String[]{"6", "8", "91", "111", "43", "718", "9", "3", "1", "2", "55", "34", "23", "78", "12", "11", "22", "20", "90", "123", "25"};
        ShellSort.sort(a);

        for (String s : a) {
            // System.out.println(s);
        }
        Assert.assertTrue(a[0].equals("1"));
        Assert.assertTrue(a[a.length - 2].equals("90"));
        Assert.assertTrue(a[a.length - 1].equals("91"));

    }
}
