Limits are a fundamental concept in calculus that describe the behavior of a function as its input approaches a certain value. They are used to define derivatives, integrals, and continuity, and they form the foundation of calculus. Here's a detailed explanation:

---

### **Definition of a Limit**

The limit of a function \( f(x) \) as \( x \) approaches a value \( a \) is the value that \( f(x) \) gets closer to as \( x \) gets closer to \( a \). Mathematically, this is written as:
$\[
\lim_{x \to a} f(x) = L
\]$
- \( L \) is the limit value.
- $\( x \to a \)$ means \( x \) approaches \( a \) (but does not necessarily equal \( a \)).

---

### **Key Concepts**

1. **One-Sided Limits**:
   - **Left-Hand Limit**: The limit as \( x \) approaches \( a \) from the left $(denoted as \( x \to a^- \))$.
   - **Right-Hand Limit**: The limit as \( x \) approaches \( a \) from the right $(denoted as \( x \to a^+ \))$.

   For the limit $\( \lim_{x \to a} f(x) \)$ to exist, the left-hand and right-hand limits must be equal:
   $\[
   \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L.
   \]$

2. **Infinite Limits**:
   - If \( f(x) \) grows without bound as \( x \to a \), the limit is said to be infinite:
     $\[
     \lim_{x \to a} f(x) = \infty \quad \text{or} \quad \lim_{x \to a} f(x) = -\infty.
     \]$

3. **Limits at Infinity**:
   - Describes the behavior of \( f(x) \) as \( x \) approaches $\( \infty \)$ or $\( -\infty \)$:
     $\[
     \lim_{x \to \infty} f(x) = L \quad \text{or} \quad \lim_{x \to -\infty} f(x) = L.
     \]$

4. **Continuity**:
   - A function \( f(x) \) is continuous at \( x = a \) if:
     $\[
     \lim_{x \to a} f(x) = f(a).
     \]$
   - This means the limit exists, and the function value equals the limit.

---

### **Properties of Limits**

1. **Sum/Difference Rule**:
   $\[
   \lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x).
   \]$

2. **Product Rule**:
   $\[
   \lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x).
   \]$

3. **Quotient Rule**:
   $\[
   \lim_{x \to a} \left[\frac{f(x)}{g(x)}\right] = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if} \quad \lim_{x \to a} g(x) \neq 0.
   \]$

4. **Constant Multiple Rule**:
   $\[
   \lim_{x \to a} [c \cdot f(x)] = c \cdot \lim_{x \to a} f(x).
   \]$

5. **Power Rule**:
   $\[
   \lim_{x \to a} [f(x)]^n = \left[\lim_{x \to a} f(x)\right]^n.
   \]$

---

### **Techniques for Evaluating Limits**

1. **Direct Substitution**:
   - If $\( f(x) \)$ is continuous at \( x = a \), then:
     $\[
     \lim_{x \to a} f(x) = f(a).
     \]$

2. **Factoring**:
   - If direct substitution results in an indeterminate form $(e.g., \( \frac{0}{0} \))$, factor the numerator and denominator and simplify.

3. **Rationalization**:
   - For limits involving square roots, multiply the numerator and denominator by the conjugate.

4. **L'Hôpital's Rule**:
   - If $\( \lim_{x \to a} \frac{f(x)}{g(x)} \)$ results in $\( \frac{0}{0} \)$ or $\( \frac{\infty}{\infty} \)$, then:
     $\[
     \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)},
     \]$
     provided the limit on the right exists.

5. **Squeeze Theorem**:
   - If $\( f(x) \leq g(x) \leq h(x) \)$ near $\( x = a \)$ and $\( \lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L \)$, then:
     $\[
     \lim_{x \to a} g(x) = L.
     \]$

---

### **Applications of Limits**

1. **Defining Derivatives**:
   - The derivative of $\( f(x) \)$ at $\( x = a \)$ is defined as:
     $\[
     f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}.
     \]$

2. **Defining Integrals**:
   - The definite integral of $\( f(x) \)$ over $\([a, b]\)$ is defined as a limit of Riemann sums.

3. **Continuity**:
   - Limits are used to define and analyze the continuity of functions.

4. **Asymptotes**:
   - Limits help identify horizontal and vertical asymptotes of functions.

---

### **Example Problems**

1. **Evaluate $\( \lim_{x \to 2} (3x + 1) \)$**:
   $\[
   \lim_{x \to 2} (3x + 1) = 3(2) + 1 = 7.
   \]$

2. **Evaluate $\( \lim_{x \to 3} \frac{x^2 - 9}{x - 3} \)$**:
   - Direct substitution gives \( \frac{0}{0} \), so factor the numerator:
     $\[
     \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} = \lim_{x \to 3} (x+3) = 6.
     \]$

3. **Evaluate $\( \lim_{x \to \infty} \frac{2x^2 + 3x - 1}{x^2 + 4} \)$**:
   - Divide numerator and denominator by $\( x^2 \)$:
     $\[
     \lim_{x \to \infty} \frac{2 + \frac{3}{x} - \frac{1}{x^2}}{1 + \frac{4}{x^2}} = \frac{2 + 0 - 0}{1 + 0} = 2.
     \]$

4. **Use L'Hôpital's Rule to evaluate $\( \lim_{x \to 0} \frac{\sin(x)}{x} \)$**:
   - Direct substitution gives $\( \frac{0}{0} \)$, so apply L'Hôpital's Rule:
     $\[
     \lim_{x \to 0} \frac{\sin(x)}{x} = \lim_{x \to 0} \frac{\cos(x)}{1} = 1.
     \]$

---

### **Key Takeaways**
- Limits describe the behavior of a function as the input approaches a specific value.
- They are essential for defining derivatives, integrals, and continuity.
- Techniques like direct substitution, factoring, and L'Hôpital's Rule are used to evaluate limits.
- Understanding limits is crucial for studying calculus and its applications.
