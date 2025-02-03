# **Rotational Motion and Dynamics**  

## **1. Rotational Motion**  
**Rotational motion** occurs when an object spins about an axis. Unlike linear motion, where objects move along a straight path, rotational motion involves angular displacement, velocity, and acceleration.

### **Key Rotational Quantities**
| Linear Motion | Rotational Motion |
|--------------|-----------------|
| Displacement (\(x\)) | Angular displacement $(\(\theta\))$ |
| Velocity (\(v\)) | Angular velocity $(\(\omega\))$ |
| Acceleration (\(a\)) | Angular acceleration $(\(\alpha\))$ |
| Force (\(F\)) | Torque $(\(\tau\))$ |
| Mass (\(m\)) | Moment of Inertia (\(I\)) |
| Momentum $(\(p = mv\))$ | Angular Momentum $(\(L = I\omega\))$ |

### **Angular Quantities**
1. **Angular Displacement $(\(\theta\))$**: Angle rotated by an object.
2. **Angular Velocity $(\(\omega\))$**: Rate of change of angular displacement.
   $\[
   \omega = \frac{d\theta}{dt}
   \]$
3. **Angular Acceleration $(\(\alpha\))$**: Rate of change of angular velocity.
   $\[
   \alpha = \frac{d\omega}{dt}
   \]$

### **Equations of Rotational Motion (Analogous to Linear Motion)**
1. $\(\omega_f = \omega_i + \alpha t\)$
2. $\(\theta = \omega_i t + \frac{1}{2} \alpha t^2\)$
3. $\(\omega_f^2 = \omega_i^2 + 2\alpha\theta\)$

---

## **2. Moment of Inertia (\(I\))**  
Moment of inertia (\(I\)) is the rotational equivalent of mass. It depends on the mass distribution relative to the axis of rotation.

$\[
I = \sum m r^2
\]$

### **Moment of Inertia for Common Objects:**
| Object | Moment of Inertia (\(I\)) |
|--------|-------------------------|
| Thin rod (about center) | $\( \frac{1}{12} ML^2 \)$ |
| Thin rod (about end) | $\( \frac{1}{3} ML^2 \)$ |
| Solid disk | $\( \frac{1}{2} MR^2 \)$ |
| Hollow cylinder | $\( MR^2 \)$ |
| Solid sphere | $\( \frac{2}{5} MR^2 \)$ |

---

## **3. Torque (\(\tau\))**  
Torque is the rotational equivalent of force, causing an object to rotate.

$\[
\tau = r F \sin \theta
\]$

where:
- $\( r \)$ = distance from axis of rotation,
- $\( F \)$ = applied force,
- $\( \theta \) = angle between \( F \) and \( r \)$.

### **Newton's Second Law for Rotation**
$\[
\tau = I \alpha
\]$
This is the rotational analog of $\( F = ma \)$.

---

## **4. Angular Momentum $(\(L\))$ and Its Conservation**  
Angular momentum is the rotational counterpart of linear momentum.

$\[
L = I \omega
\]$

### **Law of Conservation of Angular Momentum**  
If no external torque acts on a system, its angular momentum remains constant.

$\[
I_i \omega_i = I_f \omega_f
\]$

### **Example:**
- **Ice Skater Spin**: When an ice skater pulls in their arms, their moment of inertia decreases, so angular velocity increases to conserve angular momentum.

---

## **5. Rotational Kinetic Energy**
The energy associated with rotational motion is:

$\[
KE_{\text{rot}} = \frac{1}{2} I \omega^2
\]$

Total mechanical energy in a rolling object:
$\[
E_{\text{total}} = KE_{\text{translational}} + KE_{\text{rotational}}
\]$

$\[
E_{\text{total}} = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2
\]$

---

## **6. Rolling Motion**
When an object rolls without slipping, there is a relationship between linear and angular motion:

$\[
v = r \omega
\]$

This applies to rolling objects like wheels, balls, and cylinders.

---

## **Conclusion**
- **Rotational motion** deals with angular displacement, velocity, and acceleration.
- **Moment of inertia** determines how mass is distributed around the rotation axis.
- **Torque** is the force that causes rotational motion.
- **Angular momentum** is conserved if no external torque acts.
- **Rotational kinetic energy** contributes to the total energy of rolling objects.

Understanding these principles is crucial in mechanics, engineering, robotics, and astrophysics! 🚀
