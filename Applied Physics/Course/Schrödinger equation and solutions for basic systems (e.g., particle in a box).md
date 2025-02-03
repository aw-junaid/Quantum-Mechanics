# **Schrödinger Equation and Solutions for Basic Systems**

The **Schrödinger equation** is the fundamental equation in quantum mechanics that describes how the wavefunction of a quantum system evolves over time. The wavefunction contains all the information about the system’s physical properties, such as position, momentum, and energy. The Schrödinger equation provides a way to predict the future behavior of quantum systems based on their current state.

## **1. Schrödinger Equation Overview**

### **Time-Dependent Schrödinger Equation**
The **time-dependent Schrödinger equation** describes how the wavefunction $\( \psi(x, t) \)$ of a particle changes with time. It is given by:
$\[
i \hbar \frac{\partial \psi(x, t)}{\partial t} = \hat{H} \psi(x, t)
\]$
Where:
- $\( \hbar \)$ is the reduced Planck constant $(\( \hbar = \frac{h}{2\pi} \))$,
- \( i \) is the imaginary unit,
- $\( \psi(x, t) \)$ is the wavefunction of the system (depends on position \(x\) and time \(t\)),
- $\( \hat{H} \)$ is the **Hamiltonian operator**, which represents the total energy of the system (kinetic + potential energy).

### **Time-Independent Schrödinger Equation**
For systems where the potential does not depend on time, we can separate the spatial and time parts of the wavefunction. This leads to the **time-independent Schrödinger equation**, which is useful for stationary states (states with definite energy):
$\[
\hat{H} \psi(x) = E \psi(x)
\]$
Where:
- $\( \psi(x) \)$ is the wavefunction depending only on position,
- \( E \) is the energy of the system,
- The Hamiltonian operator $\( \hat{H} \)$ is often expressed as:
$\[
\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x)
\]$
Where:
- \( m \) is the mass of the particle,
- $\( V(x) \)$ is the potential energy as a function of position.

---

## **2. Solutions of the Schrödinger Equation for Basic Systems**

### **Particle in a Box (Infinite Potential Well)**

The **particle in a box** (or infinite potential well) is one of the simplest quantum mechanical systems. It consists of a particle confined in a one-dimensional box with infinitely high walls (i.e., the potential $\( V(x) \)$ is zero inside the box and infinite outside).

#### **Setting Up the Problem:**
- The potential $\( V(x) \)$ is defined as:
```math
  V(x) =
  \begin{cases}
  0, & 0 < x < L \\
  \infty, & \text{otherwise}
  \end{cases}
```
  Where \( L \) is the length of the box.
- Inside the box, the Schrödinger equation becomes:
  $\[
  -\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} = E \psi(x)
  \]$
  Outside the box, the wavefunction $\( \psi(x) \)$ must be zero because the potential is infinite (the particle cannot exist outside the box).

#### **Boundary Conditions:**
- The wavefunction must be zero at the boundaries of the box $(at \( x = 0 \) and \( x = L \))$:
  $\[
  \psi(0) = 0, \quad \psi(L) = 0
  \]$

#### **Solving the Schrödinger Equation:**
- The solution to the time-independent Schrödinger equation inside the box $(for \( 0 < x < L \))$ is a sine wave, as this satisfies the boundary conditions:
  $\[
  \psi_n(x) = \sqrt{\frac{2}{L}} \sin \left( \frac{n \pi x}{L} \right)
  \]$
  Where $\( n = 1, 2, 3, \dots \)$ is a positive integer (quantum number).
  
- The corresponding energy eigenvalues are:
  $\[
  E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}
  \]$
  Where:
  - \( n \) is the quantum number that determines the energy level,
  - $\( \hbar \)$ is the reduced Planck constant,
  - \( m \) is the mass of the particle,
  - \( L \) is the length of the box.

#### **Interpretation:**
- The particle can only occupy discrete energy levels, which are quantized. These energy levels depend on the quantum number \( n \), the mass of the particle, and the size of the box. The lower the quantum number \( n \), the lower the energy.
- The wavefunctions $\( \psi_n(x) \)$ represent the probability distributions of finding the particle at different positions within the box.

#### **Normalization:**
The wavefunctions are **normalized** so that the total probability of finding the particle within the box is equal to 1. This is achieved by ensuring that the integral of $\( |\psi(x)|^2 \)$ over the box is equal to 1:
$\[
\int_0^L |\psi_n(x)|^2 dx = 1
\]$

---

### **Particle in a One-Dimensional Finite Potential Well**

In a **finite potential well**, the potential \( V(x) \) is finite inside the well and infinite outside. The particle is still confined, but the walls are not infinitely high. This system allows for **bound states** where the energy levels are discrete but different from the infinite well.

The time-independent Schrödinger equation for a particle inside the finite well becomes more complicated, involving **exponential decay** for the wavefunction outside the well (where the particle has less probability of being found), and **trigonometric solutions** for the wavefunction inside the well.

The general solution involves solving for both the wavefunction inside and outside the well, ensuring continuity at the boundaries, and using normalization to determine the possible energy levels.

---

### **Harmonic Oscillator**

The **quantum harmonic oscillator** is another fundamental quantum system, where a particle is subject to a restoring force proportional to its displacement from the equilibrium position (similar to a mass on a spring).

The potential for a harmonic oscillator is given by:
$\[
V(x) = \frac{1}{2} m \omega^2 x^2
\]$
Where:
- \( m \) is the mass of the particle,
- $\( \omega \)$ is the angular frequency of oscillation.

The time-independent Schrödinger equation for this system is:
$\[
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} + \frac{1}{2} m \omega^2 x^2 \psi(x) = E \psi(x)
\]$

The solutions to this equation are more complex than for the particle in a box, involving **Hermite polynomials**. The energy eigenvalues are quantized and given by:
$\[
E_n = \left( n + \frac{1}{2} \right) \hbar \omega
\]$
Where $\( n = 0, 1, 2, 3, \dots \)$ is the quantum number.

---

## **3. Summary of Key Concepts**

- The **Schrödinger equation** is a key equation in quantum mechanics that governs the behavior of quantum systems. It can be time-dependent or time-independent, depending on the situation.
- The **particle in a box** is a simple system with quantized energy levels and wavefunctions that satisfy boundary conditions. This model illustrates the concept of quantization of energy.
- Other basic systems like the **finite potential well** and the **quantum harmonic oscillator** have solutions that show quantization but involve more complex wavefunctions and energy eigenvalues.
  
These systems serve as the foundation for understanding more complex quantum systems and are widely used in various areas of physics, from atomic to condensed matter physics.
