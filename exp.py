import numpy as np
import matplotlib.pyplot as plt

# Matrix A from the quadratic form
A = np.array([[1, 0.5],
              [0.5, 1]])

# Eigen-decomposition
eigvals, eigvecs = np.linalg.eigh(A)

# Semi-axis lengths
axes_lengths = 1 / np.sqrt(eigvals)

# Parametric circle
theta = np.linspace(0, 2 * np.pi, 300)
circle = np.array([np.cos(theta), np.sin(theta)])

# Transform circle to ellipse using eigenvectors and axis lengths
ellipse = eigvecs @ np.diag(axes_lengths) @ circle

# Plot
plt.figure(figsize=(6, 6))
plt.plot(ellipse[0, :], ellipse[1, :], label=r"$x^2 + xy + y^2 = 1$")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.title("Tilted Ellipse")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()