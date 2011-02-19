import java.math.*;
import java.util.*;
import static java.lang.System.*;

/**
 * code from: http://blog.mycila.com/2009/07/project-euler-problem-55.html
 */
class p055 {

  public static void main(String[] args) {
    long time = currentTimeMillis();
    final int maxNumber = 10000;
    final int maxIterations = 50;
    final Set<BigInteger> lychrel = new TreeSet<BigInteger>();
    final Set<BigInteger> nonLychrel = new TreeSet<BigInteger>();
    final Set<BigInteger> stack = new TreeSet<BigInteger>();
    for (int n = 0; n < maxNumber; n++) {
      BigInteger test = BigInteger.valueOf(n);
      // do not do anything if this number as already be marked
      if (lychrel.contains(test))
          continue;
      // if it is not marked, we must find what it is in a maximum of 'maxIterations' iterations
      stack.add(test);
      BigInteger reverse = Maths.reverse(test);
      // iterate while we not found a palindrom in some maximum iterations
      for (int it = 1; it < maxIterations; it++) {
        test = test.add(reverse);
        reverse = Maths.reverse(test);
        stack.add(test);
        if (test.equals(reverse) || nonLychrel.contains(test)) {
          nonLychrel.addAll(stack);
          stack.clear();
          break;
        } else if (lychrel.contains(test)) {
          lychrel.addAll(stack);
          stack.clear();
          break;
        }
      }
      if(!stack.isEmpty()) {
        lychrel.addAll(stack);
        stack.clear();
      }
    }

    System.out.println(lychrel);
    out.println(lychrel.size() + " in " + (currentTimeMillis() - time) + "ms");

    int count = 0;
    BigInteger max = BigInteger.valueOf(maxNumber);
    for (BigInteger l : lychrel) if (l.compareTo(max) <= 0) count++;

    out.println(count + " under " + maxNumber);
  }
}
class Maths {
  public static BigInteger reverse(BigInteger b) {
    BigInteger r = BigInteger.ZERO;
    while (b.compareTo(BigInteger.ZERO)!=0) {
      BigInteger dr[] = b.divideAndRemainder(BigInteger.TEN);
      r = r.multiply(BigInteger.TEN);
      r = r.add(dr[1]);
      b = dr[0];
    } 
    return r;
  }
}
