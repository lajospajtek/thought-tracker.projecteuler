/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

/**
 *
 * @author spd
 */
public class Cell {

    protected char c = '0';
    //protected Set<Character> cdd = new TreeSet<Character>(Arrays.asList('1', '2', '3', '4', '5', '6', '7', '8', '9'));
    //protected Set<Character> removed = new HashSet<Character>();
    protected int[] cddo = new int[Grid.SIZ + 1];
    protected int[] remo = new int[Grid.SIZ + 1];
    protected int candidates = 9;

    public Cell(char c) {
        this.c = c;
        cddo[0] = 0;
        for (int i = 1; i <= Grid.SIZ; ++i) {
            cddo[i] = 1;
        }
    }

    public boolean isEmpty() {
        return true;
    }

    public char getDigit() {
        return c;
    }

    public void setDigit(char c) {
        this.c = c;
    }

    public void addCandidate(char c) {
        //cdd.add(c);
        if (cddo[c - '0'] == 0) {
            ++candidates;
            cddo[c - '0'] = 1;
        }
    }

    public void removeCandidate(char c) {
        //cdd.remove(c);
        if (cddo[c - '0'] == 1) {
            --candidates;
            cddo[c - '0'] = 0;
        }
    }

    public boolean tryRemoveCandidate(char c) {
        if (cddo[c - '0'] == 1) {
            cddo[c - '0'] = 0;
            //removed.add(c);
            remo[c - '0'] = 1;
            --candidates;
        }
        return 0 != candidates;
    }

    public void restoreCandidate(char c) {
        //if (removed.remove(c)) {
        if (remo[c - '0'] == 1) {
            remo[c - '0'] = 0;
            //cdd.add(c);
            cddo[c - '0'] = 1;
            ++candidates;
        }
    }

    public List<Character> getCandidates() {
        List<Character> l = new ArrayList<Character>();
        for (int i = 1; i < 10; ++i) {
            if (cddo[i] == 1) {
                l.add((char) ('0' + i));
            }
        }
        return l;
    }

    public int candidates() {
        return candidates;
    }

    public String cToString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i : cddo) {
            if (i != 0) {
                sb.append('0' + i);
            }
        }
        sb.append(']');
        return sb.toString();
    }
}
