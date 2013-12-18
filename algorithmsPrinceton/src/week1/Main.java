package week1;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 8/23/13
 * Time: 2:56 PM
 * To change this template use File | Settings | File Templates.
 */

import java.io.*;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Main {

    private static Pattern whiteSpacePattern = Pattern.compile("//s+");


    public static void main(String[] args) throws IOException {

        String filename = "/workplace/study/algorithmsPrinceton/res/input.txt";
        StringBuilder txt = new StringBuilder();

        String NL = System.getProperty("line.separator");
        Scanner s;
        try {
            s = new Scanner(new FileInputStream(filename));
            // first number is the number of nodes

            int numItems = readInts(s.nextLine())[0];

            QuickFind uf = new QuickFind(numItems);

            while (s.hasNextLine()) {

                int[] numbers = readInts(s.nextLine());
                uf.union(numbers[0], numbers[1]);

            }
            s.close();
            log(txt.toString());
            log("\n");
        } catch (FileNotFoundException e) {
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        }

    }

    private static void log(String msg) {
        System.out.println(msg);
    }


    private static int[] readInts(String s) {
        //split by spaces and return an array of int[]
        String[] numbersRaw = s.trim().split("/s+");
        int[] numbers = new int[numbersRaw.length];

        for (int i = 0; i < numbersRaw.length; i++) {
            numbers[i] = Integer.parseInt(numbersRaw[i]);
        }

        return numbers;
    }
}
