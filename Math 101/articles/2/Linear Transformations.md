**Linear transformations** are functions between vector spaces that preserve the operations of vector addition and scalar multiplication. They are fundamental in linear algebra and have wide-ranging applications in mathematics, physics, engineering, and computer science. Here's a detailed explanation:

---

### **Definition of a Linear Transformation**

A function $\( T: V \to W \)$ between two vector spaces \( V \) and \( W \) over a field $\( \mathbb{F} \)$ is called a **linear transformation** if it satisfies the following properties for all $\( \vec{u}, \vec{v} \in V \)$ and $\( c \in \mathbb{F} \)$:
1. **Additivity**:
   $\[
   T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}).
   \]$
2. **Homogeneity**:
   $\[
   T(c \vec{u}) = c T(\vec{u}).
   \]$

---

### **Key Concepts**

1. **Matrix Representation**:
   - If \( V \) and \( W \) are finite-dimensional, a linear transformation \( T \) can be represented by a matrix \( A \) such that:
     $\[
     T(\vec{v}) = A \vec{v}.
     \]$
   - The matrix \( A \) depends on the choice of bases for \( V \) and \( W \).

2. **Kernel and Image**:
   - The **kernel** of \( T \) is the set of vectors in \( V \) that map to the zero vector in \( W \):
     $\[
     \ker(T) = \{ \vec{v} \in V \mid T(\vec{v}) = \vec{0} \}.
     \]$
   - The **image** of \( T \) is the set of vectors in \( W \) that are the image of some vector in \( V \):
     $\[
     \text{Im}(T) = \{ T(\vec{v}) \mid \vec{v} \in V \}.
     \]$

3. **Rank-Nullity Theorem**:
   - For a linear transformation $\( T: V \to W \)$:
     $\[
     \dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T)).
     \]$

4. **Invertibility**:
   - A linear transformation \( T \) is **invertible** if there exists a linear transformation $\( T^{-1} \)$ such that:
     $\[
     T^{-1}(T(\vec{v})) = \vec{v} \quad \text{and} \quad T(T^{-1}(\vec{w})) = \vec{w}.
     \]$

5. **Composition of Linear Transformations**:
   - If $\( T: V \to W \)$ and $\( S: W \to U \)$ are linear transformations, their composition $\( S \circ T: V \to U \)$ is also a linear transformation.

---

### **Examples of Linear Transformations**

1. **Rotation in $\( \mathbb{R}^2 \)$**:
   - A rotation by an angle $\( \theta \)$ is a linear transformation represented by the matrix:
```math
     A = \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}.
```

2. **Projection onto a Line**:
   - The projection of a vector $\( \vec{v} \)$ onto a line spanned by $\( \vec{u} \)$ is a linear transformation:
     $\[
     T(\vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\vec{u} \cdot \vec{u}} \vec{u}.
     \]$

3. **Differentiation**:
   - The derivative operator $\( \frac{d}{dx} \)$ is a linear transformation on the space of differentiable functions.

4. **Matrix Multiplication**:
   - For a fixed matrix \( A \), the function $\( T(\vec{v}) = A \vec{v} \)$ is a linear transformation.

---

### **Applications of Linear Transformations**

1. **Physics**:
   - Describes rotations, reflections, and scaling in space.

2. **Engineering**:
   - Analyzes systems of linear equations and control systems.

3. **Computer Graphics**:
   - Represents transformations of 2D and 3D objects.

4. **Machine Learning**:
   - Models data transformations in neural networks.

---

### **Example Problems**

1. **Determine if $\( T: \mathbb{R}^2 \to \mathbb{R}^2 \) defined by \( T(x, y) = (x + y, x - y) \)$ is a linear transformation**:
   - Check additivity:
     $\[
     T((x_1, y_1) + (x_2, y_2)) = T(x_1 + x_2, y_1 + y_2) = (x_1 + x_2 + y_1 + y_2, x_1 + x_2 - y_1 - y_2).
     \]$
     
     $\[
     T(x_1, y_1) + T(x_2, y_2) = (x_1 + y_1, x_1 - y_1) + (x_2 + y_2, x_2 - y_2) = (x_1 + x_2 + y_1 + y_2, x_1 + x_2 - y_1 - y_2).
     \]$
     Thus, $\( T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) \)$.
   - Check homogeneity:
     $\[
     T(c(x, y)) = T(cx, cy) = (cx + cy, cx - cy) = c(x + y, x - y) = c T(x, y).
     \]$
   - Since both properties hold, \( T \) is a linear transformation.

2. **Find the matrix representation of $\( T: \mathbb{R}^2 \to \mathbb{R}^2 \) defined by \( T(x, y) = (2x + y, x - 3y) \)$ with respect to the standard basis**:
   - The standard basis for $\( \mathbb{R}^2 \) is \( \{ \vec{e}_1 = (1, 0), \vec{e}_2 = (0, 1) \} \)$.
   - Compute $\( T(\vec{e}_1) \)$ and $\( T(\vec{e}_2) \)$:
```math
T(\vec{e}_1) = T(1, 0) = (2 \cdot 1 + 0, 1 - 3 \cdot 0) = (2, 1),
```
     
```math
T(\vec{e}_2) = T(0, 1) = (2 \cdot 0 + 1, 0 - 3 \cdot 1) = (1, -3).
```
   - The matrix representation of \( T \) is:
```math
     A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}.
```

3. **Find the kernel and image of

```math
  T: \mathbb{R}^3 \to \mathbb{R}^2 \) defined by \( T(x, y, z) = (x + y, y + z) **:
```
   - **Kernel**:
     Solve $\( T(x, y, z) = (0, 0) \)$:
     $\[
     x + y = 0, \quad y + z = 0.
     \]$
     The solutions are $\( x = -y \), \( z = -y \)$. Thus:
     $\[
     \ker(T) = \{ (-y, y, -y) \mid y \in \mathbb{R} \}.
     \]$
   - **Image**:
     The image is the span of the columns of the matrix representation of \( T \):
```math
     A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}.
```
     The columns are
```math
\begin{bmatrix} 1 \\ 0 \end{bmatrix} \) and \( \begin{bmatrix} 1 \\ 1 \end{bmatrix} \), which span \( \mathbb{R}^2.
```
     Thus:
```math
     \text{Im}(T) = \mathbb{R}^2.
```

4. **Verify the Rank-Nullity Theorem for $\( T: \mathbb{R}^3 \to \mathbb{R}^2 \)$ defined by $\( T(x, y, z) = (x + y, y + z) \)$**:
   - From the previous example:
     $\[
     \dim(\ker(T)) = 1, \quad \dim(\text{Im}(T)) = 2.
     \]$
   - The Rank-Nullity Theorem states:
     $\[
     \dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T)).
     \]$
     Here, $\( \dim(V) = 3 \)$, and:
     $\[
     1 + 2 = 3.
     \]$
     The theorem is verified.

---

### **Key Takeaways**
- Linear transformations preserve vector addition and scalar multiplication.
- They can be represented by matrices and have properties like kernels, images, and invertibility.
- Linear transformations are used in physics, engineering, computer graphics, and machine learning.
- Understanding linear transformations is essential for solving problems in linear algebra and related fields.
