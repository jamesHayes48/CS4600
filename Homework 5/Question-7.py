from scipy.integrate import quad

def f(x):
    return -0.55 * x ** 4 + 0.86 * x ** 3 - 4.2 * x ** 2 + 6.3 * x + 2

result, error = quad(f,0, 8)

print(f"Result {result}, Error: {error}")