Logarithms are mathematical functions that help simplify complex calculations, particularly those involving exponential growth or decay. They are the inverse operations of exponentiation. Here's a detailed explanation:

---

### **Definition**
The logarithm of a number \( x \) with respect to a base \( b \) is the exponent to which \( b \) must be raised to yield \( x \). Mathematically:
$\[
\log_b(x) = y \quad \text{if and only if} \quad b^y = x
\]$
- \( b \) is the **base** (a positive real number, \( b > 0 \), $\( b \neq 1 \))$.
- \( x \) is the **argument** (a positive real number, \( x > 0 \)).
- \( y \) is the **logarithm** (the exponent).

---

### **Common Bases**
1. **Natural Logarithm (ln)**:
   - Base: \( e \) (Euler's number, approximately 2.71828).
   - Written as: $\( \ln(x) = \log_e(x) \)$.

2. **Common Logarithm (log)**:
   - Base: 10.
   - Written as: $\( \log(x) = \log_{10}(x) \)$.

---

### **Properties of Logarithms**
Logarithms have several key properties that make them useful for simplifying calculations:

1. **Product Rule**:
   $\[
   \log_b(xy) = \log_b(x) + \log_b(y)
   \]$
   - The logarithm of a product is the sum of the logarithms.

2. **Quotient Rule**:
   $\[
   \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)
   \]$
   - The logarithm of a quotient is the difference of the logarithms.

3. **Power Rule**:
   $\[
   \log_b(x^n) = n \log_b(x)
   \]$
   - The logarithm of a power is the exponent times the logarithm.

4. **Change of Base Formula**:
   $\[
   \log_b(x) = \frac{\log_k(x)}{\log_k(b)}
   \]$
   - Allows conversion between different bases.

5. **Logarithm of 1**:
   $\[
   \log_b(1) = 0
   \]$
   - Because $\( b^0 = 1 \)$ for any base \( b \).

6. **Logarithm of the Base**:
   $\[
   \log_b(b) = 1
   \]$
   - Because $\( b^1 = b \)$.

---

### **Graph of Logarithmic Functions**
- The graph of $\( y = \log_b(x) \)$ is a curve that:
  - Passes through $\( (1, 0) \)$ because $\( \log_b(1) = 0 \)$.
  - Passes through $\( (b, 1) \)$ because $\( \log_b(b) = 1 \)$.
  - Is undefined for $\( x \leq 0 \)$.
  - Increases slowly as \( x \) increases.

---

### **Applications of Logarithms**
1. **Solving Exponential Equations**:
   - Logarithms are used to solve equations where the variable is in the exponent, e.g., \( 2^x = 8 \).

2. **Scientific Scales**:
   - The pH scale (acidity), Richter scale (earthquake magnitude), and decibel scale (sound intensity) are logarithmic.

3. **Compound Interest**:
   - Logarithms help calculate the time required for investments to grow exponentially.

4. **Data Compression**:
   - Logarithms are used in algorithms to reduce data size.

5. **Computer Science**:
   - Logarithms describe the time complexity of algorithms (e.g., binary search is $\( O(\log n) \))$.

---

### **Example Calculations**
1. **Evaluate $\( \log_2(8) \)$**:
   $\[
   \log_2(8) = 3 \quad \text{because} \quad 2^3 = 8.
   \]$

2. **Simplify $\( \log_3(81) \)$**:
   $\[
   \log_3(81) = \log_3(3^4) = 4 \log_3(3) = 4.
   \]$

3. **Solve \( 10^x = 1000 \)**:
   $\[
   x = \log_{10}(1000) = 3.
   \]$

4. **Change of Base**:
   $\[
   \log_2(5) = \frac{\ln(5)}{\ln(2)} \approx \frac{1.6094}{0.6931} \approx 2.3219.
   \]$

---

### **Key Takeaways**
- Logarithms transform multiplicative relationships into additive ones, simplifying calculations.
- They are essential in fields like mathematics, science, engineering, and finance.
- Understanding their properties and applications is crucial for solving real-world problems.
