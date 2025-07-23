# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of x-values with a step size of 2 for a clearer representation
x = np.arange(-10, 10, 2)  # Creates an array of values from -10 to 10 with a step size of 2

# Generate y-values equal to the corresponding x-values, representing a linear relationship
y = x  # y = x defines a straight line with a slope of 1

# Create a line plot of the y values vs. x values
plt.plot(x, y)  # Connects the corresponding x and y points as a line

# Add labels to the axes for clarity
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot for identification
plt.title('Linear Curve (y = x)')

# Enable grid lines for better data visualization and analysis
plt.grid(True)

# Display the plot for user interaction
plt.show()
