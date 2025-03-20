**Sturm-Liouville (S-L) problems** are a class of differential equations that arise in the study of boundary value problems. They are named after mathematicians Jacques Charles François Sturm and Joseph Liouville. S-L problems are essential in mathematical physics, engineering, and applied mathematics because they describe many physical phenomena, such as vibrations, heat conduction, and quantum mechanics. Here's a detailed explanation:

---

### **Definition of Sturm-Liouville Problems**

A Sturm-Liouville problem consists of a second-order linear differential equation of the form:
$\[
\frac{d}{dx} \left[ p(x) \frac{dy}{dx} \right] + q(x) y + \lambda w(x) y = 0,
\]$
where:
- $\( p(x) \), \( q(x) \), and \( w(x) \)$ are given functions.
- $\( \lambda \)$ is a parameter (eigenvalue).
- $\( y(x) \)$ is the unknown function (eigenfunction).

The equation is typically defined on an interval $\( [a, b] \)$ and is accompanied by boundary conditions, such as:
1. **Dirichlet boundary conditions**: $\( y(a) = 0 \), \( y(b) = 0 \)$.
2. **Neumann boundary conditions**: $\( y'(a) = 0 \), \( y'(b) = 0 \)$.
3. **Mixed boundary conditions**: A combination of Dirichlet and Neumann conditions.

---

### **Key Concepts**

1. **Eigenvalues and Eigenfunctions**:
   - The values of $\( \lambda \)$ for which nontrivial solutions $\( y(x) \)$ exist are called **eigenvalues**.
   - The corresponding solutions $\( y(x) \)$ are called **eigenfunctions**.

2. **Weight Function**:
   - The function $\( w(x) \)$ is called the **weight function** or **density function**. It determines the orthogonality of the eigenfunctions.

3. **Orthogonality**:
   - Eigenfunctions corresponding to distinct eigenvalues are orthogonal with respect to the weight function \( w(x) \):
     $\[
     \int_a^b y_m(x) y_n(x) w(x) \, dx = 0 \quad \text{if} \quad \lambda_m \neq \lambda_n.
     \]$

4. **Regular and Singular S-L Problems**:
   - A **regular S-L problem** satisfies:
     - $\( p(x) > 0 \) and \( w(x) > 0 \) on \( [a, b] \)$.
     - $\( p(x) \), \( q(x) \), and \( w(x) \)$ are continuous on $\( [a, b] \)$.
   - A **singular S-L problem** occurs when these conditions are not met (e.g., $\( p(x) = 0 \)$ at an endpoint).

---

### **Applications of Sturm-Liouville Problems**

1. **Vibrations**:
   - Describes the modes of vibration of a string, membrane, or beam.

2. **Heat Conduction**:
   - Models the temperature distribution in a rod or plate.

3. **Quantum Mechanics**:
   - Solves the Schrödinger equation for potential wells and harmonic oscillators.

4. **Electromagnetism**:
   - Analyzes wave propagation in waveguides and cavities.

---

### **Example Problems**

1. **Solve the S-L problem $\( y'' + \lambda y = 0 \)$ with boundary conditions $\( y(0) = 0 \), \( y(L) = 0 \)$**:
   - The general solution is:
     $\[
     y(x) = A \cos(\sqrt{\lambda} x) + B \sin(\sqrt{\lambda} x).
     \]$
   - Apply the boundary condition $\( y(0) = 0 \)$:
     $\[
     y(0) = A \cos(0) + B \sin(0) = A = 0.
     \]$
     Thus, $\( y(x) = B \sin(\sqrt{\lambda} x) \)$.
   - Apply the boundary condition $\( y(L) = 0 \)$:
     $\[
     y(L) = B \sin(\sqrt{\lambda} L) = 0.
     \]$
     For nontrivial solutions, $\( \sin(\sqrt{\lambda} L) = 0 \)$, so:
     $\[
     \sqrt{\lambda} L = n \pi \implies \lambda_n = \left( \frac{n \pi}{L} \right)^2, \quad n = 1, 2, 3, \dots.
     \]$
   - The eigenvalues are $\( \lambda_n = \left( \frac{n \pi}{L} \right)^2 \)$, and the eigenfunctions are:
     $\[
     y_n(x) = \sin\left( \frac{n \pi x}{L} \right).
     \]$

2. **Solve the S-L problem $\( y'' + \lambda y = 0 \)$ with boundary conditions $\( y'(0) = 0 \), \( y'(L) = 0 \)$**:
   - The general solution is:
     $\[
     y(x) = A \cos(\sqrt{\lambda} x) + B \sin(\sqrt{\lambda} x).
     \]$
   - Apply the boundary condition $\( y'(0) = 0 \)$:
     $\[
     y'(x) = -A \sqrt{\lambda} \sin(\sqrt{\lambda} x) + B \sqrt{\lambda} \cos(\sqrt{\lambda} x),
     \]$
     
     $\[
     y'(0) = B \sqrt{\lambda} = 0 \implies B = 0.
     \]$
     Thus, $\( y(x) = A \cos(\sqrt{\lambda} x) \)$.
   - Apply the boundary condition $\( y'(L) = 0 \)$:
     $\[
     y'(L) = -A \sqrt{\lambda} \sin(\sqrt{\lambda} L) = 0.
     \]$
     For nontrivial solutions, $\( \sin(\sqrt{\lambda} L) = 0 \)$, so:
     $\[
     \sqrt{\lambda} L = n \pi \implies \lambda_n = \left( \frac{n \pi}{L} \right)^2, \quad n = 0, 1, 2, \dots.
     \]$
   - The eigenvalues are $\( \lambda_n = \left( \frac{n \pi}{L} \right)^2 \)$, and the eigenfunctions are:
     $\[
     y_n(x) = \cos\left( \frac{n \pi x}{L} \right).
     \]$

3. **Solve the S-L problem $\( x^2 y'' + x y' + \lambda y = 0 \)$ with boundary conditions $\( y(1) = 0 \), \( y(e^\pi) = 0 \)$**:
   - Rewrite the equation in standard S-L form:
     $\[
     \frac{d}{dx} \left( x \frac{dy}{dx} \right) + \frac{\lambda}{x} y = 0.
     \]$
   - The general solution is:
     $\[
     y(x) = A \cos(\sqrt{\lambda} \ln(x)) + B \sin(\sqrt{\lambda} \ln(x)).
     \]$
   - Apply the boundary condition $\( y(1) = 0 \)$:
     $\[
     y(1) = A \cos(0) + B \sin(0) = A = 0.
     \]$
     Thus, $\( y(x) = B \sin(\sqrt{\lambda} \ln(x)) \)$.
   - Apply the boundary condition $\( y(e^\pi) = 0 \)$:
     $\[
     y(e^\pi) = B \sin(\sqrt{\lambda} \pi) = 0.
     \]$
     For nontrivial solutions, $\( \sin(\sqrt{\lambda} \pi) = 0 \)$, so:
     $\[
     \sqrt{\lambda} \pi = n \pi \implies \lambda_n = n^2, \quad n = 1, 2, 3, \dots.
     \]$
   - The eigenvalues are $\( \lambda_n = n^2 \)$, and the eigenfunctions are:
     $\[
     y_n(x) = \sin(n \ln(x)).
     \]$

---

### **Key Takeaways**
- Sturm-Liouville problems are second-order differential equations with boundary conditions.
- They involve eigenvalues and eigenfunctions, which are orthogonal with respect to a weight function.
- S-L problems are used to model physical phenomena like vibrations, heat conduction, and quantum mechanics.
- Understanding S-L problems is essential for solving boundary value problems in applied mathematics.
