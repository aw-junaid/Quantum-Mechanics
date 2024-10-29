Let's consider a simple example of a two-state system, which is a common model in various fields like physics, information theory, and thermodynamics. In this system, the random variable ( X ) can take on one of two possible states: $( x_1 )$ and $( x_2 )$. Each state has a certain probability associated with it.

### Example Setup

Suppose we have a system with the following probabilities:

- The probability of state $\( x_1 \)$ is \( p \).
- The probability of state $\( x_2 \)$ is $\( 1 - p \)$.

These two states could represent anything from the spin of a quantum particle (up or down), the outcome of a coin toss (heads or tails), or the binary state of a bit (0 or 1).

### Shannon Entropy for the Two-State System

The Shannon entropy $\( H(X) \)$ of this two-state system is calculated using the formula:

$\[
H(X) = - \left( p \log_2(p) + (1 - p) \log_2(1 - p) \right)
\]$

### Specific Cases

1. **Case 1: \( p = 0.5 \) (Maximum Entropy)**
   
   This is the case of maximum uncertainty, where both states are equally likely (e.g., a fair coin toss).

   $\[
   H(X) = - \left( 0.5 \log_2(0.5) + 0.5 \log_2(0.5) \right)
   \]$
   $\[
   H(X) = - \left( 0.5 \times -1 + 0.5 \times -1 \right) = 1 \text{ bit}
   \]$

   Here, the entropy is 1 bit, which means that on average, 1 bit is required to encode the outcome of this system. This makes sense since with equal probabilities, there is maximum uncertainty about the outcome.

2. **Case 2: \( p = 0.9 \) (Low Entropy)**
   
   In this case, one state is much more likely than the other (e.g., a biased coin that lands heads 90% of the time).

   $\[
   H(X) = - \left( 0.9 \log_2(0.9) + 0.1 \log_2(0.1) \right)
   \]$
   $\[
   H(X) = - \left( 0.9 \times -0.152 + 0.1 \times -3.322 \right)
   \]$
   $\[
   H(X) \approx - \left( -0.137 + -0.332 \right) = 0.469 \text{ bits}
   \]$

   Here, the entropy is lower (about 0.469 bits) because there is less uncertainty; the outcome is more predictable.

3. **Case 3: \( p = 1 \) (Zero Entropy)**
   
   In this case, the system is fully deterministic (e.g., a coin that always lands heads).

   $\[
   H(X) = - \left( 1 \log_2(1) + 0 \log_2(0) \right)
   \]$
   
   Since $\( \log_2(1) = 0 \)$ and the term $\( 0 \log_2(0) \)$ is considered to be 0 by convention (as it represents a probability of 0, meaning that outcome never occurs), the entropy is:

   $\[
   H(X) = 0 \text{ bits}
   \]$

   Here, the entropy is zero because there is no uncertainty; the outcome is certain.

### Summary

In a two-state system, Shannon entropy quantifies the uncertainty in predicting the outcome. When the two states are equally likely $(\( p = 0.5 \))$, the entropy is at its maximum, reflecting maximum unpredictability (1 bit). As the probabilities become skewed (\( p \) moves towards 0 or 1), the entropy decreases, indicating lower uncertainty. When one state is certain $(\( p = 1 \))$, the entropy is zero, as there is no uncertainty about the outcome.
