

/**
 * Percolation
 */
public class Percolation {

    private static int OPENED = 1;

    private int gridSize = 0;
    /**
     * translates from i, j to node # in our model,
     * thus grid[1][1]=1   , grid[1][2] = 2, grid[5][5] = 25
     */
    private int[][] grid;
    //grid to kep track what position is opened, not very OO
    // all positions are initialized to zero, which means closed
    private int[][] opened;
    private int lastNode;
    private int firstVirtNode;
    private int lastVirtNode;
    private int ufSize;


    private WeightedQuickUnionUF uf;


    /**
     * create n by n grid with all sites blocked
     *
     * @param n gridSize
     */
    public Percolation(int n) {

        this.gridSize = n;
        //the last node on the grid
        this.lastNode = n * n;
        this.lastVirtNode = this.lastNode + 1;

        // to keep  track of n size grid we need n*n nodes
        //we start at 1

        this.ufSize = n * n + 1;


        // note that the 0 row is unoccuppied, only has virt node
        // last virt node can be found at n+2
        this.grid = new int[n + 1][n + 1];
        this.opened = new int[n + 1][n + 1];

        int k = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                this.grid[i][j] = k;
                k++;
            }
        }


        // to translate from squares in the grid to uf nodes
        // we need to do a lookup on the grid structure
        //since we have added two nodes we add two extra indexes
        uf = new WeightedQuickUnionUF(ufSize);

        // remember we have some virtual nodes we need to initialize
        // to see if top and bottom are connected
        // first row is nodes 1..n
        // last row is nodes n*n-n.. n*n


        /**for (int i=1;i<=n;i++) {
         uf.union(0,i);
         uf.union(this.lastVirtNode,this.lastVirtNode-i);
         } **/

    }


    /**
     * lookup on whether a node is opened
     *
     * @param node index
     * @return boolean
     */
    private boolean innerIsOpen(int node) {
        // if it points to other than himself is open
        // get indexes from node
        int row;
        int column;

        if (node < this.gridSize) {
            column = node;
            row = 1;

        } else {

            int remainder = node % this.gridSize;
            if (remainder != 0) {
                row = (node - remainder) / this.gridSize + 1;
                column = remainder;
            } else {
                row = node / this.gridSize;
                column = this.gridSize;
            }

        }

        return isOpen(row, column);

    }

    /**
     * To open a site we connected to all its adjacent OPEN sites
     * BE CAREFUL!
     *
     * @param i row
     * @param j column
     * @throws java.lang.IndexOutOfBoundsException
     *
     */
    public void open(int i, int j) {


        if (this.isOpen(i, j)) {
            return;
        }

        int node = this.getNode(i, j);

        int top = top(node);
        int bottom = bottom(node);
        int left = left(node);
        int right = right(node);


        int[] arround = new int[]{top, bottom, left, right};



        for (int anArround : arround) {
            if (anArround > 0) {
                if (this.innerIsOpen(anArround)) {
                    uf.union(node, anArround);
                }
            }
        }

        this.opened[i][j] = OPENED;

    }


    /**
     * is site (row i, column j) open?
     *
     * @param i row
     * @param j column
     * @return boolean
     * @throws java.lang.IndexOutOfBoundsException
     *
     */
    public boolean isOpen(int i, int j) {
        this.checkIndex(i);
        this.checkIndex(j);
        return this.opened[i][j] == OPENED;
    }

    // is site (row i, column j) full?

    /**
     * A full site is an open site that can be connected to an open site in the top
     * row via a chain of neighboring (left, right, up, down) open sites.
     * We say the system percolates if there is a full site in the bottom row. In other words, a system percolates
     * if we fill all open sites connected to the top row and that process fills some open site on the bottom row.*
     *
     * @param i row
     * @param j column
     * @return boolean
     * @throws java.lang.IndexOutOfBoundsException
     *
     */
    public boolean isFull(int i, int j) {
        //I *think*  a site must be open to be full
        if (!this.isOpen(i, j)) {
            return false;
        }
        int node = this.getNode(i, j);


        //TODO quadratic solution, improve
        for (int k = 1; k <= this.gridSize; k++) { //all items on the top row
            if (uf.connected(k, node)) {

                return true;
            }
        }

        return false;
    }

    /**
     * Does the system percolate
     *
     * @return boolean
     */
    public boolean percolates() {
        // for 1 size grid if node is open it always percolates
        if (this.gridSize == 1) {
            return this.isOpen(1, 1);
        }
        //TODO quadratic solution improve
        for (int i = 1; i <= this.gridSize; i++) {
            if (this.isFull(this.gridSize, i)) {
                return true;
            }

        }


        return false;
    }

    /**
     * Given the two indexes it returns the node
     *
     * @param i row
     * @param j column
     * @return int
     * @throws java.lang.IndexOutOfBoundsException
     *
     */
    private int getNode(int i, int j) {
        this.checkIndex(i);
        this.checkIndex(j);
        return this.grid[i][j];
    }

    /**
     * @param k index
     * @throws java.lang.IndexOutOfBoundsException
     *
     */
    private void checkIndex(int k) {
        if (k == 0 || k > this.gridSize) {
            throw new IndexOutOfBoundsException("row index " + k + " out of bounds");
        }

    }

    /**
     * given a node it returns the node on top of it
     * in the cross of nodes we have to open
     * might return "-1"
     * if node has no top
     * i.e. is part of top row
     *
     * @param k index
     * @return int
     */
    private int top(int k) {


        if (1 <= k && k <= this.gridSize) {
            //node is in top row
            return -1;
        } else {
            return k - this.gridSize;
        }

    }

    /**
     * given a node it returns the node under it
     * in the cross of nodes we have to open
     * might return "-1"
     * if node has no bottom
     * i.e. is part of bottom row
     *
     * @param k index
     * @return int
     */
    private int bottom(int k) {
        if (this.lastNode - this.gridSize < k && k <= this.lastNode) {
            //node is in bottom row
            return -1;
        } else {
            return k + this.gridSize;
        }

    }

    /**
     * given a node it returns the node to the left of it
     * in the cross of nodes we have to open
     * might return "-1"
     * if node has no left
     * i.e. is part of left border
     *
     * @param k index
     * @return int
     */
    private int left(int k) {


        if ((k - 1) % this.gridSize == 0) {
            //node is in left border
            return -1;
        } else {
            return k - 1;
        }

    }

    /**
     * given a node it returns the node to the right of it
     * in the cross of nodes we have to open
     * might return "-1"
     * if node has no right
     * i.e. is part of right border
     *
     * @param k index
     * @return int
     */
    private int right(int k) {
        if (k % this.gridSize == 0) {
            //node is in right border
            return -1;
        } else {
            return k + 1;
        }

    }

    /**
     * @return String
     */
    private String printUF() {

        StringBuffer msg = new StringBuffer();

        for (int k = 0; k < this.ufSize; k++) {
            if (k > 10) {
                msg.append(k);
            } else {
                msg.append(" " + k);
            }
            msg.append("->" + this.uf.find(k) + " ");

            if (k % this.gridSize == 0) {
                msg.append("\n");
            }
        }
        return msg.toString();
    }

}
