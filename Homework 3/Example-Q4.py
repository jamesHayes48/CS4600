'''
Example from Textbook for Q4
- It works :(
'''


import numpy as np

Qa = 200 ; Qb = 50 ; Qc = 150 ; Qd = 100
E13 = 24 ; E24 = 25 ; E34 = 50
Wsm = 1000 ; Wgr = 2000
ca = 2; cb = 2

A = np.matrix([
              [Qa + E13, 0, -E13, 0],
              [0, Qc + E24, 0, -(Qa - Qd + E24)],
              [-(Qa + E13), 0, E13 + E34 + Qa, -E34],
              [0, -E24, -(Qa + E34), E34 + E24 + Qa]
              ])

b = np.array([
    [Wsm + Qa * ca],
    [Qb * cb],
    [Wgr],
    [0]
])

A = A_inv = np.linalg.inv(A)
c = A_inv * b
print(f"Solution: {c}")