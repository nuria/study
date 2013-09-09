

/**
 * How to check if system percolates?
 * It does if nodes from the bottom and nodes from the top
 * are in the same component.i.e. they are connected
 * But that would be inefficient
 * We create some virtual node on the top and another node on the botton
 * and see if those two nodes are connected.
 * <p/>
 * To open a site we connect it to all its adjacent sites.
 * <p/>
 * We initialize a grid of 5 by 5 to have 25 nodes, if we start at zero it will
 * have 24 nodes.
 */
public class PercolationStats {

    private double[] thresholds;
    private double mean;
    private double stddev;
    private double coL;
    private double coH;


    /**
     * perform T independent computational experiments on an N-by-N grid
     * each experiment opens random sites until system percolates
     *
     * @param N gridSize
     * @param T numberOftimesExpRuns
     */
    public PercolationStats(final int N, final int T) {


        if (N <= 0 || T <= 0) {
            throw new java.lang.IllegalArgumentException();
        }


        thresholds = new double[T];

        for (int k = 0; k < T; k++) {

            Percolation p = new Percolation(N);
            int openSpaces = 0;
            while (!p.percolates()) {

                p.open(StdRandom.uniform(1, N + 1), StdRandom.uniform(1, N + 1));


            }
            //threshold
            thresholds[k] = openSpaces / N * N;

        }

        //debug, printing thresholds
        for (double threshold : thresholds) {
            System.out.print(threshold);

        }

        System.out.println("___");

        this.mean = StdStats.mean(thresholds);
        this.stddev = StdStats.stddev(thresholds);
        this.coL = this.mean - 1.96 * this.stddev / Math.sqrt(T);
        this.coH = this.mean + 1.96 * this.stddev / Math.sqrt(T);

    }

    /**
     * sample mean of percolation threshold
     *
     * @return double
     */
    public double mean() {
        return this.mean;
    }

    /**
     * sample standard deviation of percolation threshold
     *
     * @return double
     */
    public double stddev() {
        return this.stddev;
    }

    /**
     * returns lower bound of the 95% confidence interval
     *
     * @return double
     */
    public double confidenceLo() {
        return this.coL;
    }

    /**
     * returns upper bound of the 95%
     * confidence interval
     *
     * @return Double
     */
    public double confidenceHi() {
        return this.coH;
    }


    /**
     * @param args
     */
    public static void main(final String[] args) {

        final int N = Integer.parseInt(args[0]);
        final int T = Integer.parseInt(args[1]);

        PercolationStats ps = new PercolationStats(N, T);

        System.out.println("mean                   =" + Double.valueOf(ps.mean()));
        System.out.println("stddev                 =" + Double.valueOf(ps.stddev()));
        System.out.println("5% confidence interval =" + Double.valueOf(ps.confidenceLo()) + "," + Double.valueOf(ps.confidenceHi()));
    }


}
