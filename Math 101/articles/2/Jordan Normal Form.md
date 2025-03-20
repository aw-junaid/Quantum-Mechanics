The **Jordan normal form** (or **Jordan canonical form**) is a way of representing a square matrix in a block-diagonal form, where each block (called a **Jordan block**) has a specific structure. It is a powerful tool in linear algebra for understanding the structure of linear transformations and solving systems of differential equations. Here's a detailed explanation:

---

### **Definition of Jordan Normal Form**

Given a square matrix \( A \) of size $\( n \times n \)$, its Jordan normal form is a block-diagonal matrix \( J \) such that:
```math
A = P J P^{-1},
```
where:
- \( P \) is an invertible matrix (the **transition matrix**).
- \( J \) is a block-diagonal matrix consisting of **Jordan blocks**.

A **Jordan block** is a matrix of the form:
```math
J_\lambda = \begin{bmatrix}
\lambda & 1 & 0 & \dots & 0 \\
0 & \lambda & 1 & \dots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \dots & \lambda & 1 \\
0 & 0 & \dots & 0 & \lambda
\end{bmatrix},
```
where $\( \lambda \)$ is an eigenvalue of \( A \).

---

### **Key Concepts**

1. **Eigenvalues and Eigenvectors**:
   - The eigenvalues of \( A \) are the values $\( \lambda \)$ for which $\( \det(A - \lambda I) = 0 \)$.
   - The eigenvectors are the vectors $\( \vec{v} \)$ such that $\( A \vec{v} = \lambda \vec{v} \)$.

2. **Generalized Eigenvectors**:
   - If \( A \) does not have enough linearly independent eigenvectors, **generalized eigenvectors** are used to form the Jordan basis.
   - A generalized eigenvector of rank \( k \) satisfies:
```math
     (A - \lambda I)^k \vec{v} = \vec{0}, \quad \text{but} \quad (A - \lambda I)^{k-1} \vec{v} \neq \vec{0}.
```

3. **Jordan Chain**:
   - A sequence of generalized eigenvectors $\( \vec{v}_1, \vec{v}_2, \dots, \vec{v}_k \)$ such that:
```math
     (A - \lambda I) \vec{v}_1 = \vec{0}, \quad (A - \lambda I) \vec{v}_2 = \vec{v}_1, \quad \dots, \quad (A - \lambda I) \vec{v}_k = \vec{v}_{k-1}.
```

4. **Jordan Basis**:
   - A basis of $\( \mathbb{C}^n \)$ consisting of eigenvectors and generalized eigenvectors.

---

### **Steps to Find the Jordan Normal Form**

1. **Find the Eigenvalues**:
   - Compute the characteristic polynomial $\( \det(A - \lambda I) \)$ and solve for $\( \lambda \)$.

2. **Find the Eigenvectors and Generalized Eigenvectors**:
   - For each eigenvalue $\( \lambda \)$, find the eigenvectors and generalized eigenvectors.

3. **Form the Jordan Chains**:
   - Arrange the eigenvectors and generalized eigenvectors into Jordan chains.

4. **Construct the Transition Matrix \( P \)**:
   - Use the Jordan chains as columns of \( P \).

5. **Construct the Jordan Matrix \( J \)**:
   - Place the Jordan blocks corresponding to each eigenvalue along the diagonal of \( J \).

---

### **Applications of Jordan Normal Form**

1. **Solving Systems of Differential Equations**:
   - The Jordan form simplifies the solution of $\( \frac{d\vec{x}}{dt} = A \vec{x} \)$.

2. **Matrix Exponentiation**:
   - The Jordan form makes it easier to compute $\( e^{A t} \)$.

3. **Stability Analysis**:
   - The Jordan form helps analyze the stability of dynamical systems.

4. **Linear Algebra**:
   - Provides insight into the structure of linear transformations.

---

### **Example Problems**

1. Find the Jordan normal form of

```math
\( A = \begin{bmatrix} 4 & 1 \\ 0 & 4 \end{bmatrix} \)
```

   - The eigenvalue is $\( \lambda = 4 \)$ (double root).
   - The eigenvector equation $\( (A - 4I) \vec{v} = \vec{0} \)$ gives:
```math
     \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
```
     The only eigenvector is
```math
     \( \vec{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \)
```

   - Find a generalized eigenvector $\( \vec{v}_2 \)$ such that $\( (A - 4I) \vec{v}_2 = \vec{v}_1 \)$:
```math
     \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}.
```
     The solution is
```math
     \vec{v}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
```
   - The transition matrix is:
```math
     P = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.
```
   - The Jordan normal form is:
```math
     J = \begin{bmatrix} 4 & 1 \\ 0 & 4 \end{bmatrix}.
```

2. Find the Jordan normal form of
```math
 A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}
```
   - The eigenvalue is $\( \lambda = 2 \)$ (triple root).
   - The eigenvector equation $\( (A - 2I) \vec{v} = \vec{0} \)$ gives:
```math
     \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.
```
     The only eigenvector is
```math
     \vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
```
 
   - Find generalized eigenvectors $\( \vec{v}_2 \) and \( \vec{v}_3 \)$ such that:
```math
     (A - 2I) \vec{v}_2 = \vec{v}_1, \quad (A - 2I) \vec{v}_3 = \vec{v}_2.
```
     Solving:
```math
     \vec{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
```
   - The transition matrix is:
```math
     P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.
```
   - The Jordan normal form is:
```math
     J = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}.
```

3. **Find the Jordan normal form of

```math
 A = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}
```
   - The eigenvalues are $\( \lambda = 3 \)$ (double root) and $\( \lambda = 2 \)$.
   - For $\( \lambda = 3 \)$:
     - The eigenvector equation $\( (A - 3I) \vec{v} = \vec{0} \)$ gives:
     - 
```math
       \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.
```
       The eigenvectors are 
```math       
vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \) and vec{v}_2 = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.
```     
     - Find a generalized eigenvector 
```math  
      vec{v}_3  such that  (A - 3I) vec{v}_3 = vec{v}_1:
```
 
```math
       \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}.
```
       The solution is
```math
\vec{v}_3 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}.
```
   - For $\( \lambda = 2 \)$:
     - The eigenvector equation $\( (A - 2I) \vec{v} = \vec{0} \)$ gives:
```math
       \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}.
```
       The eigenvector is
```math
vec{v}_4 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
```.
   - The transition matrix is:
```math
     P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.
```
   - The Jordan normal form is:
```math
     J = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}.
```

---

### **Key Takeaways**
- The Jordan normal form is a block-diagonal representation of a matrix using Jordan blocks.
- It is useful for solving systems of differential equations, matrix exponentiation, and stability analysis.
- The Jordan form is constructed using eigenvalues, eigenvectors, and generalized eigenvectors.
- Understanding the Jordan normal form is essential for advanced studies in linear algebra and differential equations.
