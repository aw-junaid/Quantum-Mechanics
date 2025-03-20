The **Divergence Theorem**, also known as **Gauss's Theorem**, is a fundamental result in vector calculus that relates the flux of a vector field through a closed surface to the divergence of the field within the volume enclosed by the surface. It is widely used in physics, engineering, and mathematics to simplify calculations involving flux and volume integrals. Here's a detailed explanation:

---

### **Statement of the Divergence Theorem**

Let \( V \) be a solid region in 3D space bounded by a closed surface \( S \), and let $\( \vec{F} \)$ be a vector field defined on \( V \). The Divergence Theorem states:
$\[
\iiint_V (\nabla \cdot \vec{F}) \, dV = \iint_S \vec{F} \cdot d\vec{S},
\]$
where:
- $\( \nabla \cdot \vec{F} \)$: The divergence of $\( \vec{F} \)$.
- \( dV \): The differential volume element in \( V \).
- $\( d\vec{S} \)$: The differential area vector normal to \( S \).

---

### **Key Concepts**

1. **Divergence of a Vector Field**:
   - The divergence of $\( \vec{F} = P \hat{i} + Q \hat{j} + R \hat{k} \)$ is:
     $\[
     \nabla \cdot \vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}.
     \]$
   - Divergence measures the "outflow" of a vector field from a point.

2. **Flux**:
   - The flux of $\( \vec{F} \)$ through \( S \) is the surface integral $\( \iint_S \vec{F} \cdot d\vec{S} \)$.
   - It represents the total amount of $\( \vec{F} \)$ passing through \( S \).

3. **Orientation**:
   - The surface \( S \) must be oriented outward (the normal vector $\( d\vec{S} \)$ points away from \( V \)).

---

### **Applications of the Divergence Theorem**

1. **Physics**:
   - Relates the flux of a vector field (e.g., electric or gravitational field) through a closed surface to the sources or sinks within the volume.

2. **Fluid Dynamics**:
   - Describes the flow of fluids through a closed surface in terms of the divergence of the velocity field.

3. **Electromagnetism**:
   - Used in Gauss's law for electricity and magnetism.

4. **Engineering**:
   - Analyzes heat transfer, fluid flow, and stress in materials.

---

### **Example Problems**

1. **Verify the Divergence Theorem for $\( \vec{F}(x, y, z) = x \hat{i} + y \hat{j} + z \hat{k} \)$ over the unit sphere $\( x^2 + y^2 + z^2 = 1 \)$**:
   - Compute the divergence of $\( \vec{F} \)$:
     $\[
     \nabla \cdot \vec{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3.
     \]$
   - Compute the volume integral:
     $\[
     \iiint_V (\nabla \cdot \vec{F}) \, dV = \iiint_V 3 \, dV = 3 \cdot \text{Volume of the unit sphere} = 3 \cdot \frac{4}{3} \pi = 4\pi.
     \]$
   - Compute the surface integral:
     The unit sphere has radius 1, and its surface area is $\( 4\pi \)$. The outward unit normal vector is $\( \hat{n} = x \hat{i} + y \hat{j} + z \hat{k} \)$. Thus:
     $\[
     \vec{F} \cdot \hat{n} = (x \hat{i} + y \hat{j} + z \hat{k}) \cdot (x \hat{i} + y \hat{j} + z \hat{k}) = x^2 + y^2 + z^2 = 1.
     \]$
     The surface integral is:
     $\[
     \iint_S \vec{F} \cdot d\vec{S} = \iint_S 1 \, dS = \text{Surface area of the unit sphere} = $4\pi$.
     \]$
   - The Divergence Theorem is verified since both integrals equal \( 4\pi \).

2. **Use the Divergence Theorem to evaluate $\( \iint_S \vec{F} \cdot d\vec{S} \)$ for $\( \vec{F}(x, y, z) = x^2 \hat{i} + y^2 \hat{j} + z^2 \hat{k} \)$ over the surface of the cube $\( 0 \leq x \leq 1 \), \( 0 \leq y \leq 1 \), \( 0 \leq z \leq 1 \)$**:
   - Compute the divergence of $\( \vec{F} \)$:
     $\[
     \nabla \cdot \vec{F} = \frac{\partial}{\partial x}(x^2) + \frac{\partial}{\partial y}(y^2) + \frac{\partial}{\partial z}(z^2) = 2x + 2y + 2z.
     \]$
   - Compute the volume integral:
     $\[
     \iiint_V (\nabla \cdot \vec{F}) \, dV = \int_0^1 \int_0^1 \int_0^1 (2x + 2y + 2z) \, dz \, dy \, dx.
     \]$
     Integrate with respect to \( z \):
     $\[
     \int_0^1 (2x + 2y + 2z) \, dz = \left[ 2x z + 2y z + z^2 \right]_0^1 = 2x + 2y + 1.
     \]$
     Integrate with respect to \( y \):
     $\[
     \int_0^1 (2x + 2y + 1) \, dy = \left[ 2x y + y^2 + y \right]_0^1 = 2x + 1 + 1 = 2x + 2.
     \]$
     Integrate with respect to \( x \):
     $\[
     \int_0^1 (2x + 2) \, dx = \left[ x^2 + 2x \right]_0^1 = 1 + 2 = 3.
     \]$
   - By the Divergence Theorem:
     $\[
     \iint_S \vec{F} \cdot d\vec{S} = 3.
     \]$

3. **Use the Divergence Theorem to evaluate $\( \iint_S \vec{F} \cdot d\vec{S} \) for \( \vec{F}(x, y, z) = x \hat{i} + y \hat{j} + z \hat{k} \)$ over the surface of the cylinder $\( x^2 + y^2 = 4 \), \( 0 \leq z \leq 3 \)$**:
   - Compute the divergence of $\( \vec{F} \)$:
     $\[
     \nabla \cdot \vec{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3.
     \]$
   - Compute the volume integral:
     The volume of the cylinder is $\( \pi r^2 h = \pi (2)^2 (3) = 12\pi \)$. Thus:
     $\[
     \iiint_V (\nabla \cdot \vec{F}) \, dV = 3 \cdot 12\pi = 36\pi.
     \]$
   - By the Divergence Theorem:
     $\[
     \iint_S \vec{F} \cdot d\vec{S} = 36\pi.
     \]$

---

### **Key Takeaways**
- The Divergence Theorem relates the flux of a vector field through a closed surface to the divergence of the field within the volume enclosed by the surface.
- It simplifies calculations by converting surface integrals into volume integrals and vice versa.
- The Divergence Theorem is essential in physics, engineering, and mathematics for solving problems involving flux and divergence.
