/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 10/12/13
 * Time: 2:07 PM
 * To change this template use File | Settings | File Templates.
 */

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.ArrayList;

public class Solver {

    private Board initial;

    private int moves = 0;

    private Solution solution;

    /**
     * // find a solution to the initial board (using the A* algorithm)*
     */
    public Solver(Board initial) {
        this.initial = initial;
        this.solution = Solver.solve(this.initial);
    }


    private static Solution solve(Board initial) {

        Set<String> visited = new HashSet<String>();
        MinPQ<Node> queue = new MinPQ<Node>();
        Node node = new Node(initial);
        Board b = node.getBoard();

        /** other board, crammy solution **/
        Board bT = b.twin();
        Set<String> visitedT = new HashSet<String>();
        MinPQ<Node> queueT = new MinPQ<Node>();
        Node nodeT = new Node(bT);


        int moves = 0;

        Solution solution = new Solution();

        while (!b.isGoal() && !bT.isGoal()) {
            String signature = Solver.boardSignature(b);
            visited.add(signature);
            solution.add(b);

            Iterator<Board> it = b.neighbors().iterator();
            moves++;

            while (it.hasNext()) {
                Board nextBoard = it.next();
                signature = Solver.boardSignature(nextBoard);
                if (!visited.contains(signature)) {

                    queue.insert(new Node(nextBoard, moves, node));

                }
            }


            node = queue.delMin();
            b = node.getBoard();

            ///// now the twin /////////

            signature = Solver.boardSignature(bT);

            visitedT.add(signature);

            Iterator<Board> itT = bT.neighbors().iterator();
            while (itT.hasNext()) {
                Board nextBoard = itT.next();
                signature = Solver.boardSignature(nextBoard);
                if (!visitedT.contains(signature)) {

                    queueT.insert(new Node(nextBoard, moves, nodeT));

                }
            }


            nodeT = queueT.delMin();
            bT = nodeT.getBoard();


        }

        // make sure to include in the solution the goal board
        // if BT is goal solution is false
        if (b.isGoal()) {
            solution.add(b);
            solution.solvable(true);
        }

        return solution;
    }


    /**
     * is the initial board solvable? *
     * To apply the fact, run the A* algorithm
     * simultaneously on two puzzle instances—one
     * with the initial board and one with the initial
     * board modified by swapping a pair of adjacent blocks
     * in the same row. Exactly one of the two will lead to the goal board.
     */
    public boolean isSolvable() {
        //running two boards in the same loop,
        //we really always have to do this
        return this.solution.isSolvable();

    }

    /**
     * min number of moves to solve initial board; -1 if no solution *
     */
    public int moves() {
        return this.solution.moves();
    }

    /**
     * sequence of boards in a shortest solution; null if no solution *
     */
    public Iterable<Board> solution() {
        return this.solution;
    }


    private static String boardSignature(Board b) {

        //
        /**  StringBuffer signature = new StringBuffer();

        for (int i = 0; i < b.dimension(); i++) {
            for (int j = 0; j < b.dimension(); j++) {
                signature.append(b.blocks[i][j]);
            }
        }  **/



        return b.toString().replaceAll("\n","").trim();
    }


    /**
     * solve a slider puzzle (given below) *
     */
    public static void main(String[] args) {
        // create initial board from file
        In in = new In(args[0]);
        int N = in.readInt();
        int[][] blocks = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);
        // let's see if we know how to serialize

        // System.out.println(initial.toString());


        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable()) {
            StdOut.println("No solution possible");
        } else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }


    }


    private static class Node implements Comparable<Node> {

        Board board;
        int moves;
        Node prior;

        public Node(Board b) {
            this.board = b;
            this.prior = null;
            this.moves = 0;
        }

        public Node(Board b, int moves, Node prior) {
            this.board = b;
            this.moves = moves;
            this.prior = prior;
        }

        public Board getBoard() {
            return this.board;
        }

        @Override
        public int compareTo(Node that) {
            return this.board.manhattan() - that.board.manhattan();  //To change body of implemented methods use File | Settings | File Templates.
        }
    }

    /**
     * Seems that we need this class but do we really? *
     */
    private static class Solution implements Iterable<Board> {

        ArrayList<Board> steps;
        boolean solvable = false;

        public Solution() {
            this.steps = new ArrayList<Board>();
        }


        public void add(Board b) {
            this.steps.add(b);
        }

        @Override
        public Iterator<Board> iterator() {
            return this.steps.iterator();
        }

        public int moves() {
            //do not count initial board when counting moves
            return this.steps.size() - 1;
        }

        public boolean isSolvable() {
            return solvable;
        }

        public void solvable(boolean solvable) {
            this.solvable = solvable;
        }
    }

}
