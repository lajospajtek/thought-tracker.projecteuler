/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p096;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

/**
 *
 * @author spd
 */
public class Cell {

    protected char c = '0';
    protected Set<Character> cdd = new TreeSet<Character>(Arrays.asList('1','2','3','4','5','6','7','8','9'));
    protected Set<Character> removed = new HashSet<Character>();

    public Cell(char c) {
        this.c = c;
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
        cdd.add(c);
    }

    public void removeCandidate(char c) {
        cdd.remove(c);
    }

    public boolean tryRemoveCandidate(char c) {
        if (cdd.remove(c)) {
            removed.add(c);
        }
        return 0 != cdd.size();
    }

    public void restoreCandidate(char c) {
        if (removed.remove(c)) {
            cdd.add(c);
        }
    }

    public Set<Character> getCandidates() {
        return cdd;
    }

    public String cToString() {
        StringBuilder sb = new StringBuilder("[");
        for (char cc: cdd) sb.append(cc);
        sb.append(']');
        return sb.toString();
    }
}
