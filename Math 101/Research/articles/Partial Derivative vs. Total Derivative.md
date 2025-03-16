### **Partial Derivative vs. Total Derivative**
 
#### **1. Partial Derivative**
A **partial derivative** is used when a function has multiple variables, but we differentiate with respect to only one variable while keeping the others constant.

##### **Example:**
Suppose we have a function:

$\[
f(x, y) = x^2 y + 3y^3
\]$

- **Partial derivative w.r.t. \( x \) (keeping \( y \) constant)**:

$\[
\frac{\partial f}{\partial x} = \frac{\partial}{\partial x} (x^2 y + 3y^3) = 2xy
\]$

- **Partial derivative w.r.t. \( y \) (keeping \( x \) constant)**:

$\[
\frac{\partial f}{\partial y} = \frac{\partial}{\partial y} (x^2 y + 3y^3) = x^2 + 9y^2
\]$

---

#### **2. Total Derivative**
A **total derivative** considers all variables as functions of an independent variable, applying the chain rule to account for their dependencies.

##### **Example:**
If $\( f(x, y) \)$ is a function of \( x \) and \( y \), but \( x \) and \( y \) themselves depend on another variable \( t \), the total derivative is:

$\[
\frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
\]$

Using the same function $\( f(x, y) = x^2 y + 3y^3 \), if \( x \) and \( y \) depend on \( t \)$:

$\[
\frac{df}{dt} = (2xy) \frac{dx}{dt} + (x^2 + 9y^2) \frac{dy}{dt}
\]$

Here, the total derivative accounts for changes in both \( x \) and \( y \) as \( t \) changes.

---

### **Key Differences:**
| Feature             | Partial Derivative | Total Derivative |
|---------------------|------------------|----------------|
| Differentiation w.r.t. | One variable, keeping others constant | All variables considering their dependencies |
| Function Type      | Multivariable function $\( f(x, y, ...) \)$ | Function where variables depend on another variable |
| Example Formula   | $\( \frac{\partial f}{\partial x} \)$ | $\( \frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt} \)$ |

