# Import necessary libraries for plotting and numerical calculations
import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values using numpy's arange function
# -10 to 10 with a step size of 0.01 for smooth curve representation
x = np.arange(-10, 10, 0.01)

# Calculate the corresponding y values using the sine function from numpy
y = np.sin(x)  # Element-wise application of sine function to each x value

# Create a plot of the sine curve using matplotlib.pyplot
plt.plot(x, y)  # Connects the corresponding x and y points as a line

# Add labels to the axes for clarity
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot for identification
plt.title('Sine Curve')

# Enable grid lines for better data visualization and analysis
plt.grid(True)

# Display the plot for user interaction
plt.show()
