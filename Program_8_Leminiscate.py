from sympy import plot_implicit, symbols, Eq

# Define symbolic variables
x, y = symbols('x, y')

# Define the parameter for the equation
a = 3

# Create the implicit equation using sympy's Eq class and multiplication
# (a^2)*y^2 = (x^2)*(a^2 - x^2)

p1 = plot_implicit(
    Eq((a**2)*(y**2), (x**2)*((a**2)-(x**2))),  # Equation to plot
    (x, -5, 5),  # Range for x-axis (-5 to 5)
    (y, -5, 5),  # Range for y-axis (-5 to 5)
    title='leminiscate:$x^2y^2=x^2(a^2-x^2)$'  # Title with the equation and name ("leminiscate")
)

# Display the plot
p1.show()
