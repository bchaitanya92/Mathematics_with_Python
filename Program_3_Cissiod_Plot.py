from sympy import plot_implicit, symbols, Eq

# Define symbolic variables
x, y = symbols('x, y')

# Define the parameter for the equation
a = 3

# Create the implicit equation using sympy's Eq class and multiplication
# (y^2)*(a-x) = x^3

p1 = plot_implicit(
    Eq((y**2)*(a-x), x**3),  # Equation to plot
    (x, -5, 5),  # Range for x-axis (-5 to 5)
    (y, -5, 5),  # Range for y-axis (-5 to 5)
    title='cissiod:$y^2(a-x)=x^3$',  # Title with the equation and name ("cissiod")
)

# Display the plot
p1.show()
