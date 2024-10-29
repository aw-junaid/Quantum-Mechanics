In quantum mechanics, the concept of entropy extends to mixed states, which are statistical ensembles of quantum states. The entropy of a mixed state provides a measure of the quantum system's uncertainty or disorder. This concept is fundamental in quantum information theory and quantum statistical mechanics.

### Pure vs. Mixed States

- **Pure State**: A pure state is described by a single quantum state, represented by a wavefunction $\( |\psi\rangle \)$ or a corresponding density matrix $\( \rho = |\psi\rangle \langle\psi| \)$. The entropy of a pure state is zero because there is no uncertainty about the state of the system.

- **Mixed State**: A mixed state represents a probabilistic mixture of different quantum states. It is described by a density matrix $\( \rho \)$ that is not a projector onto a single state, meaning it cannot be written as $\( |\psi\rangle \langle\psi| \)$ for some state $\( |\psi\rangle \)$.

### Density Matrix

The density matrix $\( \rho \)$ for a mixed state is given by:

$\[
\rho = \sum_i p_i |\psi_i\rangle \langle\psi_i|
\]$

where:
- $\( |\psi_i\rangle \)$ are the quantum states.
- $\( p_i \)$ are the probabilities associated with each state, such that $\( \sum_i p_i = 1 \)$.

### Von Neumann Entropy

The entropy of a mixed quantum state is quantified by the **von Neumann entropy**, which is a generalization of Shannon entropy to quantum systems. The von Neumann entropy $\( S(\rho) \)$ of a density matrix $\( \rho \)$ is defined as:

$\[
S(\rho) = -\text{Tr}(\rho \log_2 \rho)
\]$

Here:
- $\( \text{Tr} \)$ denotes the trace of a matrix, which is the sum of its diagonal elements.
- $\( \log_2 \rho \)$ is the matrix logarithm of the density matrix $\( \rho \)$.

### Key Properties of Von Neumann Entropy

1. **Non-Negativity**: $\( S(\rho) \geq 0 \)$. The entropy is always non-negative.
   
2. **Zero Entropy for Pure States**: For a pure state, $\( \rho = |\psi\rangle \langle\psi| \)$, the entropy $\( S(\rho) = 0 \)$. This reflects the fact that there is no uncertainty in a pure state.

3. **Maximal Entropy**: For a maximally mixed state (where the system is equally likely to be in any of a set of orthogonal states), the entropy is maximal. For a system of dimension $\( d \)$, the maximum entropy is $\( \log_2 d \)$.

4. **Additivity**: For two independent systems with density matrices $\( \rho_1 \)$ and $\( \rho_2 \)$, the entropy of the combined system is the sum of their entropies:
   $\[
   S(\rho_1 \otimes \rho_2) = S(\rho_1) + S(\rho_2)
   \]$

### Example: Two-Level System (Qubit)

Consider a qubit system where the mixed state is given by:

$\[
\rho = p |\psi_1\rangle \langle\psi_1| + (1 - p) |\psi_2\rangle \langle\psi_2|
\]$

where $\( |\psi_1\rangle \)$ and $\( |\psi_2\rangle \)$ are orthogonal states (e.g., $\( |0\rangle \)$ and $\( |1\rangle \))$ and \( p \) is the probability of the system being in state $\( |\psi_1\rangle \)$.

The density matrix can be diagonalized, and the eigenvalues of $\( \rho \)$ are $\( p \)$ and $\( 1 - p \)$. The von Neumann entropy is then:

$\[
S(\rho) = -p \log_2(p) - (1 - p) \log_2(1 - p)
\]$

This is the same as the Shannon entropy of a classical two-state system, reflecting the probabilistic nature of the mixed state.

### Summary

The entropy of mixed states in quantum mechanics, measured by the von Neumann entropy, captures the degree of uncertainty or disorder in a quantum system. For pure states, the entropy is zero, indicating no uncertainty. For mixed states, the entropy quantifies the extent to which the system is in a probabilistic mixture of different quantum states. This concept is crucial in understanding quantum information, quantum thermodynamics, and the behavior of quantum systems in general.
