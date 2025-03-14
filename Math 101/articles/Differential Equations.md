**Differential equations** are mathematical equations that relate a function to its derivatives. They are used to model dynamic systems, such as population growth, heat transfer, and motion. Differential equations are classified based on their order, linearity, and whether they are ordinary or partial. Here's a detailed explanation:

---

### **Types of Differential Equations**

1. **Ordinary Differential Equations (ODEs)**:
   - Involve functions of a single variable and their derivatives.
   - Example: $\( \frac{dy}{dx} + y = 0 \)$.

2. **Partial Differential Equations (PDEs)**:
   - Involve functions of multiple variables and their partial derivatives.
   - Example: $\( \frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2} \)$ (heat equation).

3. **Order of a Differential Equation**:
   - The highest derivative present in the equation.
   - Example: $\( \frac{d^2 y}{dx^2} + y = 0 \)$ is a second-order ODE.

4. **Linearity**:
   - A differential equation is linear if the dependent variable and its derivatives appear linearly (no products or powers).
   - Example: $\( \frac{dy}{dx} + y = 0 \) is linear; \( \left( \frac{dy}{dx} \right)^2 + y = 0 \)$ is nonlinear.

---

### **Solving Differential Equations**

1. **Separation of Variables**:
   - Used for first-order ODEs of the form $\( \frac{dy}{dx} = f(x)g(y) \)$.
   - Rearrange the equation to separate \( x \) and \( y \):
     $\[
     \frac{dy}{g(y)} = f(x) \, dx.
     \]$
   - Integrate both sides:
     $\[
     \int \frac{dy}{g(y)} = \int f(x) \, dx.
     \]$

2. **Integrating Factor**:
   - Used for linear first-order ODEs of the form $\( \frac{dy}{dx} + P(x)y = Q(x) \)$.
   - Multiply through by the integrating factor $\( \mu(x) = e^{\int P(x) \, dx} \)$:
     $\[
     \mu(x) \frac{dy}{dx} + \mu(x) P(x) y = \mu(x) Q(x).
     \]$
   - The left side becomes the derivative of $\( \mu(x) y \)$:
     $\[
     \frac{d}{dx} (\mu(x) y) = \mu(x) Q(x).
     \]$
   - Integrate both sides:
     $\[
     \mu(x) y = \int \mu(x) Q(x) \, dx.
     \]$

3. **Characteristic Equation**:
   - Used for linear homogeneous ODEs with constant coefficients.
   - Example: For $\( \frac{d^2 y}{dx^2} + a \frac{dy}{dx} + b y = 0 \)$, the characteristic equation is:
     $\[
     r^2 + a r + b = 0.
     \]$
   - Solve for \( r \) to find the general solution.

4. **Series Solutions**:
   - Used for ODEs with variable coefficients.
   - Assume a solution of the form $\( y = \sum_{n=0}^\infty a_n x^n \)$ and substitute into the ODE to find the coefficients $\( a_n \)$.

5. **Laplace Transform**:
   - Converts a differential equation into an algebraic equation, which is easier to solve.
   - Example: The Laplace transform of $\( \frac{dy}{dt} \) is \( s Y(s) - y(0) \)$.

---

### **Applications of Differential Equations**

1. **Physics**:
   - Describes motion, heat transfer, and wave propagation.

2. **Engineering**:
   - Models electrical circuits, fluid flow, and control systems.

3. **Biology**:
   - Models population dynamics and disease spread.

4. **Economics**:
   - Models economic growth and resource allocation.

5. **Chemistry**:
   - Describes reaction rates and diffusion.

---

### **Example Problems**

1. **Solve $\( \frac{dy}{dx} = 2x \)$ using separation of variables**:
   - Separate variables:
     $\[
     dy = 2x \, dx.
     \]$
   - Integrate both sides:
     $\[
     \int dy = \int 2x \, dx \implies y = x^2 + C.
     \]$

2. **Solve $\( \frac{dy}{dx} + y = e^x \)$ using an integrating factor**:
   - The integrating factor is $\( \mu(x) = e^{\int 1 \, dx} = e^x \)$.
   - Multiply through:
     $\[
     e^x \frac{dy}{dx} + e^x y = e^{2x}.
     \]$
   - The left side is the derivative of $\( e^x y \)$:
     $\[
     \frac{d}{dx} (e^x y) = e^{2x}.
     \]$
   - Integrate both sides:
     $\[
     e^x y = \frac{1}{2} e^{2x} + C \implies y = \frac{1}{2} e^x + C e^{-x}.
     \]$

3. **Solve $\( \frac{d^2 y}{dx^2} - 3 \frac{dy}{dx} + 2 y = 0 \)$ using the characteristic equation**:
   - The characteristic equation is:
     $\[
     r^2 - 3 r + 2 = 0 \implies (r - 1)(r - 2) = 0.
     \]$
   - The roots are $\( r = 1 \)$ and $\( r = 2 \)$.
   - The general solution is:
     $\[
     y = C_1 e^x + C_2 e^{2x}.
     \]$

4. **Solve $\( \frac{dy}{dt} + 2 y = 4 \) with \( y(0) = 1 \)$ using the Laplace transform**:
   - Take the Laplace transform:
     $\[
     s Y(s) - y(0) + 2 Y(s) = \frac{4}{s}.
     \]$
   - Substitute $\( y(0) = 1 \)$:
     $\[
     s Y(s) - 1 + 2 Y(s) = \frac{4}{s}.
     \]$
   - Solve for $\( Y(s) \)$:
     $\[
     Y(s) (s + 2) = \frac{4}{s} + 1 \implies Y(s) = \frac{4 + s}{s (s + 2)}.
     \]$
   - Perform partial fraction decomposition:
     $\[
     Y(s) = \frac{A}{s} + \frac{B}{s + 2}.
     \]$
     Solving for \( A \) and \( B \):
     $\[
     A = 2, \quad B = -1.
     \]$
   - Take the inverse Laplace transform:
     $\[
     y(t) = 2 - e^{-2t}.
     \]$

---

### **Key Takeaways**
- Differential equations relate a function to its derivatives and are used to model dynamic systems.
- They are classified as ordinary or partial, and by their order and linearity.
- Common solution methods include separation of variables, integrating factors, characteristic equations, and Laplace transforms.
- Differential equations are essential in physics, engineering, biology, and economics.
