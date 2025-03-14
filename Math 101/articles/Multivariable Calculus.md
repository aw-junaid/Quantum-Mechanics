**Multivariable calculus** is the extension of calculus to functions of more than one variable. It involves the study of limits, derivatives, integrals, and series in higher dimensions. Multivariable calculus is essential in fields like physics, engineering, economics, and machine learning, where systems often depend on multiple variables. Here's a detailed explanation:

---

### **Key Concepts in Multivariable Calculus**

1. **Functions of Multiple Variables**:
   - A function $\( f(x, y) \)$ depends on two variables, \( x \) and \( y \).
   - Example: $\( f(x, y) = x^2 + y^2 \)$.

2. **Limits and Continuity**:
   - The limit of $\( f(x, y) \)$ as \( (x, y) \) approaches $\( (a, b) \) is \( L \) if \( f(x, y) \)$ gets arbitrarily close to \( L \) as \( (x, y) \) gets close to \( (a, b) \).
   - A function is continuous at \( (a, b) \) if:
     $\[
     \lim_{(x, y) \to (a, b)} f(x, y) = f(a, b).
     \]$

3. **Partial Derivatives**:
   - The partial derivative of $\( f(x, y) \)$ with respect to \( x \) is the derivative of \( f \) with respect to \( x \), treating \( y \) as a constant.
   - Notation:
     $\[
     \frac{\partial f}{\partial x} \quad \text{or} \quad f_x.
     \]$
   - Example: For $\( f(x, y) = x^2 + y^2 \)$,
     $\[
     \frac{\partial f}{\partial x} = 2x, \quad \frac{\partial f}{\partial y} = 2y.
     \]$

4. **Gradient**:
   - The gradient of $\( f(x, y) \)$ is a vector of its partial derivatives:
     $\[
     \nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right).
     \]$
   - The gradient points in the direction of the steepest increase of \( f \).

5. **Directional Derivative**:
   - The rate of change of $\( f(x, y) \)$ in the direction of a unit vector $\( \vec{u} = (u_1, u_2) \)$:
     $\[
     D_{\vec{u}} f = \nabla f \cdot \vec{u} = \frac{\partial f}{\partial x} u_1 + \frac{\partial f}{\partial y} u_2.
     \]$

6. **Multiple Integrals**:
   - Double integrals compute the volume under a surface $\( z = f(x, y) \)$ over a region \( R \):
     $\[
     \iint_R f(x, y) \, dA.
     \]$
   - Triple integrals compute the volume of a solid in 3D:
     $\[
     \iiint_E f(x, y, z) \, dV.
     \]$

7. **Vector Calculus**:
   - Studies vector fields, line integrals, surface integrals, and theorems like Green's, Stokes', and the Divergence Theorem.

---

### **Applications of Multivariable Calculus**

1. **Physics**:
   - Describes motion in 3D, fluid flow, and electromagnetic fields.

2. **Engineering**:
   - Analyzes stress, heat transfer, and structural design.

3. **Economics**:
   - Models utility functions, production functions, and optimization problems.

4. **Machine Learning**:
   - Optimizes loss functions with multiple parameters.

5. **Computer Graphics**:
   - Renders 3D objects and animations.

---

### **Example Problems**

1. **Compute the partial derivatives of $\( f(x, y) = x^2 y + \sin(xy) \)$**:
   - Partial derivative with respect to \( x \):
     $\[
     \frac{\partial f}{\partial x} = 2xy + y \cos(xy).
     \]$
   - Partial derivative with respect to \( y \):
     $\[
     \frac{\partial f}{\partial y} = x^2 + x \cos(xy).
     \]$

2. **Find the gradient of $\( f(x, y) = x^2 + y^2 \) at \( (1, 2) \)$**:
   - Compute the partial derivatives:
     $\[
     \frac{\partial f}{\partial x} = 2x, \quad \frac{\partial f}{\partial y} = 2y.
     \]$
   - Evaluate at \( (1, 2) \):
     $\[
     \nabla f = (2(1), 2(2)) = (2, 4).
     \]$

3. **Compute the double integral $\( \iint_R (x + y) \, dA \)$, where \( R \) is the rectangle $\( 0 \leq x \leq 1 \)$, $\( 0 \leq y \leq 2 \)$**:
   - Set up the integral:
     $\[
     \int_0^1 \int_0^2 (x + y) \, dy \, dx.
     \]$
   - Integrate with respect to \( y \):
     $\[
     \int_0^2 (x + y) \, dy = \left[ xy + \frac{y^2}{2} \right]_0^2 = 2x + 2.
     \]$
   - Integrate with respect to \( x \):
     $\[
     \int_0^1 (2x + 2) \, dx = \left[ x^2 + 2x \right]_0^1 = 3.
     \]$

4. **Find the directional derivative of $\( f(x, y) = x^2 + y^2 \)$ at \( (1, 1) \) in the direction of $\( \vec{u} = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right) \)$**:
   - Compute the gradient:
     $\[
     \nabla f = (2x, 2y).
     \]$
   - Evaluate at \( (1, 1) \):
     $\[
     \nabla f(1, 1) = (2, 2).
     \]$
   - Compute the directional derivative:
     $\[
     D_{\vec{u}} f = \nabla f \cdot \vec{u} = (2, 2) \cdot \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right) = \frac{2}{\sqrt{2}} + \frac{2}{\sqrt{2}} = 2\sqrt{2}.
     \]$

---

### **Key Takeaways**
- Multivariable calculus extends calculus to functions of multiple variables.
- Key concepts include partial derivatives, gradients, multiple integrals, and vector calculus.
- It has wide-ranging applications in physics, engineering, economics, and machine learning.
- Understanding multivariable calculus is essential for solving problems in higher dimensions.
