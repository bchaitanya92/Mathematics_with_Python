# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the parameter for the curves (a)
a = 3

# Create a range of angles for the polar plot (theta)
theta = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Covers full circle with 1000 points

# Calculate the radius values for the first curve (r1)
# Uses the equation r = a + a * cos(theta)
r1 = a + a * np.cos(theta)

# Calculate the radius values for the second curve (r2)
# Uses the equation r = a - a * cos(theta) (opposite sign)
r2 = a - a * np.cos(theta)

# Create the polar plot
plt.polar(theta, r1, 'r-', label="r1 = a + a * cos(theta)")  # Red line with label
plt.polar(theta, r2, 'g-', label="r2 = a - a * cos(theta)")  # Green line with label

# Add a legend for identifying the curves
plt.legend()

# Display the plot
plt.show()

