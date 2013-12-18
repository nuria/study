/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/19/13
 * Time: 1:35 PM
 * To change this template use File | Settings | File Templates.
 */
public class Shuffle {


    public static void shuffle(Object[] a) {

        /** go through array, pick 'r'
         * between 0 and i-1 , swap i with r
         * **/
        for (int j = 0; j < a.length; j++) {
            int r = StdRandom.uniform(j - 1);
            Object tmp = a[(int) r];
            a[r] = a[j];
            a[j] = tmp;
        }
    }
}
