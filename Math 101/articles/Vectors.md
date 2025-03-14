Vectors are mathematical objects that have both **magnitude** (size) and **direction**. They are fundamental in physics, engineering, computer graphics, and many areas of mathematics. Vectors can represent quantities like force, velocity, and displacement. Here's a detailed explanation:

---

### **Definition of a Vector**

A vector is typically represented as an ordered list of numbers (components) in a coordinate system. In 2D, a vector $\( \vec{v} \)$ is written as:
$\[
\vec{v} = \langle v_1, v_2 \rangle,
\]$
and in 3D, it is written as:
$\[
\vec{v} = \langle v_1, v_2, v_3 \rangle.
\]$
- $\( v_1, v_2, v_3 \)$: Components of the vector along the $\( x \), \( y \), and \( z \)$ axes, respectively.

---

### **Key Concepts**

1. **Magnitude (Length) of a Vector**:
   - The magnitude of a vector $\( \vec{v} = \langle v_1, v_2 \rangle \)$ in 2D is:
     $\[
     \|\vec{v}\| = \sqrt{v_1^2 + v_2^2}.
     \]$
   - In 3D, for $\( \vec{v} = \langle v_1, v_2, v_3 \rangle \)$:
     $\[
     \|\vec{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}.
     \]$

2. **Direction of a Vector**:
   - The direction of a vector is often described by the angle it makes with a reference axis (e.g., the positive \( x \)-axis).

3. **Unit Vector**:
   - A vector with a magnitude of 1. It is obtained by dividing a vector by its magnitude:
     $\[
     \hat{u} = \frac{\vec{v}}{\|\vec{v}\|}.
     \]$

4. **Position Vector**:
   - A vector that represents the position of a point relative to an origin.

5. **Vector Addition and Subtraction**:
   - Vectors are added or subtracted component-wise:
     $\[
     \vec{u} + \vec{v} = \langle u_1 + v_1, u_2 + v_2 \rangle,
     \]$
     
     $\[
     \vec{u} - \vec{v} = \langle u_1 - v_1, u_2 - v_2 \rangle.
     \]$

6. **Scalar Multiplication**:
   - A vector is multiplied by a scalar (a real number) component-wise:
     $\[
     c\vec{v} = \langle c v_1, c v_2 \rangle.
     \]$

---

### **Operations on Vectors**

1. **Dot Product (Scalar Product)**:
   - The dot product of two vectors $\( \vec{u} = \langle u_1, u_2 \rangle \)$ and $\( \vec{v} = \langle v_1, v_2 \rangle \)$ is:
     $\[
     \vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2.
     \]$
   - In 3D:
     $\[
     \vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + u_3 v_3.
     \]$
   - The dot product measures the similarity between two vectors and is used to calculate angles between them:
     $\[
     \cos(\theta) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}.
     \]$

2. **Cross Product (Vector Product)**:
   - The cross product of two 3D vectors $\( \vec{u} = \langle u_1, u_2, u_3 \rangle \) and \( \vec{v} = \langle v_1, v_2, v_3 \rangle \)$ is:
     $\[
     \vec{u} \times \vec{v} = \langle u_2 v_3 - u_3 v_2, u_3 v_1 - u_1 v_3, u_1 v_2 - u_2 v_1 \rangle.
     \]$
   - The cross product produces a vector perpendicular to both $\( \vec{u} \) and \( \vec{v} \)$, with magnitude equal to the area of the parallelogram formed by $\( \vec{u} \) and \( \vec{v} \)$.

3. **Projection**:
   - The projection of $\( \vec{u} \)$ onto $\( \vec{v} \)$ is:
     $\[
     \text{proj}_{\vec{v}} \vec{u} = \left( \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|^2} \right) \vec{v}.
     \]$

---

### **Applications of Vectors**

1. **Physics**:
   - Represent forces, velocity, acceleration, and displacement.

2. **Engineering**:
   - Analyze structures, fluid flow, and electromagnetic fields.

3. **Computer Graphics**:
   - Represent and manipulate 3D objects, lighting, and animations.

4. **Navigation**:
   - Calculate directions and distances.

5. **Mathematics**:
   - Solve systems of equations, study geometry, and perform linear algebra.

---

### **Example Problems**

1. **Find the magnitude of $\( \vec{v} = \langle 3, 4 \rangle \)$**:
   $\[
   \|\vec{v}\| = \sqrt{3^2 + 4^2} = 5.
   \]$

2. **Add $\( \vec{u} = \langle 1, 2 \rangle \) and \( \vec{v} = \langle 3, 4 \rangle \)$**:
   $\[
   \vec{u} + \vec{v} = \langle 1 + 3, 2 + 4 \rangle = \langle 4, 6 \rangle.
   \]$

3. **Compute the dot product of $\( \vec{u} = \langle 1, 2 \rangle \) and \( \vec{v} = \langle 3, 4 \rangle \)$**:
   $\[
   \vec{u} \cdot \vec{v} = (1)(3) + (2)(4) = 11.
   \]$

4. **Find the angle between $\( \vec{u} = \langle 1, 0 \rangle \) and \( \vec{v} = \langle 0, 1 \rangle \)$**:
   - Compute the dot product and magnitudes:
     $\[
     \vec{u} \cdot \vec{v} = 0, \quad \|\vec{u}\| = 1, \quad \|\vec{v}\| = 1.
     \]$
   - Use the dot product formula:
     $\[
     \cos(\theta) = \frac{0}{1 \cdot 1} = 0 \implies \theta = 90^\circ.
     \]$

5. **Compute the cross product of $\( \vec{u} = \langle 1, 0, 0 \rangle \) and \( \vec{v} = \langle 0, 1, 0 \rangle \)$**:
   $\[
   \vec{u} \times \vec{v} = \langle (0)(0) - (0)(1), (0)(0) - (1)(0), (1)(1) - (0)(0) \rangle = \langle 0, 0, 1 \rangle.
   \]$

---

### **Key Takeaways**
- Vectors have both magnitude and direction and are represented as ordered lists of components.
- Operations like addition, subtraction, dot product, and cross product are fundamental to vector analysis.
- Vectors are widely used in physics, engineering, computer graphics, and mathematics.
- Understanding vectors is essential for solving problems involving direction and magnitude.
