Integration is a fundamental concept in calculus that deals with finding the **integral** of a function. It is the reverse process of differentiation and is used to compute areas, volumes, and other quantities that accumulate over an interval. Integration is essential in physics, engineering, economics, and many other fields. Here's a detailed explanation:

---

### **Definition of Integration**

1. **Indefinite Integral**:
   - Represents a family of functions (antiderivatives) whose derivative is the original function.
   - Notation:
     $\[
     \int f(x) \, dx = F(x) + C
     \]$
     - \( F(x) \) is the antiderivative of \( f(x) \).
     - \( C \) is the constant of integration.

2. **Definite Integral**:
   - Represents the accumulation of a quantity over an interval $\([a, b]\)$.
   - Notation:
     $\[
     \int_a^b f(x) \, dx
     \]$
     - Computes the net area under the curve $\( y = f(x) \)$ between \( x = a \) and \( x = b \).

---

### **Fundamental Theorem of Calculus**

The Fundamental Theorem of Calculus connects differentiation and integration:
1. **Part 1**:
   - If \( F(x) \) is an antiderivative of \( f(x) \), then:
     $\[
     \int_a^b f(x) \, dx = F(b) - F(a).
     \]$

2. **Part 2**:
   - If \( f(x) \) is continuous on $\([a, b]\)$, then:
     $\[
     \frac{d}{dx} \left[\int_a^x f(t) \, dt\right] = f(x).
     \]$

---

### **Techniques of Integration**

1. **Basic Rules**:
   - $\( \int x^n \, dx = \frac{x^{n+1}}{n+1} + C \) (for \( n \neq -1 \))$.
   - $\( \int e^x \, dx = e^x + C \)$.
   - $\( \int \frac{1}{x} \, dx = \ln|x| + C \)$.

2. **Substitution**:
   - Used to simplify integrals by changing variables.
   - Example:
     $\[
     \int 2x \cos(x^2) \, dx.
     \]$
     Let $\( u = x^2 \)$, then $\( du = 2x \, dx \)$, and the integral becomes:
     $\[
     \int \cos(u) \, du = \sin(u) + C = \sin(x^2) + C.
     \]$

3. **Integration by Parts**:
   - Based on the product rule for differentiation.
   - Formula:
     $\[
     \int u \, dv = uv - \int v \, du.
     \]$
   - Example:
     $\[
     \int x e^x \, dx.
     \]$
     Let \( u = x \) and $\( dv = e^x \, dx \)$, then $\( du = dx \)$ and $\( v = e^x \)$. Apply the formula:
     $\[
     \int x e^x \, dx = x e^x - \int e^x \, dx = x e^x - e^x + C.
     \]$

4. **Partial Fractions**:
   - Used to integrate rational functions by decomposing them into simpler fractions.
   - Example:
     $\[
     \int \frac{1}{x^2 - 1} \, dx.
     \]$
     Decompose:
     $\[
     \frac{1}{x^2 - 1} = \frac{1}{2} \left(\frac{1}{x-1} - \frac{1}{x+1}\right).
     \]$
     Integrate:
     $\[
     \int \frac{1}{x^2 - 1} \, dx = \frac{1}{2} \left[\ln|x-1| - \ln|x+1|\right] + C.
     \]$

5. **Trigonometric Integrals**:
   - Used to integrate products of trigonometric functions.
   - Example:
     $\[
     \int \sin^2(x) \, dx.
     \]$
     Use the identity $\( \sin^2(x) = \frac{1 - \cos(2x)}{2} \)$:
     $\[
     \int \sin^2(x) \, dx = \frac{1}{2} \int (1 - \cos(2x)) \, dx = \frac{1}{2} \left(x - \frac{\sin(2x)}{2}\right) + C.
     \]$

---

### **Applications of Integration**

1. **Area Under a Curve**:
   - The definite integral $\( \int_a^b f(x) \, dx \)$ computes the net area between the curve $\( y = f(x) \)$ and the \( x \)-axis from \( x = a \) to \( x = b \).

2. **Volume of Solids of Revolution**:
   - Used to find volumes of shapes formed by rotating a curve around an axis (e.g., disk method, shell method).

3. **Work and Energy**:
   - In physics, integration is used to calculate work done by a force or energy stored in a system.

4. **Probability and Statistics**:
   - Integration is used to compute probabilities and expected values in continuous probability distributions.

5. **Economics**:
   - Used to calculate consumer surplus, producer surplus, and total revenue.

---

### **Example Problems**

1. **Compute the indefinite integral $\( \int (3x^2 + 2x - 5) \, dx \)$**:
   $\[
   \int (3x^2 + 2x - 5) \, dx = x^3 + x^2 - 5x + C.
   \]$

2. **Evaluate the definite integral $\( \int_0^2 x^3 \, dx \)$**:
   $\[
   \int_0^2 x^3 \, dx = \left[\frac{x^4}{4}\right]_0^2 = \frac{16}{4} - 0 = 4.
   \]$

3. **Use substitution to evaluate $\( \int 2x \sqrt{x^2 + 1} \, dx \)$**:
   - Let $\( u = x^2 + 1 \)$, then $\( du = 2x \, dx \)$:
     $\[
     \int \sqrt{u} \, du = \frac{2}{3} u^{3/2} + C = \frac{2}{3} (x^2 + 1)^{3/2} + C.
     \]$

4. **Use integration by parts to evaluate \( \int x \ln(x) \, dx \)**:
   - Let $\( u = \ln(x) \)$ and $\( dv = x \, dx \)$, then $\( du = \frac{1}{x} \, dx \)$ and $\( v = \frac{x^2}{2} \)$:
     $\[
     \int x \ln(x) \, dx = \frac{x^2}{2} \ln(x) - \int \frac{x^2}{2} \cdot \frac{1}{x} \, dx = \frac{x^2}{2} \ln(x) - \frac{x^2}{4} + C.
     \]$

5. **Find the area under $\( y = x^2 \) from \( x = 0 \) to \( x = 2 \)$**:
   $\[
   \int_0^2 x^2 \, dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}.
   \]$

---

### **Key Takeaways**
- Integration is the reverse process of differentiation and is used to compute areas, volumes, and accumulated quantities.
- Techniques like substitution, integration by parts, and partial fractions simplify integration.
- Integration has wide-ranging applications in science, engineering, economics, and beyond.
- Understanding integration is essential for solving problems in calculus and related fields.
