from sympy import plot_implicit, symbols, Eq

# Define symbolic variables
x, y = symbols('x, y')

# Define the parameter for the equation
a = 3

# Create the implicit equation using Eq class and addition
# x^(2/3) + y^(2/3) = a^(2/3)

p1 = plot_implicit(
    Eq(x**(2/3) + y**(2/3), a**(2/3)),  # Equation to plot
    (x, -5, 5),  # Range for x-axis (-5 to 5)
    (y, -5, 5),  # Range for y-axis (-5 to 5)
    title='astroid:$x^{2/3}+y^{2/3}=a^{2/3}$',  # Title with the equation and name ("astroid")
)

# Display the plot
p1.show()
