# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define a range of angles for the polar plot (theta)
# This covers a full circle with high resolution for a smooth curve
theta = np.arange(0, 2 * np.pi, 0.01)

# Calculate the radius values using the equation: r = 5 + 5 * cos(theta)
# This equation defines a cardioid curve with a heart-like shape
r = 5 + 5 * np.cos(theta)

# Create the polar plot with a red line
plt.polar(theta, r, 'r-')  # Connects the corresponding theta and r points as a red line

# Add a title and labels for clarity
plt.title('Cardioid Curve')
plt.xlabel('Theta (radians)')
plt.ylabel('Radius')

# Display the plot for user interaction
plt.show()

