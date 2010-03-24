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
public class GridReader {

    private List<Grid> grids = new ArrayList<Grid>(50);

    public GridReader(String filename) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            Grid grid;
            while ((grid = getNextFrom(br)) != null) {
                grids.add(grid);
            }
        } catch (IOException ex) {
            Logger.getLogger(GridReader.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private Grid getNextFrom(BufferedReader br) throws IOException {
        // TODO some sanity checks
        String name = br.readLine();
        if (name == null) {
            return null;
        }
        String[] lines = new String[Grid.SIZ];
        for (int i = 0; i < Grid.SIZ; ++i) {
            lines[i] = br.readLine();
        }
        return new Grid(name, lines);
    }

    public List<Grid> getGrids() {
        return grids;
    }
}
