Differentiation is a fundamental concept in calculus that deals with finding the **derivative** of a function. The derivative represents the rate at which a function changes with respect to its input variable. Differentiation is used to analyze motion, optimize functions, solve differential equations, and more. Here's a detailed explanation:

---

### **Definition of the Derivative**

The derivative of a function \( f(x) \) with respect to \( x \) is defined as:
$\[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
\]$
- $\( f'(x) \)$ is the derivative of \( f(x) \).
- The limit represents the instantaneous rate of change of $\( f(x) \)$ at the point \( x \).

---

### **Notation for Derivatives**

1. **Leibniz Notation**:
   $\[
   \frac{dy}{dx} \quad \text{or} \quad \frac{df}{dx}
   \]$
   - Commonly used in physics and engineering.

2. **Prime Notation**:
   $\[
   f'(x)
   \]$
   - Commonly used in mathematics.

3. **Dot Notation**:
   $\[
   \dot{y}
   \]$
   - Used in physics to denote derivatives with respect to time.

---

### **Rules of Differentiation**

1. **Constant Rule**:
   $\[
   \frac{d}{dx} [c] = 0, \quad \text{where \( c \) is a constant}.
   \]$

2. **Power Rule**:
   $\[
   \frac{d}{dx} [x^n] = nx^{n-1}, \quad \text{where \( n \) is a real number}.
   \]$

3. **Sum/Difference Rule**:
   $\[
   \frac{d}{dx} [f(x) \pm g(x)] = f'(x) \pm g'(x).
   \]$

4. **Product Rule**:
   $\[
   \frac{d}{dx} [f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x).
   \]$

5. **Quotient Rule**:
   $\[
   \frac{d}{dx} \left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}.
   \]$

6. **Chain Rule**:
   $\[
   \frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x).
   \]$

7. **Exponential and Logarithmic Functions**:
   - $\( \frac{d}{dx} [e^x] = e^x \)$.
   - $\( \frac{d}{dx} [\ln(x)] = \frac{1}{x} \)$.

8. **Trigonometric Functions**:
   - $\( \frac{d}{dx} [\sin(x)] = \cos(x) \)$.
   - $\( \frac{d}{dx} [\cos(x)] = -\sin(x) \)$.
   - $\( \frac{d}{dx} [\tan(x)] = \sec^2(x) \)$.

---

### **Applications of Differentiation**

1. **Rates of Change**:
   - Used to find velocities, accelerations, and other rates of change in physics and engineering.

2. **Tangent Lines**:
   - The derivative gives the slope of the tangent line to a curve at a point.

3. **Optimization**:
   - Used to find maximum and minimum values of functions (e.g., profit maximization, cost minimization).

4. **Curve Sketching**:
   - Helps analyze the behavior of functions (e.g., increasing/decreasing intervals, concavity).

5. **Related Rates**:
   - Used to find the rate of change of one quantity with respect to another.

6. **Differential Equations**:
   - Used to model and solve equations involving derivatives.

---

### **Example Problems**

1. **Find the derivative of $\( f(x) = 3x^2 + 2x - 5 \)$**:
   $\[
   f'(x) = \frac{d}{dx}(3x^2) + \frac{d}{dx}(2x) - \frac{d}{dx}(5) = 6x + 2.
   \]$

2. **Use the product rule to differentiate $\( f(x) = x^2 \sin(x) \)$**:
   $\[
   f'(x) = \frac{d}{dx}(x^2) \cdot \sin(x) + x^2 \cdot \frac{d}{dx}(\sin(x)) = 2x \sin(x) + x^2 \cos(x).
   \]$

3. **Use the chain rule to differentiate $\( f(x) = \sin(3x^2) \)$**:
   $\[
   f'(x) = \cos(3x^2) \cdot \frac{d}{dx}(3x^2) = \cos(3x^2) \cdot 6x = 6x \cos(3x^2).
   \]$

4. **Find the slope of the tangent line to $\( y = x^3 - 2x \)$ at \( x = 1 \)**:
   - Compute the derivative:
     $\[
     \frac{dy}{dx} = 3x^2 - 2.
     \]$
   - Evaluate at \( x = 1 \):
     $\[
     \frac{dy}{dx}\bigg|_{x=1} = 3(1)^2 - 2 = 1.
     \]$
   - The slope is \( 1 \).

5. **Optimize the function $\( f(x) = x^3 - 6x^2 + 9x + 1 \)$**:
   - Find the derivative:
     $\[
     f'(x) = 3x^2 - 12x + 9.
     \]$
   - Set $\( f'(x) = 0 \)$ to find critical points:
     $\[
     3x^2 - 12x + 9 = 0 \implies x^2 - 4x + 3 = 0 \implies x = 1, 3.
     \]$
   - Use the second derivative test to determine maxima/minima:
     $\[
     f''(x) = 6x - 12.
     \]$
     - At $\( x = 1 \)$: $\( f''(1) = -6 < 0 \)$ (local maximum).
     - At $\( x = 3 \)$: $\( f''(3) = 6 > 0 \)$ (local minimum).

---

### **Key Takeaways**
- Differentiation is the process of finding the derivative of a function.
- The derivative represents the rate of change of a function with respect to its input.
- Rules like the power rule, product rule, quotient rule, and chain rule simplify differentiation.
- Differentiation has wide-ranging applications in science, engineering, economics, and beyond.
