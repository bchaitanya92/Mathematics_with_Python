# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of angles for the polar plot (theta)
# Covers full circle with 1000 points for smooth curves
theta = np.linspace(0, 2 * np.pi, 1000)

# Calculate the radius values using the equation: r = 2 * abs(cos(2 * theta))
# This equation defines a rose curve with eight petals
r = 2 * abs(np.cos(2 * theta))

# Create the polar plot with a red line
plt.polar(theta, r, 'r-')  # Connects the corresponding theta and r points as a red line

# Display the plot for user interaction
plt.show()
