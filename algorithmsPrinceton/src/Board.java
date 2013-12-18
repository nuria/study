

import java.util.ArrayList;


/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 10/12/13
 * Time: 2:07 PM
 * To change this template use File | Settings | File Templates.
 */
public class Board {

    /**
     * construct a board from an N-by-N array of blocks
     * (where blocks[i][j] = block in row i, column j)
     * Note that we are starting index 0 unlike a matrix
     */

    private int[][] blocks;

    //stores the position of every element in the solution like:
    // 1->(0,0)
    //2 ->(0,1)
    private Object[] solution;

    private int N;


    public Board(int[][] blocks) {
        this.blocks = blocks;
        // do we need to recalculate dimension here?
        N = blocks.length;
        int largest = blocks.length * blocks.length;

        // we need to find the solution to compare indexes for hamming distance
        solution = new Object[largest + 1]; //for easiness

        int i = 0;
        int j = 0;

        for (int n = 1; n < largest; n++) {
            solution[n] = new int[]{i, j};
            if (j == N - 1) {
                i++;
                j = 0;
            } else {
                j++;
            }

        }
        //last element
        solution[largest] = new int[]{0, 0};

        /**   for (int n=1;n <=largest;n++){
         int[] item = (int[])solution[n];
         System.out.println(n+" ->  "+item[0]+" ,"+item[1]);

         }  **/
    }

    /**
     * board dimension N   *
     */
    public int dimension() {
        return blocks.length;
    }

    /**
     * Number of blocks out of place
     * Map blocks to an array of length N*N
     * Every value!= key is counts one towards the distance
     * O(n) in time if we do it w/o additional array
     * <p/>
     * If we serialize board to an array we can count the number of inversions in
     * *
     */
    public int hamming() {
        int distance = 0;
        int N = this.dimension();

        int position = 1;

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {

                if (blocks[i][j] != position && blocks[i][j] != 0) { //open space does not count
                    distance = distance + 1;
                }
                //last position is zero
                if (i == N - 1 && j == N - 2) {
                    position = 0;
                } else {
                    position++;
                }

            }

        }

        return distance;
    }

    /**
     * sum of Manhattan distances between blocks and goal *
     * We need to know what is the solution matrix or rather, given a value
     * we need to be able to locate its indexes on the right position.
     * Once we have its indexes we substract them with the indexes of the position
     * the item is at
     */
    public int manhattan() {
        int distance = 0;
        int N = this.dimension();

        int position = 1;

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {

                if (blocks[i][j] != position && blocks[i][j] != 0) { //open space does not count
                    //position is wrong, calculate manhattan distance via solution array
                    int[] tuple = (int[]) this.solution[blocks[i][j]];
                    distance = distance + Math.abs(tuple[0] - i) + Math.abs(tuple[1] - j);
                }
                //last postion is zero
                if (i == N - 1 && j == N - 2) {
                    position = 0;
                } else {
                    position++;
                }

            }

        }

        return distance;
    }

    /**
     * Is this board the goal board? *
     */
    public boolean isGoal() {

        return this.hamming() == 0;
    }

    /**
     * a board obtained by exchanging two adjacent blocks in the same row *
     */
    public Board twin() {
        //TODO make sure they are not white blocks
        Board b = swap(new int[]{1, 0}, new int[]{1, 1});
        //System.out.println(b.toString());
        return b;
    }


    /**
     * Return a board in which values at position 1 and 2 are swapped
     *
     * @param p1 (i,j)
     * @param p2 (i',j')
     * @return
     */
    private Board swap(int[] p1, int[] p2) {
        int N = this.blocks.length;
        int[][] twin = new int[this.blocks.length][this.blocks.length];


        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                twin[i][j] = this.blocks[i][j];
            }
        }

        int tmp = twin[p1[0]][p1[1]];
        twin[p1[0]][p1[1]] = twin[p2[0]][p2[1]];
        twin[p2[0]][p2[1]] = tmp;
        return new Board(twin);
    }

    /**
     * Does this board equal y?  *
     */
    public boolean equals(Object y) {
        // loop through the board and make sure they are not the same
        Board that = (Board) y;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (this.blocks[i][j] != that.blocks[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }


    /**
     * For a given Board, the neighbors() method needs to compute all the Board's neighbors.
     * To be clear the neighbors of a given Board are the Boards that can be reached
     * from the given Board by moving one tile. Depending on where the empty tile is,
     * a Board may have between 2 and 4 neighbors.
     */
    public Iterable<Board> neighbors() {

        ArrayList<Board> neighbors = new ArrayList<Board>();

        // swap with blank tile
        // we know i [row index] and j [column index]
        // are between 0 and N-1
        int blankC = -1;   // index of the column where the blank is at
        int blankR = -1;  // index of the row where the blank is at

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (this.blocks[i][j] == 0) {
                    blankC = j;
                    blankR = i;
                    break;
                }
            }
        }

        //up
        if (blankR - 1 >= 0) {
            neighbors.add(this.swap(new int[]{blankR, blankC}, new int[]{blankR - 1, blankC}));
        }
        //down
        if (blankR + 1 < N) {
            Board b = this.swap(new int[]{blankR, blankC}, new int[]{blankR + 1, blankC});
            neighbors.add(b);
        }
        //left
        if (blankC - 1 >= 0) {

            neighbors.add(this.swap(new int[]{blankR, blankC}, new int[]{blankR, blankC - 1}));
        }
        //right
        if (blankC + 1 < N) {
            Board b = this.swap(new int[]{blankR, blankC}, new int[]{blankR, blankC + 1});
            neighbors.add(this.swap(new int[]{blankR, blankC}, new int[]{blankR, blankC + 1}));
            //  System.out.println(neighbors.get(neighbors.size()-1));
        }
        return neighbors;
    }

    /**
     * The input and output format for a board is the board dimension N followed
     * by the N-by-N initial board, using 0 to represent the blank square. As an example, *
     */
    public String toString() {
        int N = this.dimension();
        StringBuffer sb = new StringBuffer();
        sb.append(N);
        sb.append("\n");
        for (int i = 0; i < N; i++) {
            sb.append(" ");
            for (int j = 0; j < N; j++) {
                sb.append(String.format("%2d ", this.blocks[i][j]));
            }
            sb.append("\n");
        }

        return sb.toString();
    }

}
