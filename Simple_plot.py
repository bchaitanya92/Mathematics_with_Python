# Import necessary libraries for plotting and numerical calculations
import matplotlib.pyplot as plt
import numpy as np

# Define a range of x values using `np.linspace` with high resolution
x = np.linspace(0, 2, 100)  # Creates 100 points between 0 and 2 (inclusive)

# Calculate corresponding y values for different functions:
# - Linear: y = x
y1 = x

# - Quadratic: y = x^2
y2 = x**2

# - Cubic: y = x^3
y3 = x**3

# Create a single plot with three curves
plt.plot(x, y1, label='linear')  # Line 1 with label 'linear'
plt.plot(x, y2, label='quadratic')  # Line 2 with label 'quadratic'
plt.plot(x, y3, label='cubic')  # Line 3 with label 'cubic'

# Add labels for axes and a descriptive title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Comparison of Linear, Quadratic, and Cubic Functions')

# Enable grid lines for better visualization
plt.grid(True)

# Display a legend for differentiating the curves
plt.legend()

# Show the plot for user interaction
plt.show()
