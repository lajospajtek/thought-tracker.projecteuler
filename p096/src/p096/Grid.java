/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

/**
 *
 * @author spd
 */
public class Grid {

    public static int SIZ = 9;
    private String name;
    private Cell grid[][] = new Cell[SIZ][SIZ];
    int fixed = SIZ * SIZ;

    public Grid(String line) {
        name = "Unnamed";
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                char c = line.charAt(i * SIZ + j);
                if (!Character.isDigit(c)) c = '0';
                grid[i][j] = new Cell(c);
            }
        }
    }

    public Grid(String name, String[] lines) {
        this.name = name;
        int i = 0;
        for (String line : lines) {
            for (int j = 0; j < line.length(); ++j) {
                grid[i][j] = new Cell(line.charAt(j));
            }
            ++i;
        }
    }

    public Cell cellAt(int i, int j) {
        return grid[i][j];
    }

    public String getName() {
        return name;
    }

    public void findAllCandidates() {
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                if (grid[i][j].getDigit() == '0') {
                    findCandidates(i, j);
                    --fixed;
                }
            }
        }
    }

    public void findCandidates(int i, int j) {
        Cell crt = grid[i][j];
        for (int ii = 0; ii < SIZ; ++ii) {
            char c = grid[ii][j].getDigit();
            if (c != '0') {
                crt.removeCandidate(c);
            }
        }
        for (int jj = 0; jj < SIZ; ++jj) {
            char c = grid[i][jj].getDigit();
            if (c != '0') {
                crt.removeCandidate(c);
            }
        }
        int bi = (i / 3) * 3;
        int bj = (j / 3) * 3;
        for (int ii = 0; ii < 3; ++ii) {
            for (int jj = 0; jj < 3; ++jj) {
                char c = grid[bi + ii][bj + jj].getDigit();
                if (c != '0') {
                    crt.removeCandidate(c);
                }
            }
        }
    }

    public boolean solve() {
        // find the first cell with least number fo candidates,
        // start/continue solving from there
        int min = Integer.MAX_VALUE;
        int mi = 0, mj = 0;
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                if (grid[i][j].getDigit() != '0') {
                    continue;
                }
                int cm = grid[i][j].getCandidates().size();
                if (cm < 0) {
                    System.exit(1);
                }
                if (cm < min) {
                    mi = i;
                    mj = j;
                    min = cm;
                }
            }
        }
        if (min != Integer.MAX_VALUE) {
            return checkCandidates(mi, mj);
        } else {
            return false;
        }
    }

    private boolean checkCandidates(int i, int j) {
        Cell crt = grid[i][j];
        char c = crt.getDigit();
        if (c == '0') {
            for (char cd : crt.getCandidates()) {
                crt.setDigit(cd);
                ++fixed;
                //if (fixed == SIZ*SIZ) return true;
                boolean ok = true;
                for (int ii = 0; ii < SIZ; ++ii) {
                    if (ii == i) {
                        continue;
                    }
                    ok &= (cd != grid[ii][j].getDigit());
                }
                //for (int ii = i+1; ii < SIZ; ++ii) {
                for (int ii = 0; ok && ii < SIZ; ++ii) {
                    Cell cc = grid[ii][j];
//                    System.out.println("i: " + ii + ", j: " + j + ", ch:" + cc.getDigit());
                    if (cc.getDigit() == '0') {
                        ok &= cc.tryRemoveCandidate(cd);
                    }
                }
                for (int jj = 0; ok && jj < SIZ; ++jj) {
                    if (jj == j) {
                        continue;
                    }
                    ok &= (cd != grid[i][jj].getDigit());
                }
                //for (int jj = j+1; jj < SIZ; ++jj) {
                for (int jj = 0; ok && jj < SIZ; ++jj) {
                    Cell cc = grid[i][jj];
                    //System.out.println("i: " + i + ", j: " + jj + ", ch:" + cc.getDigit());
                    if (cc.getDigit() == '0') {
                        ok &= cc.tryRemoveCandidate(cd);
                    }
                }
                // integrity check for the 3x3 sub-grid
                int bi = (i / 3) * 3;
                int bj = (j / 3) * 3;
                for (int ii = 0; ok && ii < 3; ++ii) {
                    if (i == bi+ii) continue;
                    for (int jj = 0; jj < 3; ++jj) {
                        if (j == bj+jj) continue;
                        Cell cc = grid[bi + ii][bj + jj];
                        ok &= (cd != cc.getDigit());
                    }
                }


                for (int ii = 0; ok && ii < 3; ++ii) {
                    for (int jj = 0; jj < 3; ++jj) {
                        Cell cc = grid[bi + ii][bj + jj];
                        if (cc.getDigit() == '0') {
                            ok &= cc.tryRemoveCandidate(cd);
                        }
                    }
                }

                //System.out.print("selecting from: [" + i + "," + j + "]:" + cd + "\n" + toString2());
                // TODO: tune this: is fixed needed at all?
                if (ok) {
                    if (fixed == SIZ * SIZ) {
                        //System.out.print("\n" + toString2());
                        return true;
                    }
                    if (solve()) {
                        return true;
                    }
                } else {
                    //System.out.println("- backtrack");
                }
                crt.setDigit('0');
                --fixed;

                for (int ii = 0; ii < SIZ; ++ii) {
                    Cell cc = grid[ii][j];
                    if (cc.getDigit() == '0') {
                        cc.restoreCandidate(cd);
                    }
                }
                for (int jj = 0; jj < SIZ; ++jj) {
                    Cell cc = grid[i][jj];
                    if (cc.getDigit() == '0') {
                        cc.restoreCandidate(cd);
                    }
                }
                for (int ii = 0; ii < 3; ++ii) {
                    for (int jj = 0; jj < 3; ++jj) {
                        Cell cc = grid[bi + ii][bj + jj];
                        if (cc.getDigit() == '0') {
                            cc.restoreCandidate(cd);
                        }
                    }
                }
                //System.out.print(toString2());
            }
        } else {
            //System.out.println("Skipping " + i + ", " + j);
        }
        return false;
    }

    public int getP96Id() {
        int id = 100 * (grid[0][0].getDigit() - '0');
        id += 10 * (grid[0][1].getDigit() - '0');
        id += (grid[0][2].getDigit() - '0');
        return id;
    }

    public String toLine() {
        StringBuilder sb = new StringBuilder(SIZ*SIZ);
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                sb.append(grid[i][j].getDigit());
            }
        }
        return sb.toString();
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(name).append('\n');
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                sb.append('(').append(grid[i][j].getDigit()).append(')');
            }
            sb.append('\n');
        }
        return sb.toString();
    }

    public String toString2() {
        StringBuilder sb = new StringBuilder();
        sb.append(name).append('\n');
        for (int i = 0; i < SIZ; ++i) {
            for (int j = 0; j < SIZ; ++j) {
                char c = grid[i][j].getDigit();
                if (c == '0') {
                    sb.append(grid[i][j].cToString());
                } else {
                    sb.append('(').append(c).append(')');
                }
            }
            sb.append('\n');
        }
        return sb.toString();
    }

    public String toGid() {
        StringBuilder sb = new StringBuilder(SIZ*(4+SIZ));
        for (int i = 0; i < SIZ; ++i) {
            if (i%3==0) sb.append("------+------+------\n");
            for (int j = 0; j<SIZ; ++j) {
                if (j!=0 && j%3==0) sb.append('|');
                char c = grid[i][j].getDigit();
                sb.append(c).append(' ');
            }
            sb.append('\n');
        }
        return sb.toString();
    }
}
