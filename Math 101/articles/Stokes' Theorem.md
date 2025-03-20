**Stokes' Theorem** is a fundamental result in vector calculus that relates a surface integral of the curl of a vector field to a line integral of the vector field around the boundary of the surface. It generalizes Green's theorem to higher dimensions and is widely used in physics and engineering. Here's a detailed explanation:

---

### **Statement of Stokes' Theorem**

Let \( S \) be an oriented surface with boundary $\( \partial S \)$, and let $\( \vec{F} \)$ be a vector field defined on \( S \). Stokes' theorem states:
$\[
\iint_S (\nabla \times \vec{F}) \cdot d\vec{S} = \oint_{\partial S} \vec{F} \cdot d\vec{r},
\]$
where:
- $\( \nabla \times \vec{F} \)$: The curl of $\( \vec{F} \)$.
- $\( d\vec{S} \)$: The differential area vector normal to \( S \).
- $\( d\vec{r} \)$: The differential displacement vector along $\( \partial S \)$.

---

### **Key Concepts**

1. **Curl of a Vector Field**:
   - The curl of $\( \vec{F} = P \hat{i} + Q \hat{j} + R \hat{k} \)$ is:
     $\[
     \nabla \times \vec{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) \hat{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) \hat{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \hat{k}.
     \]$

2. **Orientation**:
   - The surface \( S \) and its boundary $\( \partial S \)$ must be consistently oriented. The normal vector $\( d\vec{S} \)$ and the direction of $\( d\vec{r} \)$ follow the right-hand rule.

3. **Special Cases**:
   - If \( S \) is a flat region in the \( xy \)-plane, Stokes' theorem reduces to Green's theorem:
     $\[
     \iint_S \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \oint_{\partial S} P \, dx + Q \, dy.
     \]$

---

### **Applications of Stokes' Theorem**

1. **Physics**:
   - Relates the circulation of a vector field (e.g., fluid flow) to the curl of the field.

2. **Engineering**:
   - Analyzes electromagnetic fields and fluid dynamics.

3. **Mathematics**:
   - Provides a tool for converting surface integrals into line integrals and vice versa.

---

### **Example Problems**

1. **Verify Stokes' theorem for $\( \vec{F}(x, y, z) = -y \hat{i} + x \hat{j} + z \hat{k} \)$ over the surface \( S \) of the paraboloid $\( z = 1 - x^2 - y^2 \)$ bounded by the plane $\( z = 0 \)$**:
   - Compute the curl of $\( \vec{F} \)$:
     $\[
     \nabla \times \vec{F} = \left( \frac{\partial z}{\partial y} - \frac{\partial x}{\partial z} \right) \hat{i} + \left( \frac{\partial (-y)}{\partial z} - \frac{\partial z}{\partial x} \right) \hat{j} + \left( \frac{\partial x}{\partial x} - \frac{\partial (-y)}{\partial y} \right) \hat{k} = (0 - 0) \hat{i} + (0 - 0) \hat{j} + (1 + 1) \hat{k} = 2 \hat{k}.
     \]$
   - Compute the surface integral:
     $\[
     \iint_S (\nabla \times \vec{F}) \cdot d\vec{S} = \iint_S 2 \hat{k} \cdot d\vec{S}.
     \]$
     The surface \( S \) is the paraboloid $\( z = 1 - x^2 - y^2 \)$, and its projection onto the \( xy \)-plane is the unit disk $\( x^2 + y^2 \leq 1 \)$. The differential area vector is:
     $\[
     d\vec{S} = \left( -\frac{\partial z}{\partial x}, -\frac{\partial z}{\partial y}, 1 \right) dx \, dy = (2x, 2y, 1) dx \, dy.
     \]$
     Thus:
     $\[
     \iint_S 2 \hat{k} \cdot (2x, 2y, 1) dx \, dy = \iint_S 2 dx \, dy.
     \]$
     The area of the unit disk is $\( \pi \)$, so:
     $\[
     \iint_S 2 dx \, dy = 2 \pi.
     \]$
   - Compute the line integral:
     The boundary $\( \partial S \)$ is the circle $\( x^2 + y^2 = 1 \)$ in the \( xy \)-plane. Parameterize the circle:
     $\[
     \vec{r}(t) = \cos(t) \hat{i} + \sin(t) \hat{j}, \quad 0 \leq t \leq 2\pi.
     \]$
     The differential displacement vector is:
     $\[
     d\vec{r} = (-\sin(t) \hat{i} + \cos(t) \hat{j}) dt.
     \]$
     Evaluate $\( \vec{F} \)$ on the boundary:
     $\[
     \vec{F}(\vec{r}(t)) = -\sin(t) \hat{i} + \cos(t) \hat{j} + 0 \hat{k}.
     \]$
     Compute the line integral:
     $\[
     \oint_{\partial S} \vec{F} \cdot d\vec{r} = \int_0^{2\pi} (-\sin(t) \hat{i} + \cos(t) \hat{j}) \cdot (-\sin(t) \hat{i} + \cos(t) \hat{j}) dt = \int_0^{2\pi} (\sin^2(t) + \cos^2(t)) dt = \int_0^{2\pi} 1 dt = 2\pi.
     \]$
   - Stokes' theorem is verified since both integrals equal $\( 2\pi \)$.

2. **Use Stokes' theorem to evaluate $\( \iint_S (\nabla \times \vec{F}) \cdot d\vec{S} \)$ for $\( \vec{F}(x, y, z) = y \hat{i} + z \hat{j} + x \hat{k} \)$ over the surface \( S \) of the hemisphere $\( x^2 + y^2 + z^2 = 1 \), \( z \geq 0 \)$**:
   - Compute the curl of $\( \vec{F} \)$:
     $\[
     \nabla \times \vec{F} = \left( \frac{\partial x}{\partial y} - \frac{\partial z}{\partial z} \right) \hat{i} + \left( \frac{\partial y}{\partial z} - \frac{\partial x}{\partial x} \right) \hat{j} + \left( \frac{\partial z}{\partial x} - \frac{\partial y}{\partial y} \right) \hat{k} = (0 - 1) \hat{i} + (0 - 1) \hat{j} + (0 - 1) \hat{k} = -\hat{i} - \hat{j} - \hat{k}.
     \]$
   - Compute the surface integral:
     $\[
     \iint_S (\nabla \times \vec{F}) \cdot d\vec{S} = \iint_S (-\hat{i} - \hat{j} - \hat{k}) \cdot d\vec{S}.
     \]$
     The surface $\( S \)$ is the upper hemisphere, and its boundary $\( \partial S \)$ is the circle $\( x^2 + y^2 = 1 \)$ in the \( xy \)-plane. By Stokes' theorem:
     $\[
     \iint_S (\nabla \times \vec{F}) \cdot d\vec{S} = \oint_{\partial S} \vec{F} \cdot d\vec{r}.
     \]$
   - Compute the line integral:
     Parameterize the boundary $\( \partial S \)$:
     $\[
     \vec{r}(t) = \cos(t) \hat{i} + \sin(t) \hat{j}, \quad 0 \leq t \leq 2\pi.
     \]$
     The differential displacement vector is:
     $\[
     d\vec{r} = (-\sin(t) \hat{i} + \cos(t) \hat{j}) dt.
     \]$
     Evaluate $\( \vec{F} \)$ on the boundary:
     $\[
     \vec{F}(\vec{r}(t)) = \sin(t) \hat{i} + 0 \hat{j} + \cos(t) \hat{k}.
     \]$
     Compute the line integral:
     $\[
     \oint_{\partial S} \vec{F} \cdot d\vec{r} = \int_0^{2\pi} (\sin(t) \hat{i} + 0 \hat{j} + \cos(t) \hat{k}) \cdot (-\sin(t) \hat{i} + \cos(t) \hat{j}) dt = \int_0^{2\pi} (-\sin^2(t)) dt = -\pi.
     \]$
   - The surface integral is $\( -\pi \)$.

---

### **Key Takeaways**
- Stokes' theorem relates the surface integral of the curl of a vector field to the line integral of the field around the boundary of the surface.
- It generalizes Green's theorem to higher dimensions and is essential in physics and engineering.
- Understanding Stokes' theorem is crucial for solving problems involving circulation and flux in 3D space.
