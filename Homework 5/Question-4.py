import numpy as np
import matplotlib.pyplot as plt
from sympy.printing.numpy import const

t_data = np.array([15, 45, 75, 105, 135, 165, 225, 255, 285, 315, 345])
temp_data = np.array([3.4, 4.7, 8.5, 11.7, 16, 18.7, 19.7, 17.1, 12.7, 7.7, 5.1])

omega = (2 * np.pi) / 365



# Coefficients in matrix
N = len(t_data)
sum_cos = np.sum(np.cos(omega * t_data))
sum_sin = np.sum(np.sin(omega * t_data))
sum_cos_square = np.sum((np.cos(omega * t_data)) ** 2)
sum_cos_sin = np.sum((np.cos(omega * t_data)) * np.sin(omega * t_data))
sum_sin_square = np.sum((np.sin(omega * t_data)) ** 2)

# Constants
sum_y = np.sum(temp_data)
sum_y_cos = np.sum(temp_data * np.cos(omega * t_data))
sum_y_sin = np.sum(temp_data * np.sin(omega * t_data))

# Normal Equations in matrix form
normal_eq_matrix = np.matrix([
    [N, sum_cos, sum_sin],
    [sum_cos, sum_cos_square, sum_cos_sin],
    [sum_sin, sum_cos_sin, sum_sin_square]
])

# Constants in Matrix
constant_eq = np.matrix([
    [sum_y],
    [sum_y_cos],
    [sum_y_sin]
])
print(f"Coefficient matrix: {normal_eq_matrix}")

b_matrix = np.linalg.solve(normal_eq_matrix, constant_eq)

# Extract final coefficients for model
A0 = np.asarray(b_matrix[0][0]).item()
A1 = np.asarray(b_matrix[1][0]).item()
B1 = np.asarray(b_matrix[2][0]).item()

print(f"Final answers: "
      f"A0 = {A0} \n"
      f"A1 = {A1} \n"
      f"B1 = {B1}")

x_line = np.linspace(min(t_data), max(t_data))
y_line = A0 + (A1 * np.cos(omega * x_line)) + (B1 * np.sin(omega * x_line))

plt.figure()
plt.xlabel('t,d')
plt.ylabel('T, Degrees Celsius')
plt.title('Scatter plot with Least-Squares fit of a sinusoid Model')
plt.scatter(t_data, temp_data, color='red', label='Sample data')
plt.plot(x_line, y_line, color='teal', label='Line of Best Fit')
plt.legend()
plt.show()
