# Import libraries for plotting and numerical calculations
import matplotlib.pyplot as plt
import numpy as np

# Define a range of x values with high resolution for smooth curves
x = np.arange(-10, 10, 0.01)

# Calculate corresponding y values using sine function
y = np.sin(x)

# Calculate corresponding z values using cosine function
z = np.cos(x)

# Create a single plot with two curves:
# - First curve: x vs. y (sine)
# - Second curve: x vs. z (cosine)
plt.plot(x, y, label='Sine (y)')
plt.plot(x, z, label='Cosine (z)')

# Add labels for axes and a title for clarification
plt.xlabel('x-axis')
plt.ylabel('y-axis (Sine) / z-axis (Cosine)')
plt.title('Sine and Cosine Curves')

# Display grid lines for better data visualization
plt.grid(True)

# Display the combined plot with legend for differentiating curves
plt.legend()
plt.show()
