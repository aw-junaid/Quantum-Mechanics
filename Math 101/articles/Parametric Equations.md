Parametric equations are a way of defining a mathematical relationship using one or more independent variables, called **parameters**. Instead of expressing \( y \) directly as a function of \( x \) (or vice versa), parametric equations describe both \( x \) and \( y \) in terms of a third variable, often denoted as \( t \). Parametric equations are widely used in physics, engineering, computer graphics, and calculus to describe curves and motion. Here's a detailed explanation:

---

### **Definition of Parametric Equations**

A set of parametric equations defines a curve by expressing the coordinates \( x \) and \( y \) as functions of a parameter \( t \):
$\[
x = f(t), \quad y = g(t).
\]$
- \( t \) is the parameter, which often represents time or an angle.
- As \( t \) varies, the point \( (x, y) \) traces out a curve in the plane.

---

### **Key Concepts**

1. **Eliminating the Parameter**:
   - To convert parametric equations into a Cartesian equation (relating \( x \) and \( y \) directly), solve one equation for \( t \) and substitute into the other.
   - Example:
     $\[
     x = t + 1, \quad y = t^2.
     \]$
     Solve for \( t \): \( t = x - 1 \). Substitute into \( y \):
     $\[
     y = (x - 1)^2.
     \]$

2. **Graphing Parametric Equations**:
   - Plot points by choosing values of \( t \) and computing \( x \) and \( y \).
   - Example:
     $\[
     x = \cos(t), \quad y = \sin(t).
     \]$
     This describes a circle of radius 1 centered at the origin.

3. **Direction of Motion**:
   - Parametric equations often describe motion, and the parameter \( t \) indicates the direction in which the curve is traced.

4. **Parametric Curves in 3D**:
   - In three dimensions, parametric equations can describe curves in space:
     $\[
     x = f(t), \quad y = g(t), \quad z = h(t).
     \]$

---

### **Applications of Parametric Equations**

1. **Physics**:
   - Describe the motion of objects (e.g., projectile motion, planetary orbits).

2. **Engineering**:
   - Model trajectories of vehicles, robots, or particles.

3. **Computer Graphics**:
   - Render curves and surfaces in animations and simulations.

4. **Calculus**:
   - Used to compute derivatives, integrals, and arc lengths of curves.

---

### **Calculus with Parametric Equations**

1. **Derivatives**:
   - The slope of the tangent line to a parametric curve is given by:
     $\[
     \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}.
     \]$
   - Example:
     $\[
     x = t^2, \quad y = t^3.
     \]$
     Compute $\( \frac{dx}{dt} = 2t \)$ and $\( \frac{dy}{dt} = 3t^2 \)$. Then:
     $\[
     \frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}.
     \]$

2. **Arc Length**:
   - The length of a parametric curve from \( t = a \) to \( t = b \) is:
     $\[
     L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt.
     \]$
   - Example:
     $\[
     x = \cos(t), \quad y = \sin(t), \quad 0 \leq t \leq 2\pi.
     \]$
     Compute $\( \frac{dx}{dt} = -\sin(t) \)$ and $\( \frac{dy}{dt} = \cos(t) \)$. Then:
     $\[
     L = \int_0^{2\pi} \sqrt{(-\sin(t))^2 + (\cos(t))^2} \, dt = \int_0^{2\pi} \sqrt{1} \, dt = 2\pi.
     \]$

3. **Area Under a Curve**:
   - The area under a parametric curve $\( y = g(t) \)$ from \( t = a \) to \( t = b \) is:
     $\[
     A = \int_a^b y \, \frac{dx}{dt} \, dt.
     \]$
   - Example:
     $\[
     x = t^2, \quad y = t^3, \quad 0 \leq t \leq 1.
     \]$
     Compute $\( \frac{dx}{dt} = 2t \)$. Then:
     $\[
     A = \int_0^1 t^3 \cdot 2t \, dt = \int_0^1 2t^4 \, dt = \frac{2}{5}.
     \]$

---

### **Example Problems**

1. **Graph the parametric equations $\( x = 2\cos(t) \)$, $\( y = 3\sin(t) \)$ for $\( 0 \leq t \leq 2\pi \)$**:
   - This describes an ellipse centered at the origin with semi-major axis 3 and semi-minor axis 2.

2. **Eliminate the parameter \( t \) from \( x = t + 1 \), $\( y = t^2 \)$**:
   - Solve for \( t \): $\( t = x - 1 \)$. Substitute into \( y \):
     $\[
     y = (x - 1)^2.
     \]$

3. **Find the slope of the tangent line to the curve $\( x = t^2 \)$, $\( y = t^3 \)$ at $\( t = 2 \)$**:
   - Compute $\( \frac{dx}{dt} = 2t \)$ and $\( \frac{dy}{dt} = 3t^2 \)$. Then:
     $\[
     \frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}.
     \]$
     At \( t = 2 \):
     $\[
     \frac{dy}{dx} = \frac{3(2)}{2} = 3.
     \]$

4. **Compute the arc length of the curve $\( x = \cos(t) \)$, $\( y = \sin(t) \)$ for $\( 0 \leq t \leq 2\pi \)$**:
   - Compute $\( \frac{dx}{dt} = -\sin(t) \)$ and $\( \frac{dy}{dt} = \cos(t) \)$. Then:
     $\[
     L = \int_0^{2\pi} \sqrt{(-\sin(t))^2 + (\cos(t))^2} \, dt = \int_0^{2\pi} \sqrt{1} \, dt = 2\pi.
     \]$

---

### **Key Takeaways**
- Parametric equations define curves using a parameter \( t \), expressing \( x \) and \( y \) as functions of \( t \).
- They are useful for describing motion, curves, and surfaces in mathematics, physics, and engineering.
- Calculus techniques (e.g., derivatives, arc length) can be applied to parametric equations.
- Understanding parametric equations is essential for advanced studies in calculus and related fields.
