**Eigenvalues** are a fundamental concept in linear algebra that describe the scaling factor of a linear transformation along specific directions (called **eigenvectors**). They are widely used in physics, engineering, computer science, and other fields to analyze systems, solve differential equations, and perform data transformations. Here's a detailed explanation:

---

### **Definition of Eigenvalues**

For a square matrix \( A \) of size $\( n \times n \)$, an **eigenvalue** $\( \lambda \)$ is a scalar such that:
$\[
A \vec{v} = \lambda \vec{v},
\]$
where:
- $\( \vec{v} \)$ is a nonzero vector called an **eigenvector**.
- $\( \lambda \)$ is the eigenvalue corresponding to $\( \vec{v} \)$.

---

### **Key Concepts**

1. **Characteristic Equation**:
   - The eigenvalues of \( A \) are the roots of the **characteristic polynomial**:
     $\[
     \det(A - \lambda I) = 0,
     \]$
     where \( I \) is the identity matrix of the same size as \( A \).

2. **Eigenvectors**:
- For each eigenvalue $\( \lambda \)$, the corresponding eigenvectors are the nonzero solutions to:
$\[
(A - \lambda I) \vec{v} = \vec{0}.
\]$

3. **Geometric and Algebraic Multiplicity**:
   - The **algebraic multiplicity** of an eigenvalue is the number of times it appears as a root of the characteristic polynomial.
   - The **geometric multiplicity** is the number of linearly independent eigenvectors corresponding to the eigenvalue.

4. **Diagonalization**:
   - A matrix \( A \) is **diagonalizable** if it can be written as:
     $\[
     A = P D P^{-1},
     \]$
     where \( D \) is a diagonal matrix of eigenvalues, and \( P \) is a matrix of eigenvectors.

5. **Spectral Theorem**:
   - For a symmetric matrix \( A \), all eigenvalues are real, and \( A \) can be diagonalized by an orthogonal matrix.

---

### **Applications of Eigenvalues**

1. **Physics**:
   - Describes the stability of systems, quantum mechanics, and vibrations.

2. **Engineering**:
   - Analyzes structural stability, control systems, and signal processing.

3. **Computer Science**:
   - Used in machine learning (e.g., PCA), graph theory, and data compression.

4. **Economics**:
   - Models input-output systems and optimization problems.

---

### **Example Problems**

1. **Find the eigenvalues and eigenvectors of

```math
3. A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \)
```
   - Compute the characteristic polynomial:
```math
\det(A - \lambda I) = \det \begin{bmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{bmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4 \lambda + 3.
```
Solve $\( \lambda^2 - 4 \lambda + 3 = 0 \)$:
$\[
\lambda = 1, 3.
\]$
   - For $\( \lambda = 1 \)$:
     Solve $\( (A - I) \vec{v} = \vec{0} \)$:
```math
     \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
```
     The eigenvector is
```math
\vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.
```
   - For $\( \lambda = 3 \)$:
     Solve $\( (A - 3I) \vec{v} = \vec{0} \)$:
```math
\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
```
The eigenvector is 

```math
\( \vec{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \).
```

2. Diagonalize the matrix

```math
 A = \begin{bmatrix} 4 & 1 \\ 0 & 4 \end{bmatrix}
```
   - The eigenvalues are $\( \lambda = 4 \)$ (double root).
   - The eigenvector equation $\( (A - 4I) \vec{v} = \vec{0} \)$ gives:
```math
     \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
```
The only eigenvector is

```math
 \vec{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
```
- Since there is only one linearly independent eigenvector, $\( A \)$ is not diagonalizable.

3. **Find the eigenvalues of

```math
A = \begin{bmatrix} 3 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}
```
   - The characteristic polynomial is:
```math
     \det(A - \lambda I) = \det \begin{bmatrix} 3 - \lambda & 0 & 0 \\ 0 & 2 - \lambda & 1 \\ 0 & 0 & 2 - \lambda \end{bmatrix} = (3 - \lambda)(2 - \lambda)^2.
```

The eigenvalues are $\( \lambda = 3 \)$ (algebraic multiplicity 1) and $\( \lambda = 2 \)$ (algebraic multiplicity 2).

4. **Verify the Spectral Theorem for
```math
 A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} 
```
   - The eigenvalues are $\( \lambda = 1 \)$ and $\( \lambda = 3 \)$, which are real.
   - The eigenvectors are
```math
   \( \vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix} \) and \( \vec{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \),
```
   which are orthogonal.
   - The matrix \( A \) can be diagonalized as:
```math
     A = P D P^{-1}, \quad \text{where} \quad P = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix}.
```

---

### **Key Takeaways**
- Eigenvalues describe the scaling factor of a linear transformation along specific directions (eigenvectors).
- They are found by solving the characteristic equation $\( \det(A - \lambda I) = 0 \)$.
- Eigenvalues and eigenvectors are used in diagonalization, stability analysis, and data transformations.
- Understanding eigenvalues is essential for solving problems in linear algebra and applied mathematics.
