# Peano Arithmetic (PA)

Peano Arithmetic (PA) is a formal system foundational to understanding the natural numbers and their properties. Named after the Italian mathematician Giuseppe Peano, it consists of a set of axioms that define the basic properties of natural numbers, starting from $0$ and using the concept of "successorship" (moving from one number to the next).

## The Axioms of Peano Arithmetic

Peano Arithmetic is based on a small set of axioms, which can be divided into two categories: logical axioms and axioms specific to arithmetic. The system typically includes the following:

1. **Zero Axiom**:
   - $0$ is a natural number.

2. **Successor Axiom**:
   - Every natural number $n$ has a successor, denoted by $S(n)$, which is also a natural number.
   - $S(n)$ is thought of as the "next" number after $n$. For example, the successor of $0$ is $1$, the successor of $1$ is $2$, and so on.

3. **No Natural Number Has $0$ as Its Successor**:
   - $\forall n \, (S(n) \neq 0)$.
   - This ensures that $0$ is the first natural number, and no other number can "come before" it.

4. **Injectivity of the Successor Function**:
   - $\forall m \, \forall n \, (S(m) = S(n) \rightarrow m = n)$.
   - This states that if two numbers have the same successor, then they must be the same number. The successor function is injective (one-to-one).

5. **Induction Axiom**:
   - If a property holds for $0$ and holds for the successor of a number whenever it holds for that number, then it holds for all natural numbers.
   - Formally: $\forall P \, [P(0) \land \forall n \, (P(n) \rightarrow P(S(n))) \rightarrow \forall n \, P(n)]$.
   - This is the principle of mathematical induction, which is crucial for proving statements about all natural numbers.

## Arithmetic Operations in Peano Arithmetic

Using these axioms, one can define the basic arithmetic operations such as addition and multiplication:

- **Addition**:
  - $n + 0 = n$
  - $n + S(m) = S(n + m)$

- **Multiplication**:
  - $n \times 0 = 0$
  - $n \times S(m) = (n \times m) + n$

## Expressiveness and Limitations

Peano Arithmetic is powerful enough to express basic properties of natural numbers and prove many theorems about them. However, Gödel's incompleteness theorems demonstrate that PA, while consistent, cannot be both complete and able to prove its own consistency.

## Interpretations and Models

Peano Arithmetic can be interpreted in different models, but the standard model is the set of natural numbers $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ with the usual successor function, addition, and multiplication. However, non-standard models of PA also exist, which include "infinite" natural numbers beyond those in the standard model.

## Importance of Peano Arithmetic

Peano Arithmetic is foundational to number theory and has significant implications for the philosophy of mathematics. It forms the basis for understanding how natural numbers work and is often the starting point for more complex mathematical theories.

## Summary

Peano Arithmetic is a formal system that provides the basic axioms for natural numbers, defining concepts such as zero, succession, addition, and multiplication. It is a cornerstone of mathematics, used to understand the properties of natural numbers, and plays a key role in discussions of mathematical logic and the foundations of mathematics.
