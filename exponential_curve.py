# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of x-values with high resolution for a smooth curve
x = np.arange(-10, 10, 0.01)  # -10 to 10 with a step size of 0.01

# Calculate the corresponding y-values using the exponential function
y = np.exp(x)  # Element-wise application of the exponential function to each x value

# Create a plot of the exponential curve
plt.plot(x, y)  # Connects the corresponding x and y points as a line

# Add labels to the axes for clarity
plt.xlabel('x-axis')
plt.ylabel('y-axis (e^x)')  # Specify the exponential y-axis label

# Add a title to the plot for identification
plt.title('Exponential Curve (e^x)')

# Enable grid lines for better data visualization and analysis
plt.grid(True)

# Display the plot for user interaction
plt.show()

