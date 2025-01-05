import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
x = np.linspace(-3, 3, 500)  # x values
n = 2  # Example: n=2 for y = x^2
y = x**n  # y = x^n
dy_dx = n * x**(n-1)  # dy/dx = n*x^(n-1)

# Plot the function and its derivative
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$y = x^n$', color='blue', linewidth=2)
plt.plot(x, dy_dx, label=r'$\frac{dy}{dx} = n \cdot x^{n-1}$', color='orange', linestyle='--', linewidth=2)

# Highlight tangent at a specific point (e.g., x=1)
x_tangent = 1
y_tangent = x_tangent**n
slope = n * x_tangent**(n-1)
tangent_line = slope * (x - x_tangent) + y_tangent
plt.plot(x, tangent_line, label='Tangent at x=1', color='green', linestyle=':')

# Add labels, legend, and grid
plt.title('Function and Its Gradient', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend(fontsize=12)
plt.grid(alpha=0.4)
plt.tight_layout()

# Show the plot
plt.show()
