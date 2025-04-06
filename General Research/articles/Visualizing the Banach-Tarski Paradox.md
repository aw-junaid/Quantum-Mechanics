# Visualizing the Banach-Tarski Paradox in Jupyter Notebook

While we can't perfectly recreate the true Banach-Tarski paradox (which relies on non-measurable sets and the Axiom of Choice), we can create a simplified visualization that demonstrates the core concept of decomposing and reassembling shapes. Here's a Jupyter notebook implementation using matplotlib:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
import matplotlib.animation as animation
from IPython.display import HTML

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(-3, 3)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')
plt.title('Simplified Banach-Tarski Paradox Visualization', pad=20)

# Create original circle
original_circle = Circle((0, 0), 1, fc='blue', alpha=0.5)
ax.add_patch(original_circle)
ax.text(0, 0, 'Original\nBall', ha='center', va='center', color='white')

# Create pieces (simplified into wedges)
pieces = []
colors = ['red', 'green', 'yellow', 'purple', 'orange']
angles = [0, 72, 144, 216, 288]  # 5 pieces at 72° each

for i, angle in enumerate(angles):
    wedge = Wedge((0, 0), 1, angle, angle+72, fc=colors[i], alpha=0.7)
    pieces.append(wedge)
    ax.add_patch(wedge)

# Animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    
    if frame < 30:  # Initial state - whole ball
        circle = Circle((0, 0), 1, fc='blue', alpha=0.5)
        ax.add_patch(circle)
        ax.text(0, 0, 'Original\nBall', ha='center', va='center', color='white')
    elif frame < 60:  # Decomposing into pieces
        for i, wedge in enumerate(pieces):
            # Move pieces outward slightly
            center_x = np.cos(np.radians(angles[i]+36)) * 0.1 * (frame-30)/30
            center_y = np.sin(np.radians(angles[i]+36)) * 0.1 * (frame-30)/30
            wedge = Wedge((center_x, center_y), 1, angles[i], angles[i]+72, 
                          fc=colors[i], alpha=0.7)
            ax.add_patch(wedge)
    elif frame < 90:  # Moving pieces apart
        for i, wedge in enumerate(pieces):
            center_x = np.cos(np.radians(angles[i]+36)) * (1 + (frame-60)/30)
            center_y = np.sin(np.radians(angles[i]+36)) * (1 + (frame-60)/30)
            wedge = Wedge((center_x, center_y), 1, angles[i], angles[i]+72, 
                          fc=colors[i], alpha=0.7)
            ax.add_patch(wedge)
    else:  # Reassembling into two balls
        # First new ball (using pieces 0,1,4)
        for i in [0,1,4]:
            progress = (frame-90)/30
            target_x = -1.5 + np.cos(np.radians(angles[i]+36)) * progress
            target_y = 0 + np.sin(np.radians(angles[i]+36)) * progress
            wedge = Wedge((target_x, target_y), 1, angles[i], angles[i]+72, 
                          fc=colors[i], alpha=0.7)
            ax.add_patch(wedge)
        
        # Second new ball (using pieces 2,3)
        for i in [2,3]:
            progress = (frame-90)/30
            target_x = 1.5 + np.cos(np.radians(angles[i]+36)) * progress
            target_y = 0 + np.sin(np.radians(angles[i]+36)) * progress
            wedge = Wedge((target_x, target_y), 1, angles[i], angles[i]+72, 
                          fc=colors[i], alpha=0.7)
            ax.add_patch(wedge)
        
        # Draw the new balls
        if frame >= 110:
            circle1 = Circle((-1.5, 0), 1, fc='blue', alpha=0.3)
            circle2 = Circle((1.5, 0), 1, fc='blue', alpha=0.3)
            ax.add_patch(circle1)
            ax.add_patch(circle2)
            ax.text(-1.5, 0, 'New Ball 1', ha='center', va='center')
            ax.text(1.5, 0, 'New Ball 2', ha='center', va='center')

# Create and display animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50)
plt.close()
HTML(ani.to_jshtml())
```

## Explanation of the Visualization:

1. **Initial State**: Shows a single blue circle representing the original ball.

2. **Decomposition**: The ball splits into 5 colored pieces (simplified representation).

3. **Separation**: The pieces move outward from the center.

4. **Reassembly**: The pieces reorganize into two new balls (using 3 pieces for one ball and 2 for the other).

## Important Notes:

- This is a **conceptual visualization only** - the real Banach-Tarski paradox:
  - Uses non-measurable sets (which can't be drawn)
  - Requires the Axiom of Choice (infinite, non-constructive selection)
  - Works in 3D space with proper rotations

- The animation shows:
  - How decomposition and reassembly can conceptually create two balls
  - That the "pieces" maintain their size but are rearranged

For a more mathematically rigorous treatment, you would need to:
1. Work with free group rotations
2. Deal with non-measurable sets
3. Use abstract mathematical constructions rather than visual shapes
