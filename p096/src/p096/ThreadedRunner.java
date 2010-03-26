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
import java.util.concurrent.PriorityBlockingQueue;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author spd
 */
public class ThreadedRunner {

    private String END = "__END__";
    private int cores;
    private final BlockingQueue<IndexedLine> solverQueue;
    private final BlockingQueue<IndexedLine> printerQueue;
    private final ExecutorService inputReader, solverService;

    public ThreadedRunner() {
        cores = Runtime.getRuntime().availableProcessors();
        solverQueue = new LinkedBlockingQueue<IndexedLine>(2 * cores);
        printerQueue = new PriorityBlockingQueue<IndexedLine>();
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
            int i = 0;
            while (true) {
                IndexedLine il = printerQueue.take();
                if (il.getIndex() != i) {
                    printerQueue.put(il);
                    Thread.sleep(100);
                    continue;
                }
                ++i;
                String line = il.getLine();
                sw.println(line);
                System.out.println(il.getIndex() + " : " + line);
            }
        } catch (InterruptedException ignored) {
        }
        sw.close();
    }

    class IndexedLine implements Comparable {

        protected int index;
        protected String line;

        public IndexedLine(int index, String line) {
            this.index = index;
            this.line = line;
        }

        public int getIndex() {
            return index;
        }

        public String getLine() {
            return line;
        }

        public void setLine(String line) {
            this.line = line;
        }
        
        public int compareTo(Object o) {
            if (!(o instanceof IndexedLine)) {
                throw new UnsupportedOperationException("IndexedLine instance expected");
            }
            IndexedLine il = (IndexedLine)o;
            return index - il.index;
        }

    }

    class GridReader implements Runnable {

        private BlockingQueue<IndexedLine> solverQueue;
        private Thread thread;

        public GridReader(BlockingQueue<IndexedLine> solverQueue) {
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
                        solverQueue.put(new IndexedLine(i, line));
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

        private BlockingQueue<IndexedLine> solverQueue;
        private BlockingQueue<IndexedLine> printerQueue;
        private Thread thread;

        public Solver(BlockingQueue<IndexedLine> solverQueue, BlockingQueue<IndexedLine> printerQueue) {
            this.solverQueue = solverQueue;
            this.printerQueue = printerQueue;
        }

        @Override
        public void run() {
            thread = Thread.currentThread();
            while (!thread.isInterrupted()) {
                try {
                    IndexedLine il = solverQueue.take();
                    String line = il.getLine();
                    if (line == END) { // object identity, not equality
                        printerQueue.put(new IndexedLine(0, END));
                        break;
                    }
                    Grid grid = new Grid(line);
                    String pzl = grid.toLine();
                    grid.findAllCandidates();
                    grid.solve();
                    String psol = grid.toLine();
                    il.setLine(psol);
                    printerQueue.put(il);
                } catch (InterruptedException ignored) {
                    thread.interrupt();
                    break;
                }
            }
        }
    }
}
