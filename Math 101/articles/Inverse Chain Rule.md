The **inverse chain rule** is a technique used in calculus to simplify the process of integration, particularly when dealing with composite functions. It is essentially the reverse of the **chain rule** used in differentiation. The inverse chain rule is often applied in integration by substitution, where a change of variables is used to simplify the integral. Here's a detailed explanation:

---

### **What is the Inverse Chain Rule?**

The inverse chain rule is based on the idea of recognizing the derivative of a composite function within an integral. If an integral can be written in the form:
$\[
\int f(g(x)) \cdot g'(x) \, dx,
\]$
then the substitution $\( u = g(x) \)$ simplifies the integral to:
$\[
\int f(u) \, du.
\]$
This is because $\( g'(x) \, dx \)$ is the differential of \( u \), i.e., $\( du = g'(x) \, dx \)$.

---

### **Steps for Using the Inverse Chain Rule**

1. **Identify the Substitution**:
   - Look for a function $\( g(x) \)$ and its derivative $\( g'(x) \)$ in the integrand.
   - Let $\( u = g(x) \)$.

2. **Compute the Differential**:
   - Differentiate \( u \) with respect to \( x \):
    $\[
     du = g'(x) \, dx.
     \]$

3. **Rewrite the Integral**:
   - Substitute \( u \) and \( du \) into the integral:
     $\[
     \int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du.
     \]$

4. **Integrate with Respect to \( u \)**:
   - Compute the integral $\( \int f(u) \, du \)$.

5. **Substitute Back**:
   - Replace $\( u \) with \( g(x) \)$ to express the result in terms of \( x \).

---

### **Example Problems**

1. **Integrate $\( \int 2x \cos(x^2) \, dx \)$**:
   - Let $\( u = x^2 \)$. Then, $\( du = 2x \, dx \)$.
   - Rewrite the integral:
     $\[
     \int \cos(u) \, du.
     \]$
   - Integrate:
     $\[
     \int \cos(u) \, du = \sin(u) + C.
     \]$
   - Substitute back:
     $\[
     \sin(x^2) + C.
     \]$

2. **Integrate $\( \int \frac{3x^2}{\sqrt{x^3 + 1}} \, dx \)$**:
   - Let $\( u = x^3 + 1 \)$. Then, $\( du = 3x^2 \, dx \)$.
   - Rewrite the integral:
     $\[
     \int \frac{1}{\sqrt{u}} \, du.
     \]$
   - Integrate:
     $\[
     \int u^{-1/2} \, du = 2u^{1/2} + C.
     \]$
   - Substitute back:
     $\[
     2\sqrt{x^3 + 1} + C.
     \]$

3. **Integrate $\( \int e^{3x} \, dx \)$**:
   - Let $\( u = 3x \)$. Then, $\( du = 3 \, dx \), or \( dx = \frac{1}{3} \, du \)$.
   - Rewrite the integral:
     $\[
     \int e^u \cdot \frac{1}{3} \, du = \frac{1}{3} \int e^u \, du.
     \]$
   - Integrate:
     $\[
     \frac{1}{3} e^u + C.
     \]$
   - Substitute back:
     $\[
     \frac{1}{3} e^{3x} + C.
     \]$

4. **Integrate $\( \int \frac{\ln(x)}{x} \, dx \)$**:
   - Let $\( u = \ln(x) \)$. Then, $\( du = \frac{1}{x} \, dx \)$.
   - Rewrite the integral:
     $\[
     \int u \, du.
     \]$
   - Integrate:
     $\[
     \frac{u^2}{2} + C.
     \]$
   - Substitute back:
     $\[
     \frac{(\ln(x))^2}{2} + C.
     \]$

---

### **Key Takeaways**
- The inverse chain rule is a technique for simplifying integrals by recognizing the derivative of a composite function.
- It involves substitution: let $\( u = g(x) \)$ and $\( du = g'(x) \, dx \)$.
- After substitution, the integral becomes $\( \int f(u) \, du \)$, which is often easier to evaluate.
- The inverse chain rule is widely used in integration by substitution and is essential for solving many types of integrals.
