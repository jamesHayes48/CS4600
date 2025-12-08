import numpy as np
import matplotlib.pyplot as plt

t_data = np.array([15, 45, 75, 105, 135, 165, 225, 255, 285, 315, 345])
temp_data = np.array([3.4, 4.7, 8.5, 11.7, 16, 18.7, 19.7, 17.1, 12.7, 7.7, 5.1])

N = len(t_data)
omega = np.pi / 365
A0 = np.sum(temp_data) / N
A1 = (2 * np.sum(temp_data * (np.cos(omega * t_data)))) / N
B1 = (2 * np.sum(temp_data * (np.sin(omega * t_data)))) / N

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
