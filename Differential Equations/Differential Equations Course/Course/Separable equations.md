### **Separable Differential Equations**  

A **separable differential equation** is a first-order differential equation that can be written in the form:

$\[
\frac{dy}{dx} = f(x) g(y)
\]$

Or, equivalently:

$\[
\frac{dy}{dx} = \frac{h(y)}{k(x)}
\]$

These equations are called **separable** because the variables \(x\) and \(y\) can be separated on opposite sides of the equation.

---

### 📌 **General Solution Method for Separable Equations:**
1. **Rewrite the equation:**  
   Rearrange the terms to separate the variables:

$\[
\frac{dy}{g(y)} = f(x) \, dx
\]$

2. **Integrate both sides:**  
   Perform integration on both sides:

$\[
\int \frac{1}{g(y)} \, dy = \int f(x) \, dx
\]$

3. **Solve for \(y\):**  
   If possible, solve the resulting equation to express \(y\) explicitly in terms of \(x\).

4. **Apply initial conditions (if provided):**  
   If an initial value is given, use it to determine the constant of integration.

---

### ✅ **Example 1: Basic Separable Equation**
Solve:

$\[
\frac{dy}{dx} = xy
\]$

**Step 1:** Separate variables:

$\[
\frac{dy}{y} = x \, dx
\]$

**Step 2:** Integrate both sides:

$\[
\int \frac{1}{y} \, dy = \int x \, dx
\]$

$\[
\ln |y| = \frac{x^2}{2} + C
\]$

**Step 3:** Solve for \(y\):

$\[
y = C e^{x^2/2}
\]$

---

### ✅ **Example 2: Solving with an Initial Condition**
Solve the equation:

$\[
\frac{dy}{dx} = 3y, \quad y(0) = 2
\]$

**Step 1:** Separate variables:

$\[
\frac{dy}{y} = 3 \, dx
\]$

**Step 2:** Integrate both sides:

$\[
\int \frac{1}{y} \, dy = \int 3 \, dx
\]$

$\[
\ln |y| = 3x + C
\]$

**Step 3:** Solve for \(y\):

$\[
y = C e^{3x}
\]$

**Step 4:** Apply the initial condition $\( y(0) = 2 \)$:

$\[
2 = C e^{0} \Rightarrow C = 2
\]$

So, the particular solution is:

$\[
y = 2 e^{3x}
\]$

---

### 📊 **Applications of Separable Equations:**
1. **Population Growth (Exponential Model):**
   $\[
   \frac{dP}{dt} = rP
   \]$
   Solution: $\( P(t) = P_0 e^{rt} \)$
   
2. **Radioactive Decay:**
   $\[
   \frac{dN}{dt} = -\lambda N
   \]$
   Solution: $\( N(t) = N_0 e^{-\lambda t} \)$
   
3. **Newton's Law of Cooling:**
   $\[
   \frac{dT}{dt} = -k(T - T_{\text{env}})
   \]$

4. **Mixing Problems** (e.g., saltwater concentration changes over time).

---

### 📌 **Key Takeaways:**
- **Separable equations** allow us to **split variables** and integrate each part.
- They appear frequently in **real-world models** like **growth**, **decay**, and **heating/cooling** processes.
- Integration techniques like **natural logarithms** and **exponentials** are commonly used to find solutions.
