# @title
from ipywidgets import interact, Dropdown
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from collections import Counter
import ipywidgets as widgets
from ipywidgets import interactive

def find_all_sums_of_two_squares(n):
    results = []
    for a in range(1, int(n**0.5) + 1):
        for b in range(a, int(n**0.5) + 1):
                if a**2 + b**2 == n:
                    results.append((a, b))
    return results

def compute_degeneracy(combinations, dim):
    d = 0
    for combination in combinations:
        count = Counter(combination)
        deg = factorial(dim) // np.prod([factorial(v) for v in count.values()])
        d += deg
    return d

def plot_sums_of_two_squares(n):
    numbers = []
    combinations = []
    degeneracies = []

    for num in range(1, n + 1):
        results = find_all_sums_of_two_squares(num)
        if results:
            numbers.append(num)
            combinations.append(results)
            degeneracies.append(compute_degeneracy(results, 2))

    result_array = np.array(numbers)
    degeneracy_array = np.array(degeneracies)
    print('Total number of degenerate states within index', n, 'is', len(result_array))
    print('Total number of states within index', n, 'is', sum(degeneracy_array))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    x = np.arange(1, len(result_array) + 1)

    ax1.plot(x, result_array , color = 'orange')
    ax1.scatter(x, result_array, color='g', s=20)
    ax1.set_xlabel('Degenerate State')
    ax1.set_ylabel('Energy')
    ax1.set_title('Energy vs Degenerate State')
    ax1.grid(True)

    ax2.plot(x, degeneracy_array, color='b')
    ax2.scatter(x, degeneracy_array, color='r', s=30)
    ax2.set_xlabel('Degenerate State')
    ax2.set_ylabel('Degeneracy')
    ax2.set_title('Degeneracy vs Degenerate State')
    ax2.grid(True)

    plt.tight_layout()
    plt.figtext(0.5, 0.01, '\u00A9 Designed by Avoy Jana (MSc, IITD)', ha='center', va='top', fontsize=12, color='gray')
    plt.show()

    print("\nEnergies, Combinations and Degeneracies:")
    for i, num in enumerate(numbers):
        print(f"{num}: {combinations[i]} with d = {degeneracies[i]}")

def find_all_sums_of_three_squares(n):
    results = []
    for a in range(1, int(n**0.5) + 1):
        for b in range(a, int(n**0.5) + 1):
            for c in range(b, int(n**0.5) + 1):
                if a**2 + b**2 + c**2 == n:
                    results.append((a, b, c))
    return results

def plot_sums_of_three_squares(n):
    numbers = []
    combinations = []
    degeneracies = []

    for num in range(1, n + 1):
        results = find_all_sums_of_three_squares(num)
        if results:
            numbers.append(num)
            combinations.append(results)
            degeneracies.append(compute_degeneracy(results, 3))

    result_array = np.array(numbers)
    degeneracy_array = np.array(degeneracies)
    print('Total number of degenerate states within index', n, 'is', len(result_array))
    print('Total number of states within index', n, 'is', sum(degeneracy_array))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    x = np.arange(1, len(result_array) + 1)

    ax1.plot(x, result_array , color = 'orange')
    ax1.scatter(x, result_array, color='g', s=20)
    ax1.set_xlabel('Degenerate State')
    ax1.set_ylabel('Energy')
    ax1.set_title('Energy vs Degenerate State')
    ax1.grid(True)

    ax2.plot(x, degeneracy_array, color='b')
    ax2.scatter(x, degeneracy_array, color='r', s=30)
    ax2.set_xlabel('Degenerate State')
    ax2.set_ylabel('Degeneracy')
    ax2.set_title('Degeneracy vs Degenerate State')
    ax2.grid(True)

    plt.tight_layout()
    plt.figtext(0.5, 0.01, '\u00A9 Designed by Avoy Jana (MSc, IITD)', ha='center', va='top', fontsize=12, color='gray')
    plt.show()

    print("\nEnergies, Combinations and Degeneracies:")
    for i, num in enumerate(numbers):
        print(f"{num}: {combinations[i]} with d = {degeneracies[i]}")

code_selector = Dropdown(
    options={'Two Dimensional Box': plot_sums_of_two_squares, 'Three dimensional Box': plot_sums_of_three_squares},
    value=plot_sums_of_two_squares,
    description='Potential:'
)

# Define a function to run the selected code
def run_selected_code(selected_code, n):
    selected_code(n)

n_slider = widgets.IntSlider(value=100, min=1, max=200, step=1, description='n')
# Create an interactive widget
interact(
    run_selected_code,
    selected_code=code_selector,
    n=n_slider
)
