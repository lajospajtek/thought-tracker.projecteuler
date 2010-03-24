/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.PrintStream;

/**
 *
 * @author spd
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws Exception {
        go3();
    }

    public static void go3() throws Exception {
        PrintStream sw = new PrintStream(new FileOutputStream("solver_output.txt"));
        BufferedReader br = new BufferedReader(new FileReader("sudoku17"));
        int i = 0, solved = 0;
        String line;
        while ((line = br.readLine()) != null) {
            Grid grid = new Grid(line);
            String pzl = grid.toLine();
            grid.findAllCandidates();
            grid.solve();
            String psol = grid.toLine();
            System.out.println("Grid: " + i);
            System.out.println(pzl);
            System.out.println(psol);
            sw.println(psol);
            ++i;
        }
        sw.close();
        //br.close();
        //System.out.println("Verified: " + solved + " out of " + i);
    }

    public static void go2() throws Exception {
        PrintStream sw = new PrintStream(new FileOutputStream("solver_output.txt"));
        BufferedReader br = new BufferedReader(new FileReader("solutions.txt"));
        GridReader1 gr = new GridReader1("puzzles.txt");
        int i = 0, solved = 0;
        for (Grid grid : gr.getGrids()) {
            String pzl = grid.toLine();
            grid.findAllCandidates();
            grid.solve();
            String psol = grid.toLine();
            String csol = br.readLine();
            ++i;
            if (psol.equals(csol)) ++solved;
            //System.out.println("Grid: " + i + ": " + (psol.equals(csol) ? "OK":"NOK"));
            //System.out.println(psol);
            sw.println(psol);
        }
        sw.close();
        br.close();
        System.out.println("Verified: " + solved + " out of " + i);
    }

    public static void go1() {
        GridReader gr = new GridReader("sudoku.txt");
        int sum = 0;
        for (Grid grid : gr.getGrids()) {
            //System.out.print(grid);
            grid.findAllCandidates();
            //System.out.print(grid.toString2());
            grid.solve();
            //System.out.print(grid.toString2());
            int pid = grid.getP96Id();
            sum += pid;
            //System.out.println("pid: " + pid);
            System.out.println(pid);
        }
        System.out.println("sum: " + sum + ((sum == 24702)?" (OK)":" (NOT OK)"));

/*        Grid grid = gr.getGrids().get(0);
        System.out.print(grid);
        grid.findAllCandidates();
        System.out.print(grid.toString2());
        System.out.println(grid.getP96Id());
        grid.solve(0,0);
        System.out.println("p096 id:" + grid.getP96Id());
        System.out.print(grid.toString2());
*/
    }
}
