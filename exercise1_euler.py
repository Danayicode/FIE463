# Exercise 1: Approximate Euler's number
# e = lim_{n→∞} (1 + 1/n)^n

# Import the true value of e
from math import e

# Part 1: Create approximations for n = 10, 20, 30, ..., 100 using list comprehension
euler_approx = [(1.0 + 1.0/n)**n for n in range(10, 101, 10)]

print('Approximate values of e:')
print(euler_approx)

# Part 2: Compute and print the approximation error for each element
# Error = approximation - true value
euler_error = [approx - e for approx in euler_approx]

print('\nApproximation errors:')
print(euler_error)

# Optional: Print in a nicer format
print('\n' + '='*60)
print(f'{"n":>5} {"Approximation":>15} {"Error":>15}')
print('='*60)
for i, n in enumerate(range(10, 101, 10)):
    print(f'{n:>5} {euler_approx[i]:>15.10f} {euler_error[i]:>15.10f}')
print('='*60)
print(f'\nTrue value of e: {e:.10f}')

# ==============================================================================
# Exercise 2: Approximate the sum of a geometric series
# ==============================================================================
# σ = Σ(i=0 to ∞) α^i = 1/(1-α)
# Use α = 0.1 and iterate until |σ_approx - σ_exact| < 1e-8

print('\n\n' + '='*60)
print('Exercise 2: Geometric Series')
print('='*60)

# Convergence tolerance
tol = 1e-8
alpha = 0.1

# The exact value of the sum
sigma_exact = 1.0 / (1.0 - alpha)

# Keep track of number of iterations
n = 0

# Initialize approximated sum
sigma = 0.0

# Iterate until absolute difference is smaller than tolerance level
# The built-in function abs() returns the absolute value
while abs(sigma - sigma_exact) > tol:
    # Add the next term: α^n
    # We can combine addition and assignment into a single operator +=
    # This is equivalent to: sigma = sigma + alpha**n
    sigma += alpha**n
    # Increment exponent
    n += 1

print(f'\nalpha = {alpha}')
print(f'Tolerance: {tol}')
print(f'Exact sum (1/(1-alpha)): {sigma_exact:.10f}')
print(f'Approximated sum: {sigma:.10f}')
print(f'Number of iterations: {n}')
print(f'Final error: {abs(sigma - sigma_exact):.2e}')

# Show the first few terms to understand the series
print('\nFirst 10 terms of the series:')
for i in range(10):
    print(f'  alpha^{i} = {alpha**i:.10f}')
print('='*60)

# ==============================================================================
# Exercise 3: Diagonal and band matrices
# ==============================================================================

import numpy as np

print('\n\n' + '='*60)
print('Exercise 3: Diagonal and Band Matrices')
print('='*60)

# Part 1: Create identity matrix
print('\nPart 1: Identity Matrix')
print('-' * 40)

m = n = 4
a = np.zeros((m, n), dtype=int)

# Loop over diagonal elements, set them to 1
for i in range(n):
    a[i, i] = 1

print('Identity matrix (manual):')
print(a)

# Verify with np.identity()
identity_builtin = np.identity(n, dtype=int)
print('\nIdentity matrix (np.identity):')
print(identity_builtin)

# Check if they are equal
print(f'\nAre they equal? {np.array_equal(a, identity_builtin)}')

# Part 2: Create band matrix
print('\n\nPart 2: Band Matrix')
print('-' * 40)

m = 4
n = 5
b = np.zeros((m, n), dtype=int)

# Loop over rows
for i in range(m):
    # Loop over columns
    for j in range(n):
        if i == j:
            # Main diagonal element
            b[i, j] = 1
        elif i == (j - 1):
            # Upper diagonal element (first upper diagonal)
            b[i, j] = 2
        elif i == (j + 1):
            # Lower diagonal element (first lower diagonal)
            b[i, j] = 3

print('Band matrix (4x5):')
print(b)

print('\nExplanation:')
print('  Main diagonal (i == j): 1')
print('  First upper diagonal (i == j-1): 2')
print('  First lower diagonal (i == j+1): 3')
print('='*60)
