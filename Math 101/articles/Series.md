A **series** is the sum of the terms of a sequence. It is a fundamental concept in mathematics, particularly in calculus and analysis, and is used to represent functions, solve problems, and analyze patterns. Series can be finite (with a limited number of terms) or infinite (with an unlimited number of terms). Here's a detailed explanation:

---

### **Key Concepts**

1. **Sequence vs. Series**:
   - A **sequence** is an ordered list of numbers (e.g., $\( a_1, a_2, a_3, \dots \))$.
   - A **series** is the sum of the terms of a sequence $(e.g., \( a_1 + a_2 + a_3 + \dots \))$.

2. **Finite Series**:
   - A series with a finite number of terms.
   - Example: $\( 1 + 2 + 3 + 4 + 5 \)$.

3. **Infinite Series**:
   - A series with an infinite number of terms.
   - Example: $\( 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots \)$.

4. **Partial Sum**:
   - The sum of the first \( n \) terms of a series:
     $\[
     S_n = a_1 + a_2 + \dots + a_n.
     \]$

5. **Convergence and Divergence**:
   - A series **converges** if the sequence of its partial sums approaches a finite limit as \( n \to \infty \).
   - A series **diverges** if the sequence of its partial sums does not approach a finite limit.

---

### **Types of Series**

1. **Arithmetic Series**:
   - A series where each term is obtained by adding a constant difference \( d \) to the previous term.
   - General form: $\( a + (a + d) + (a + 2d) + \dots \)$.
   - Sum of the first \( n \) terms:
     $\[
     S_n = \frac{n}{2} [2a + (n-1)d].
     \]$

2. **Geometric Series**:
   - A series where each term is obtained by multiplying the previous term by a constant ratio \( r \).
   - General form: $\( a + ar + ar^2 + ar^3 + \dots \)$.
   - Sum of the first \( n \) terms:
     $\[
     S_n = a \frac{1 - r^n}{1 - r} \quad (r \neq 1).
     \]$
   - Sum of an infinite geometric series $(if \( |r| < 1 \))$:
     $\[
     S = \frac{a}{1 - r}.
     \]$

3. **Harmonic Series**:
   - A series of the form:
     $\[
     1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots.
     \]$
   - The harmonic series diverges.

4. **Power Series**:
   - A series of the form:
     $\[
     \sum_{n=0}^\infty c_n (x - a)^n,
     \]$
     where $\( c_n \)$ are coefficients and \( a \) is a constant.
   - Used to represent functions as infinite polynomials.

5. **Taylor and Maclaurin Series**:
   - A power series representation of a function about a point \( a \):
     $\[
     f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x - a)^n.
     \]$
   - If $\( a = 0 \)$, it is called a Maclaurin series.

---

### **Convergence Tests**

1. **Divergence Test**:
   - If $\( \lim_{n \to \infty} a_n \neq 0 \)$, the series $\( \sum a_n \)$ diverges.

2. **Integral Test**:
   - If $\( f(n) = a_n \)$ is positive, continuous, and decreasing, then $\( \sum a_n \)$ and $\( \int_1^\infty f(x) \, dx \)$ either both converge or both diverge.

3. **Comparison Test**:
   - If $\( 0 \leq a_n \leq b_n \) for all \( n \), and \( \sum b_n \) converges, then \( \sum a_n \)$ converges.
   - If $\( \sum a_n \)$ diverges, then $\( \sum b_n \)$ diverges.

4. **Ratio Test**:
   - Compute $\( L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| \)$.
     - If $\( L < 1 \)$, the series converges.
     - If $\( L > 1 \)$, the series diverges.
     - If $\( L = 1 \)$, the test is inconclusive.

5. **Root Test**:
   - Compute $\( L = \lim_{n \to \infty} \sqrt[n]{|a_n|} \)$.
     - If $\( L < 1 \)$, the series converges.
     - If $\( L > 1 \)$, the series diverges.
     - If $\( L = 1 \)$, the test is inconclusive.

6. **Alternating Series Test**:
   - For an alternating series $\( \sum (-1)^n a_n \), if \( a_n \)$ is positive, decreasing, and $\( \lim_{n \to \infty} a_n = 0 \)$, the series converges.

---

### **Applications of Series**

1. **Approximating Functions**:
   - Power series (e.g., Taylor series) are used to approximate functions.

2. **Solving Differential Equations**:
   - Series solutions are used to solve differential equations.

3. **Physics and Engineering**:
   - Series are used to model oscillations, waves, and other phenomena.

4. **Probability and Statistics**:
   - Series are used in probability distributions and statistical analysis.

5. **Computer Science**:
   - Series are used in algorithms and numerical methods.

---

### **Example Problems**

1. **Find the sum of the arithmetic series $\( 3 + 7 + 11 + \dots + 99 \)$**:
   - First term \( a = 3 \), common difference \( d = 4 \).
   - Number of terms:
     $\[
     a_n = a + (n-1)d \implies 99 = 3 + (n-1)(4) \implies n = 25.
     \]$
   - Sum:
     $\[
     S_n = \frac{n}{2} [2a + (n-1)d] = \frac{25}{2} [6 + 96] = 1275.
     \]$

2. **Find the sum of the infinite geometric series \( 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots \)**:
   - First term \( a = 1 \), common ratio $\( r = \frac{1}{2} \)$.
   - Sum:
     $\[
     S = \frac{a}{1 - r} = \frac{1}{1 - \frac{1}{2}} = 2.
     \]$

3. **Test the convergence of $\( \sum_{n=1}^\infty \frac{1}{n^2} \)$**:
   - Use the integral test with $\( f(x) = \frac{1}{x^2} \)$:
     $\[
     \int_1^\infty \frac{1}{x^2} \, dx = \left[-\frac{1}{x}\right]_1^\infty = 1.
     \]$
   - The integral converges, so the series converges.

4. **Find the Maclaurin series for \( f(x) = e^x \)**:
   - The derivatives of $\( e^x \)$ are all $\( e^x \)$, and $\( f^{(n)}(0) = 1 \)$.
   - Maclaurin series:
     $\[
     e^x = \sum_{n=0}^\infty \frac{x^n}{n!}.
     \]$

---

### **Key Takeaways**
- A series is the sum of the terms of a sequence.
- Series can be finite or infinite, and they can converge or diverge.
- Common types include arithmetic, geometric, and power series.
- Convergence tests help determine whether a series converges or diverges.
- Series are widely used in mathematics, physics, engineering, and computer science.
