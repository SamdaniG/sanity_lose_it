import time
import numpy as np
from itertools import permutations
from multiprocessing import Pool

# Step 1: Generate only valid permutations (at most 2 occurrences per number)
prime = [1, 2, 3, 4,1,2]
master_list = list(set(permutations(prime, 6)))  # Ensures unique 6-element lists

# Step 2: Convert to NumPy array for fast indexing
master_array = np.array(master_list)

# Step 3: Split into blocks based on element position
blocks = {n: master_array[master_array[:, 1] == n] for n in range(1, 5)}

# Step 4: Set-based uniqueness checks
def check_diff(a, b, num_unique):
    return all(len({a[i], b[i]}) == num_unique for i in [0, 2, 3, 4, 5])

# Step 5: Precompute rotations
def rotate1(a): return [a[0], a[2], a[3], a[4], a[1], a[5]]
def rotate2(a): return rotate1(rotate1(a))
def rotate3(a): return rotate1(rotate2(a))
def left1(a): return [a[3], a[0], a[2], a[5], a[4], a[1]]
def left2(a): return left1(left1(a))
def left3(a): return left1(left2(a))

rotation_funcs = [lambda x: x, rotate1, rotate2, rotate3, left1, left2, left3]
precomputed_rotations = {tuple(a): [func(a) for func in rotation_funcs] for a in master_list}

# Step 6: Check final uniqueness across all rotations
def final_check(yo):
    a, b, c, d = yo
    rotation_combinations = [
        (func_a(a), func_b(b), func_c(c), func_d(d))
        for func_a in rotation_funcs
        for func_b in rotation_funcs
        for func_c in rotation_funcs
        for func_d in rotation_funcs
    ]
    return any(all(len(set(combo[i])) == 4 for i in range(6)) for combo in rotation_combinations)

# Step 7: Parallelized processing
def process_combination(data):
    a, b, c, d = data
    if check_diff(a, b, 2) and check_diff(a, c, 3) and check_diff(a, d, 4):
        if final_check([a, b, c, d]):
            return [a, b, c, d]
    return None

# Generate all valid (a, b, c, d) combinations
combinations = [(a, b, c, d) for a in blocks[1] for b in blocks[2] for c in blocks[3] for d in blocks[4]]

# Step 8: Run parallel processing
start_time = time.time()
with Pool() as pool:
    results = pool.map(process_combination, combinations)

possible_solution = [r for r in results if r is not None]

# Step 9: Buffered file writing
buffer = []
with open("final_solution.txt", "w") as file:
    for solution in possible_solution:
        buffer.append(str(solution) + "\n")
        if len(buffer) >= 1000:  # Write every 1000 solutions
            file.writelines(buffer)
            buffer = []
    if buffer:
        file.writelines(buffer)  # Write remaining solutions

# Step 10: Final log
end_time = time.time()
print(f"Total Possible Solutions: {len(possible_solution)}")
print(f"Execution Time: {(end_time - start_time):.2f} seconds")
print("The file has finally finished running\a")  # Beep sound added
