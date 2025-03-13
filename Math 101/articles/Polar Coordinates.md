Polar coordinates are a two-dimensional coordinate system that represents points in a plane using a distance from a reference point (called the **pole**, typically the origin) and an angle from a reference direction (usually the positive \( x \)-axis). Polar coordinates are particularly useful for describing curves and shapes that are symmetric about a point, such as circles, spirals, and roses. Here's a detailed explanation:

---

### **Definition of Polar Coordinates**

A point in polar coordinates is represented as $\( (r, \theta) \)$, where:
- \( r \): The radial distance from the pole (origin) to the point.
- $\( \theta \)$: The angle (in radians or degrees) measured from the positive \( x \)-axis (polar axis) to the line connecting the pole and the point.

---

### **Relationship Between Polar and Cartesian Coordinates**

Polar coordinates $\( (r, \theta) \)$ can be converted to Cartesian coordinates \( (x, y) \) using the following formulas:
$\[
x = r \cos(\theta), \quad y = r \sin(\theta).
\]$
Conversely, Cartesian coordinates \( (x, y) \) can be converted to polar coordinates $\( (r, \theta) \)$ using:
$\[
r = \sqrt{x^2 + y^2}, \quad \theta = \arctan\left(\frac{y}{x}\right).
\]$
- The angle $\( \theta \)$ is determined up to multiples of $\( 2\pi \)$, and the quadrant of $\( (x, y) \)$ must be considered.

---

### **Key Concepts**

1. **Polar Curves**:
   - Equations in polar coordinates often describe curves. For example:
     - \( r = a \): A circle of radius \( a \) centered at the origin.
     - $\( r = a\theta \)$: A spiral.
     - $\( r = a\cos(\theta) \)$ or $\( r = a\sin(\theta) \)$: Circles shifted from the origin.

2. **Symmetry**:
   - Polar curves can exhibit symmetry about the polar axis $(\( \theta = 0 \))$, the line $\( \theta = \frac{\pi}{2} \)$, or the origin.

3. **Negative \( r \)**:
   - If $\( r < 0 \)$, the point $\( (r, \theta) \)$ is located in the opposite direction of $\( \theta \)$.

4. **Multiple Representations**:
   - A point in polar coordinates can have multiple representations. For example:
     $\[
     (r, \theta) = (r, \theta + 2\pi n) \quad \text{or} \quad (-r, \theta + \pi + 2\pi n),
     \]$
     where \( n \) is an integer.

---

### **Common Polar Curves**

1. **Circle**:
   - \( r = a \): A circle of radius \( a \) centered at the origin.
   - $\( r = 2a\cos(\theta) \)$: A circle of radius \( a \) centered at \( (a, 0) \).
   - $\( r = 2a\sin(\theta) \)$: A circle of radius \( a \) centered at \( (0, a) \).

2. **Cardioid**:
   - $\( r = a(1 + \cos(\theta)) \)$: A heart-shaped curve.

3. **Limaçon**:
   - $\( r = a + b\cos(\theta) \)$ or $\( r = a + b\sin(\theta) \)$: A looped or dimpled curve.

4. **Rose Curves**:
   - $\( r = a\cos(n\theta) \)$ or $\( r = a\sin(n\theta) \)$: A flower-like curve with \( n \) petals if \( n \) is odd, or $\( 2n \)$ petals if \( n \) is even.

5. **Spiral**:
   - $\( r = a\theta \)$: A curve that spirals outward as $\( \theta \)$ increases.

---

### **Calculus in Polar Coordinates**

1. **Slope of a Tangent Line**:
   - The slope of the tangent line to a polar curve $\( r = f(\theta) \)$ is given by:
     $\[
     \frac{dy}{dx} = \frac{\frac{dr}{d\theta} \sin(\theta) + r \cos(\theta)}{\frac{dr}{d\theta} \cos(\theta) - r \sin(\theta)}.
     \]$

2. **Area in Polar Coordinates**:
   - The area enclosed by a polar curve \( r = f(\theta) \) between angles \( \theta = \alpha \) and \( \theta = \beta \) is:
     $\[
     A = \frac{1}{2} \int_\alpha^\beta [f(\theta)]^2 \, d\theta.
     \]$

3. **Arc Length**:
   - The arc length of a polar curve $\( r = f(\theta) \)$ between angles $\( \theta = \alpha \)$ and $\( \theta = \beta \)$ is:
     $\[
     L = \int_\alpha^\beta \sqrt{[f(\theta)]^2 + \left[\frac{df}{d\theta}\right]^2} \, d\theta.
     \]$

---

### **Example Problems**

1. **Convert $\( (x, y) = (3, 4) \)$ to polar coordinates**:
   - Compute \( r \):
     $\[
     r = \sqrt{3^2 + 4^2} = 5.
     \]$
   - Compute $\( \theta \)$:
     $\[
     \theta = \arctan\left(\frac{4}{3}\right).
     \]$
   - Polar coordinates: $\( (5, \arctan\left(\frac{4}{3}\right)) \)$.

2. **Convert $\( (r, \theta) = (2, \frac{\pi}{3}) \)$ to Cartesian coordinates**:
   - Compute \( x \) and \( y \):
     $\[
     x = 2 \cos\left(\frac{\pi}{3}\right) = 1, \quad y = 2 \sin\left(\frac{\pi}{3}\right) = \sqrt{3}.
     \]$
   - Cartesian coordinates: \( (1, \sqrt{3}) \).

3. **Find the area enclosed by $\( r = 2\cos(\theta) \)$**:
   - The curve is a circle of radius 1 centered at \( (1, 0) \).
   - The area is:
     $\[
     A = \frac{1}{2} \int_0^{2\pi} (2\cos(\theta))^2 \, d\theta = \frac{1}{2} \int_0^{2\pi} 4\cos^2(\theta) \, d\theta.
     \]$
     Use the identity $\( \cos^2(\theta) = \frac{1 + \cos(2\theta)}{2} \)$:
     $\[
     A = 2 \int_0^{2\pi} \frac{1 + \cos(2\theta)}{2} \, d\theta = \int_0^{2\pi} (1 + \cos(2\theta)) \, d\theta = 2\pi.
     \]$

4. **Find the slope of the tangent line to $\( r = 1 + \cos(\theta) \)$ at $\( \theta = \frac{\pi}{2} \)$**:
   - Compute $\( \frac{dr}{d\theta} = -\sin(\theta) \)$.
   - At $\( \theta = \frac{\pi}{2} \)$:
     $\[
     r = 1 + \cos\left(\frac{\pi}{2}\right) = 1, \quad \frac{dr}{d\theta} = -\sin\left(\frac{\pi}{2}\right) = -1.
     \]$
   - The slope is:
     $\[
     \frac{dy}{dx} = \frac{(-1)\sin\left(\frac{\pi}{2}\right) + 1 \cos\left(\frac{\pi}{2}\right)}{(-1)\cos\left(\frac{\pi}{2}\right) - 1 \sin\left(\frac{\pi}{2}\right)} = \frac{-1 + 0}{0 - 1} = 1.
     \]$

---

### **Key Takeaways**
- Polar coordinates represent points using a distance \( r \) and an angle $\( \theta \)$.
- They are useful for describing curves with symmetry about a point.
- Calculus techniques (e.g., area, arc length) can be applied to polar curves.
- Understanding polar coordinates is essential for advanced studies in mathematics, physics, and engineering.
