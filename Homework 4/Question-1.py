'''
Question 1b - Gauss-Seidel Method
'''

import numpy as np


def function_1(x_2, x_3):
    return (27 - 2 * x_2 + x_3) / 10


def function_2(x_1, x_3):
    return (-61.5 + (3 * x_1) + (-2 * x_3)) / -6


def function_3(x_1, x_2):
    return (-21.5 - x_1 - x_2) / 5


def error_calc(new, old):
    return abs((new - old) / new) * 100


def gauss_seidel(rel_error):
    # Initialize with initial guess
    assume = [0, 0, 0]

    # Hold previous answers
    prev_answer = []

    # Hold relative errors of each variable
    error_array = [100, 100, 100]

    # Use to check for relative error
    condition = lambda error: error > rel_error

    # Iteration counter
    iter_count = 0

    while any(condition(a) for a in error_array):
        prev_answer = assume.copy()
        print(prev_answer)
        # Find and store new x1
        new_x_1 = function_1(assume[1], assume[2])
        assume[0] = new_x_1

        # Find and store new x2
        new_x_2 = function_2(assume[0], assume[2])
        assume[1] = new_x_2

        # Find and store new x3
        new_x_3 = function_3(assume[0], assume[1])
        assume[2] = new_x_3

        # Check for relative error of each answer
        if iter_count != 0:
            error_array[0] = error_calc(assume[0], prev_answer[0])
            error_array[1] = error_calc(assume[1], prev_answer[1])
            error_array[2] = error_calc(assume[2], prev_answer[2])

        print(f"Iteration {iter_count}: \n"
              f"x1 = {assume[0]} error_x1 = {error_array[0]} ; "
              f"x2 = {assume[1]} error_x2 = {error_array[1]} ; "
              f"x3 = {assume[2]} error_x3 = {error_array[2]}"
              )

        iter_count += 1


gauss_seidel(5)
