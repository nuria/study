package week1;

import java.util.Arrays;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/26/13
 * Time: 8:45 AM
 * To change this template use File | Settings | File Templates.
 */
public class BinarySearch {


    /**
     * Using binary search finds a number in a sorted set,
     * returns false if not found
     *
     * @param n
     * @return
     */
    public static boolean find(int[] set, int n) {
        //break input in half each time
        int half = set.length / 2; //does this round?


        if (set.length == 1) {

            if (set[0] == n) {
                return true;
            } else {
                return false;
            }
        }
        if (n < set[half]) {
            return find(Arrays.copyOfRange(set, 0, half), n);
        } else if (n > set[half]) {
            return find(Arrays.copyOfRange(set, half, set.length - 1), n);
        } else {
            return true;
        }

    }
}
