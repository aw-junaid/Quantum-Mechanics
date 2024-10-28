An eigenvector is a concept from linear algebra that is crucial in various areas of mathematics and applied sciences. It is associated with eigenvalues, and together they provide valuable insights into the behavior of linear transformations.

### Definition

Given a square matrix \( A \) and a vector $\( \mathbf{v} \)$, the vector $\( \mathbf{v} \)$ is called an eigenvector of $\( A \)$ if it satisfies the following equation:

$\[
A \mathbf{v} = \lambda \mathbf{v}
\]$

where:
- \( A \) is an $\( n \times n \)$ matrix.
- $\( \mathbf{v} \)$ is a non-zero vector (the eigenvector).
- $\( \lambda \)$ is a scalar (the eigenvalue) associated with the eigenvector $\( \mathbf{v} \)$.

### Key Concepts

1. **Eigenvalue**:
   - The scalar $\( \lambda \)$ is called the eigenvalue corresponding to the eigenvector $\( \mathbf{v} \)$. It indicates how the eigenvector is scaled during the linear transformation represented by \( A \).

2. **Linear Transformation**:
   - The matrix \( A \) represents a linear transformation that acts on vectors. The eigenvector $\( \mathbf{v} \)$ remains in the same direction after the transformation, though it may be scaled by the eigenvalue $\( \lambda \)$.

3. **Eigenvalue Equation**:
   - The eigenvalue equation can be written as:
     $\[
     (A - \lambda I) \mathbf{v} = 0
     \]$
     where \( I \) is the identity matrix of the same dimension as \( A \). For a non-zero eigenvector $\( \mathbf{v} \)$ to exist, the matrix $\( (A - \lambda I) \)$ must be singular, meaning its determinant is zero:
     $\[
     \det(A - \lambda I) = 0
     \]$

4. **Finding Eigenvalues and Eigenvectors**:
   - **Eigenvalues** are found by solving the characteristic polynomial:
     $\[
     \det(A - \lambda I) = 0
     \]$
   - **Eigenvectors** are found by substituting each eigenvalue $\( \lambda \)$ back into the equation $\( (A - \lambda I) \mathbf{v} = 0 \)$ and solving for $\( \mathbf{v} \)$.

### Example

Consider the matrix:
$\[
A = \begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}
\]$

To find the eigenvalues, solve the characteristic polynomial:
$\[
\det(A - \lambda I) = \det \begin{pmatrix}
4 - \lambda & 1 \\
2 & 3 - \lambda
\end{pmatrix}
= (4 - \lambda)(3 - \lambda) - 2 \cdot 1
= \lambda^2 - 7\lambda + 10
\]$

Set the polynomial equal to zero to find the eigenvalues:
$\[
\lambda^2 - 7\lambda + 10 = 0
\]$
Solving this quadratic equation gives:
$\[
\lambda_1 = 5 \quad \text{and} \quad \lambda_2 = 2
\]$

For each eigenvalue, find the corresponding eigenvector:

1. **For**:
   Solve:
   $\[
   (A - 5I) \mathbf{v} = \begin{pmatrix}
   -1 & 1 \\
   2 & -2
   \end{pmatrix} \mathbf{v} = \mathbf{0}
   \]$
   The eigenvector is $\( \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \)$.

2. **For**:
   Solve:
   $\[
   (A - 2I) \mathbf{v} = \begin{pmatrix}
   2 & 1 \\
   2 & 1
   \end{pmatrix} \mathbf{v} = \mathbf{0}
   \]$
   The eigenvector is $\( \mathbf{v}_2 = \begin{pmatrix} -1 \\ 2 \end{pmatrix} \)$.

### Properties

1. **Eigenvectors and Eigenvalues**:
   - Eigenvectors corresponding to distinct eigenvalues are linearly independent.
   - An $\( n \times n \)$ matrix has \( n \) eigenvalues (counting multiplicities), and the number of linearly independent eigenvectors is equal to the number of distinct eigenvalues if the matrix is diagonalizable.

2. **Diagonalization**:
   - A matrix \( A \) is diagonalizable if there exists a matrix \( P \) such that $\( P^{-1}AP \)$ is a diagonal matrix with the eigenvalues of \( A \) on the diagonal. The columns of \( P \) are the eigenvectors of \( A \).

3. **Stability and Dynamics**:
   - In differential equations and dynamical systems, eigenvalues can indicate stability. For example, in a system of differential equations, eigenvalues with negative real parts generally indicate stable behavior.

### Applications

1. **Physics**:
   - Eigenvectors and eigenvalues are used in quantum mechanics to solve the Schrödinger equation and describe physical systems.

2. **Engineering**:
   - In structural engineering, eigenvectors are used to analyze vibrations and stability of structures.

3. **Data Analysis**:
   - Principal Component Analysis (PCA) uses eigenvectors and eigenvalues to reduce the dimensionality of data and identify important features.

4. **Machine Learning**:
   - Techniques like Singular Value Decomposition (SVD) rely on eigenvectors for tasks such as dimensionality reduction and data compression.

### Summary

Eigenvectors are vectors that, when a linear transformation is applied to them, only get scaled by a corresponding eigenvalue and do not change direction. The process of finding eigenvalues and eigenvectors is fundamental in many areas of mathematics, science, and engineering, providing insights into the properties and behavior of linear systems and transformations.
