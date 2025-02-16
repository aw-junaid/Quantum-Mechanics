# Differential Equations: Definition and Classification

## Definition
A **differential equation** is a mathematical equation that relates a function with its derivatives. It describes how a quantity changes over time or space.

## Classification of Differential Equations
Differential equations are classified based on different criteria:

### 1. Ordinary vs. Partial Differential Equations
- **Ordinary Differential Equation (ODE):** An equation involving a function of a single independent variable and its derivatives.
  
  $\[ \frac{d^n y}{dx^n} + a_{n-1} \frac{d^{n-1} y}{dx^{n-1}} + \dots + a_1 \frac{dy}{dx} + a_0 y = g(x) \]$
  
- **Partial Differential Equation (PDE):** An equation involving partial derivatives of a function with respect to multiple independent variables.
  
  $\[ \frac{\partial^n u}{\partial x^n} + \frac{\partial^m u}{\partial y^m} = g(x, y) \]$

### 2. Order of a Differential Equation
The **order** of a differential equation is the highest derivative that appears in the equation.
- First-order ODE: $\( \frac{dy}{dx} + p(x)y = q(x) \)$
- Second-order ODE: $\( \frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = r(x) \)$

### 3. Linearity
A differential equation is **linear** if it can be written in the form:

$\[ a_n(x) \frac{d^n y}{dx^n} + a_{n-1}(x) \frac{d^{n-1} y}{dx^{n-1}} + \dots + a_1(x) \frac{dy}{dx} + a_0(x)y = g(x) \]$

where \( y \) and its derivatives appear to the first power and are not multiplied together.
- **Linear ODE Example:** $\( \frac{d^2 y}{dx^2} + 3 \frac{dy}{dx} + 2y = x \)$
- **Nonlinear ODE Example:** $\( \left(\frac{dy}{dx}\right)^2 + y = x \)$

### 4. Homogeneous vs. Non-Homogeneous Equations
- **Homogeneous:** If the equation can be written as $\( L(y) = 0 \)$, where \( L \) is a linear operator.
- **Non-Homogeneous:** If the equation has a nonzero term, i.e., $\( L(y) = g(x) \)$.

## Summary Table
| Type               | Description |
|-------------------|-------------|
| **ODE** | Involves derivatives with respect to one variable |
| **PDE** | Involves partial derivatives with respect to multiple variables |
| **First Order** | Highest derivative is first order |
| **Second Order** | Highest derivative is second order |
| **Linear** | No product of derivatives, appears to first power |
| **Nonlinear** | Contains nonlinear terms in function or its derivatives |
| **Homogeneous** | Right-hand side is zero |
| **Non-Homogeneous** | Right-hand side is nonzero |

## Conclusion
Understanding the classification of differential equations is essential for selecting appropriate solution techniques. Depending on whether an equation is an ODE or PDE, its order, and whether it is linear or nonlinear, different methods are applied to solve them.

