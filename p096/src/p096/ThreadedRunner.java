/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author spd
 */
public class ThreadedRunner {

    private String END = "__END__";
    private int cores;
    private final BlockingQueue<String> solverQueue, printerQueue;
    private final ExecutorService inputReader, solverService;

    public ThreadedRunner() {
        cores = Runtime.getRuntime().availableProcessors();
        solverQueue = new LinkedBlockingQueue<String>(2 * cores);
        printerQueue = new LinkedBlockingQueue<String>();
        inputReader = Executors.newSingleThreadExecutor();
        solverService = Executors.newFixedThreadPool(cores);
    }

    public void go() throws Exception {
        for (int i = 0; i < cores; i++) {
            solverService.submit(new Solver(solverQueue, printerQueue));
        }
        inputReader.submit(new GridReader(solverQueue));

        PrintStream sw = new PrintStream(new FileOutputStream("solver_output.txt"));
        try {
            while (true) {
                String line = solverQueue.take();
                if (line == END) { // object identity, not equality
                    solverQueue.put(END);
                    break;
                }
                sw.println(line);
                System.out.println(line);
            }
        } catch (InterruptedException ignored) {
        }
        sw.close();
    }

    class GridReader implements Runnable {

        private BlockingQueue<String> solverQueue;
        private Thread thread;

        public GridReader(BlockingQueue<String> solverQueue) {
            this.solverQueue = solverQueue;
        }

        @Override
        public void run() {
            thread = Thread.currentThread();
            while (!thread.isInterrupted()) {
                try {
                    BufferedReader br = new BufferedReader(new FileReader("sudoku17"));
                    int i = 0;
                    String line;
                    while ((line = br.readLine()) != null) {
                        solverQueue.put(line);
                        ++i;
                    }
                    br.close();
                } catch (IOException ex) {
                    Logger.getLogger(ThreadedRunner.class.getName()).log(Level.SEVERE, null, ex);
                } catch (InterruptedException ie) {
                    thread.interrupt();
                }

            }
        }
    }

    class Solver implements Runnable {

        private BlockingQueue<String> solverQueue;
        private BlockingQueue<String> printerQueue;
        private Thread thread;

        public Solver(BlockingQueue<String> solverQueue, BlockingQueue<String> printerQueue) {
            this.solverQueue = solverQueue;
            this.printerQueue = printerQueue;
        }

        @Override
        public void run() {
            thread = Thread.currentThread();
            while (!thread.isInterrupted()) {
                try {
                    String line = solverQueue.take();
                    if (line == END) { // object identity, not equality
                        printerQueue.put(END);
                        break;
                    }
                    Grid grid = new Grid(line);
                    String pzl = grid.toLine();
                    grid.findAllCandidates();
                    grid.solve();
                    String psol = grid.toLine();
                    printerQueue.put(psol);
                } catch (InterruptedException ignored) {
                    thread.interrupt();
                    break;
                }
            }

        }
    }
}
