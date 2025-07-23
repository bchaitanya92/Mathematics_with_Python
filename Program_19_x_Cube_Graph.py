# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of values for the x-axis with a larger step size (2)
x = np.arange(-10, 10, 2)  # Creates an array of values from -10 to 10 with a step size of 2

# Calculate the corresponding y-values using the cubic function
y = x**3  # Raises each element of x to the power of 3

# Create a plot of the x^3 curve
plt.plot(x, y)  # Plots the x and y values as a line graph

# Add labels to the axes for clarity
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot for identification
plt.title('x-cube Curve.')

# Enable grid lines for better data visualization and analysis
plt.grid(True)

# Display the plot for user interaction
plt.show()
