package week4;

import org.testng.annotations.Test;
import junit.framework.Assert;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/29/13
 * Time: 1:51 PM
 * To change this template use File | Settings | File Templates.
 */
public class HeapsortTest {
    @Test
    public void testFirstpass() {
        Integer[] a = new Integer[]{9, 8, 3, 6, 5, 4, 3};

        Heapsort.sort(a);
        System.out.println(HeapsortTest._toString(a));
    }

    private static String _toString(Comparable[] a) {
        StringBuffer sb = new StringBuffer();
        sb.append("{");
        for (int i = 0; i < a.length; i++) {
            sb.append(" " + i + "=>" + a[i] + ",");

        }
        sb.append("}");
        return sb.toString();
    }
}
