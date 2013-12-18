import org.testng.annotations.Test;
import junit.framework.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.AfterClass;

import java.util.ArrayList;
import java.lang.Iterable;
import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 10/12/13
 * Time: 2:34 PM
 * To change this template use File | Settings | File Templates.
 */
public class BoardTest {
    int[][] blocks = new int[3][3];

    @BeforeClass
    public void setUp() {
        blocks[0][0] = 0;
        blocks[0][1] = 1;
        blocks[0][2] = 3;
        blocks[1][0] = 4;
        blocks[1][1] = 2;
        blocks[1][2] = 5;
        blocks[2][0] = 7;
        blocks[2][1] = 8;
        blocks[2][2] = 6;
    }

    //@Test
    public void testDistances() throws Exception {
        Board b = new Board(this.blocks);
        Assert.assertEquals(b.hamming(), 4);
        int[][] blocks2 = new int[3][3];
        blocks2[0][0] = 8;
        blocks2[0][1] = 1;
        blocks2[0][2] = 3;
        blocks2[1][0] = 4;
        blocks2[1][1] = 0;
        blocks2[1][2] = 2;
        blocks2[2][0] = 7;
        blocks2[2][1] = 6;
        blocks2[2][2] = 5;
        Board b2 = new Board(blocks2);
        Assert.assertEquals(b2.hamming(), 5);
        Assert.assertEquals(b2.manhattan(), 10);
    }

    @Test
    public void testNeighbors() throws Exception {

        /** Moving the original board should return
         *
         4 1 3
         0 2 5
         7 8 6

         1 0 3
         4 2 5
         7 8 6
         **/
        Board b = new Board(this.blocks);
        Iterable<Board> neighbors = b.neighbors();

        Iterator it = neighbors.iterator();
        System.out.println("****");
        //board has only two neighbors
        Assert.assertTrue(it.hasNext());
        Board board = (Board) it.next();

        int corner = board.blocks[0][0];

        Assert.assertTrue(corner == 4);

        // System.out.println(it.next().toString());
        Assert.assertTrue(it.hasNext());
        board = (Board) it.next();
        corner = board.blocks[0][0];

        Assert.assertTrue(corner == 1);
        //System.out.println(it.next().toString());
        Assert.assertFalse(it.hasNext());


    }

    @Test
    public void testFourPossibilities() {
        int[][] blocks3 = new int[3][3];
        blocks3[0][0] = 1;
        blocks3[0][1] = 2;
        blocks3[0][2] = 3;
        blocks3[1][0] = 4;
        blocks3[1][1] = 0;
        blocks3[1][2] = 5;
        blocks3[2][0] = 6;
        blocks3[2][1] = 7;
        blocks3[2][2] = 8;


        Board b = new Board(blocks3);
        Iterable<Board> neighbors = b.neighbors();

        Iterator<Board> it = neighbors.iterator();

        /**
         * 1 2 3
         * 4 0 5
         * 6 7 8
         * should have 4 neighbourghs
         */
        for (int i = 0; i < 4; i++) {
            Assert.assertTrue(it.hasNext());
            Board board = it.next();
            System.out.println(board);
        }


    }
}
