Formulas used in explaining **partial derivative** and **total derivative**:

### **1. Partial Derivative Formula**
For a function $\( f(x, y) \)$, the **partial derivative** with respect to \( x \) and \( y \) is:

$\[
\frac{\partial f}{\partial x} = \lim_{\Delta x \to 0} \frac{f(x + \Delta x, y) - f(x, y)}{\Delta x}
\]$

$\[
\frac{\partial f}{\partial y} = \lim_{\Delta y \to 0} \frac{f(x, y + \Delta y) - f(x, y)}{\Delta y}
\]$

### **2. Total Derivative Formula**
For a function $\( f(x, y) \), where \( x \) and \( y \) are functions of \( t \)$, the **total derivative** is given by:

$\[
\frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
\]$

### **Example Application**
For the function:

$\[
f(x, y) = x^2 y + 3y^3
\]$

- **Partial derivatives:**
  $\[
  \frac{\partial f}{\partial x} = 2xy
  \]$
  
  $\[
  \frac{\partial f}{\partial y} = x^2 + 9y^2
  \]$

- **Total derivative:**
  $\[
  \frac{df}{dt} = (2xy) \frac{dx}{dt} + (x^2 + 9y^2) \frac{dy}{dt}
  \]$

