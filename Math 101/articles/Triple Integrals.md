**Triple integrals** are an extension of double integrals to functions of three variables. They are used to compute volumes, masses, and other quantities in three-dimensional space. Triple integrals are essential in physics, engineering, and mathematics for solving problems involving 3D regions. Here's a detailed explanation:

---

### **Definition of Triple Integrals**

A triple integral of a function $\( f(x, y, z) \)$ over a 3D region \( E \) is written as:
$\[
\iiint_E f(x, y, z) \, dV,
\]$
where $\( dV \)$ represents an infinitesimal volume element. In Cartesian coordinates, $\( dV = dx \, dy \, dz \)$.

---

### **Steps for Evaluating Triple Integrals**

1. **Set Up the Integral**:
   - Determine the limits of integration for \( x \), \( y \), and \( z \) based on the region \( E \).

2. **Choose the Order of Integration**:
   - The order of integration depends on the geometry of the region. Common orders are $\( dz \, dy \, dx \), \( dy \, dx \, dz \)$, etc.

3. **Evaluate the Innermost Integral**:
   - Integrate with respect to the innermost variable, treating the other variables as constants.

4. **Evaluate the Middle Integral**:
   - Integrate the result of the innermost integral with respect to the next variable.

5. **Evaluate the Outer Integral**:
   - Integrate the result of the middle integral with respect to the outermost variable.

---

### **Applications of Triple Integrals**

1. **Volume of a 3D Region**:
   - The volume of a region \( E \) is given by:
     $\[
     V = \iiint_E 1 \, dV.
     \]$

2. **Mass of a Solid**:
   - If $\( f(x, y, z) \)$ represents the density of a solid, the mass is:
     $\[
     m = \iiint_E f(x, y, z) \, dV.
     \]$

3. **Center of Mass**:
   - The coordinates of the center of mass are:
     $\[
     \bar{x} = \frac{1}{m} \iiint_E x f(x, y, z) \, dV,
     \]$
     
     $\[
     \bar{y} = \frac{1}{m} \iiint_E y f(x, y, z) \, dV,
     \]$
     
     $\[
     \bar{z} = \frac{1}{m} \iiint_E z f(x, y, z) \, dV.
     \]$

4. **Moment of Inertia**:
   - The moment of inertia about an axis is:
     $\[
     I = \iiint_E r^2 f(x, y, z) \, dV,
     \]$
     where \( r \) is the distance from the axis.

---

### **Example Problems**

1. **Compute the volume of the region bounded by $\( z = 0 \), \( z = 1 - x^2 - y^2 \), and the \( xy \)-plane$**:
   - The region is a paraboloid bounded below by \( z = 0 \) and above by $\( z = 1 - x^2 - y^2 \)$.
   - In cylindrical coordinates, the limits are:
     $\[
     0 \leq z \leq 1 - r^2, \quad 0 \leq r \leq 1, \quad 0 \leq \theta \leq 2\pi.
     \]$
   - Set up the integral:
     $\[
     V = \int_0^{2\pi} \int_0^1 \int_0^{1 - r^2} r \, dz \, dr \, d\theta.
     \]$
   - Evaluate the innermost integral:
     $\[
     \int_0^{1 - r^2} r \, dz = r(1 - r^2).
     \]$
   - Evaluate the middle integral:
     $\[
     \int_0^1 r(1 - r^2) \, dr = \int_0^1 (r - r^3) \, dr = \left[ \frac{r^2}{2} - \frac{r^4}{4} \right]_0^1 = \frac{1}{4}.
     \]$
   - Evaluate the outer integral:
     $\[
     \int_0^{2\pi} \frac{1}{4} \, d\theta = \frac{\pi}{2}.
     \]$
   - The volume is $\( \frac{\pi}{2} \)$.

2. **Compute the mass of a solid with density $\( f(x, y, z) = x + y + z \)$ bounded by $\( 0 \leq x \leq 1 \)$, $\( 0 \leq y \leq 1 \)$, and $\( 0 \leq z \leq 1 \)$**:
   - Set up the integral:
     $\[
     m = \int_0^1 \int_0^1 \int_0^1 (x + y + z) \, dz \, dy \, dx.
     \]$
   - Evaluate the innermost integral:
     $\[
     \int_0^1 (x + y + z) \, dz = \left[ xz + yz + \frac{z^2}{2} \right]_0^1 = x + y + \frac{1}{2}.
     \]$
   - Evaluate the middle integral:
     $\[
     \int_0^1 \left( x + y + \frac{1}{2} \right) \, dy = \left[ xy + \frac{y^2}{2} + \frac{y}{2} \right]_0^1 = x + \frac{1}{2} + \frac{1}{2} = x + 1.
     \]$
   - Evaluate the outer integral:
     $\[
     \int_0^1 (x + 1) \, dx = \left[ \frac{x^2}{2} + x \right]_0^1 = \frac{1}{2} + 1 = \frac{3}{2}.
     \]$
   - The mass is $\( \frac{3}{2} \)$.

3. **Find the center of mass of a solid with constant density $\( \rho \)$ bounded by $\( z = 0 \)$, $\( z = 1 - x^2 - y^2 \)$, and the \( xy \)-plane**:
   - The mass is $\( m = \rho V \)$, where \( V \) is the volume computed earlier $(\( V = \frac{\pi}{2} \))$.
   - Compute $\( \bar{x} \)$:
     $\[
     \bar{x} = \frac{1}{m} \iiint_E x \rho \, dV = \frac{1}{\rho V} \cdot \rho \iiint_E x \, dV = \frac{1}{V} \iiint_E x \, dV.
     \]$
     Due to symmetry, $\( \bar{x} = 0 \)$.
   - Similarly, $\( \bar{y} = 0 \)$.
   - Compute $\( \bar{z} \)$:
     $\[
     \bar{z} = \frac{1}{V} \iiint_E z \, dV.
     \]$
     Using cylindrical coordinates:
     $\[
     \iiint_E z \, dV = \int_0^{2\pi} \int_0^1 \int_0^{1 - r^2} z r \, dz \, dr \, d\theta.
     \]$
     Evaluate the innermost integral:
     $\[
     \int_0^{1 - r^2} z r \, dz = r \left[ \frac{z^2}{2} \right]_0^{1 - r^2} = \frac{r}{2} (1 - r^2)^2.
     \]$
     Evaluate the middle integral:
     $\[
     \int_0^1 \frac{r}{2} (1 - r^2)^2 \, dr = \frac{1}{2} \int_0^1 r (1 - 2r^2 + r^4) \, dr = \frac{1}{2} \left[ \frac{r^2}{2} - \frac{r^4}{2} + \frac{r^6}{6} \right]_0^1 = \frac{1}{12}.
     \]$
     Evaluate the outer integral:
     $\[
     \int_0^{2\pi} \frac{1}{12} \, d\theta = \frac{\pi}{6}.
     \]$
     Thus:
     $\[
     \bar{z} = \frac{1}{\frac{\pi}{2}} \cdot \frac{\pi}{6} = \frac{1}{3}.
     \]$
   - The center of mass is at $\( (0, 0, \frac{1}{3}) \)$.

---

### **Key Takeaways**
- Triple integrals are used to compute volumes, masses, and other quantities in 3D regions.
- The order of integration depends on the geometry of the region.
- Applications include finding volumes, masses, centers of mass, and moments of inertia.
- Understanding triple integrals is essential for solving problems in 3D space.
