/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author spd
 */
public class GridReader1 {

    private List<Grid> grids = new ArrayList<Grid>(500);

    public GridReader1(String filename) throws Exception {
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            Grid grid;
            while ((grid = getNextFrom(br)) != null) {
                grids.add(grid);
            }
            br.close();
        } catch (IOException ex) {
            Logger.getLogger(GridReader1.class.getName()).log(Level.SEVERE, null, ex);
            throw ex;
        }
    }

    private Grid getNextFrom(BufferedReader br) throws IOException {
        // TODO some sanity checks
        String line = br.readLine();
        return line == null ? null : new Grid(line);
    }

    public List<Grid> getGrids() {
        return grids;
    }
}
