# Limit Definition of the Derivative Exploration
# We have discussed how to represent a function as an array and usenp.gradient() to perform numerical differentiation in Python.
# We found that it uses a process that is fairly similar to the limit definition of a derivative.
# To explore this idea more and get you familiar with the process of taking numerical derivatives, we’ll implement our own differentiation function from scratch and explore how it aligns with the limit definition of the derivative.


import numpy as np
from math import sin, log, pi
import matplotlib.pyplot as plt

# function to compute the derivative using the limit definition
def limit_derivative(f, x, h):
  """
  f: function to be differentiated 
  x: the point at which to differentiate f 
  h: distance between the points to be evaluated
  """
  # compute the derivative at x with limit definition
  return (f(x + h) - f(x)) / h

# f1(x) = sin(x)
def f1(x):
    return sin(x)


# f2(x) = x^4
def f2(x):
    return pow(x, 4)


# f3(x) = x^2*log(x)
def f3(x):
    if x <= 0:
        return float('nan')
    return pow(x, 2) * log(x)


# Calculate derivatives here
print("Limit approaches of f3")
print(limit_derivative(f3, 1, 2))
print(limit_derivative(f3, 1, 0.1))
print(limit_derivative(f3, 1, 0.00001))
# Limit derivative approaches 1
print("Limit approaches of f2")
print(limit_derivative(f2, 1, 2))
print(limit_derivative(f2, 1, 0.1))
print(limit_derivative(f2, 1, 0.00001))
# Limit derivative approaches 4
print("Limit approaches of f1")
print(limit_derivative(f1, 1, 2))
print(limit_derivative(f1, 1, 0.1))
print(limit_derivative(f1, 1, 0.00001))
# Limit derivative approaches 0.54
print("As h decreases, the limit derivative approaches the true derivative value. Smaller h values yield more accurate approximations.")

# Graph the true derivative
x_vals = np.linspace(1, 10, 200)
# For f1
# y_vals = [cos(val) for val in x_vals]
# For f2
y_vals = [4 * pow(val, 3) for val in x_vals]
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)


# Plot different approximated derivatives of f using limit definition of derivative
def plot_approx_deriv(f):
  x_vals = np.linspace(1, 10, 200)
  h_vals = [10, 1, .25, .01]

  for h in h_vals:
      derivative_values = []
      for x in x_vals:
          derivative_values.append(limit_derivative(f, x, h))

      plt.plot(x_vals, derivative_values, linestyle='--', label="h=" + str(h))

  plt.legend()
  plt.title("Convergence to Derivative by varying h")
  plt.show()
  plt.close()


# Plot here
# plot_approx_deriv(f1)
plot_approx_deriv(f2)

# Own function to calculate the y values of the function
def f(x):
  return 4 * pow(x, 3)

# x values
f_array_x = [x for x in np.arange(1, 10, 0.01)]
# y values
f_array_y = [f(x) for x in np.arange(1, 10, 0.01)]
# derivative calculation
f_array_deriv = np.gradient(f_array_y, 0.01)
# plot the results
plt.plot(f_array_x, f_array_deriv, linestyle='--', label="h=" + str(0.01))
plt.legend()
plt.title("Convergence to Derivative by varying x")
plt.show()
