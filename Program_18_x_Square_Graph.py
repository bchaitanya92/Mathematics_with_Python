# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of values for the x-axis
x = np.arange(-10, 10, 0.01)  # Creates an array of values from -10 to 10 with a step size of 0.01

# Calculate the corresponding y-values using the square function
y = x**2  # Raises each element of x to the power of 2

# Create a plot
plt.plot(x, y)  # Plots the x and y values as a line graph

# Add labels to the axes
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot
plt.title('x-square Curve.')

# Enable grid lines for better visualization
plt.grid(True)

# Display the plot
plt.show()
