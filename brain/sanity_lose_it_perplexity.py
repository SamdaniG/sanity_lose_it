import numpy as np
from numba import cuda, jit
import time

# Constants
PRIME_RANGE = np.array([1,2,3,4,5,6], dtype=np.int32)
ELEMENT_CHECK = np.array([0,2,3,4,5], dtype=np.int32)

@jit(nopython=True)
def multiplicity_check(arr):
    """
    Check if any element appears more than twice in the array
    Returns 0 if valid, >0 if invalid
    """
    counts = np.zeros(7, dtype=np.int32)
    for x in arr:
        counts[x] += 1
        if counts[x] > 2:
            return 1
    return 0

@jit(nopython=True)
def process_valid_combinations(combinations):
    """
    Process valid combinations and separate them into blocks
    based on the value in position 1
    """
    block1 = []
    block2 = []
    block3 = []
    block4 = []
    
    for combo in combinations:
        if combo[1] == 1:
            block1.append(combo)
        elif combo[1] == 2:
            block2.append(combo)
        elif combo[1] == 3:
            block3.append(combo)
        else:
            block4.append(combo)
            
    return np.array(block1), np.array(block2), np.array(block3), np.array(block4)

@cuda.jit
def multiplicity_check_kernel(input_array, output_flags):
    """GPU kernel for multiplicity check"""
    idx = cuda.grid(1)
    if idx < input_array.shape[0]:
        counts = cuda.local.array(7, dtype=np.int32)
        for i in range(7):
            counts[i] = 0
            
        for i in range(6):
            counts[input_array[idx, i]] += 1
            if counts[input_array[idx, i]] > 2:
                output_flags[idx] = 1
                return
        output_flags[idx] = 0

@jit(nopython=True)
def generate_combinations():
    """Generate all possible combinations"""
    combinations = []
    for a in PRIME_RANGE:
        for b in PRIME_RANGE:
            for c in PRIME_RANGE:
                for d in PRIME_RANGE:
                    for e in PRIME_RANGE:
                        for f in PRIME_RANGE:
                            combo = np.array([a,b,c,d,e,f], dtype=np.int32)
                            if multiplicity_check(combo) == 0:
                                combinations.append(combo)
    return np.array(combinations, dtype=np.int32)

@jit(nopython=True)
def check_diff2(a, b):
    """Check if two arrays have different elements at specified positions"""
    for i in ELEMENT_CHECK:
        if a[i] == b[i]:
            return False
    return True

@jit(nopython=True)
def check_diff3(a, b, c):
    """Check if three arrays have different elements at specified positions"""
    for i in ELEMENT_CHECK:
        values = set([a[i], b[i], c[i]])
        if len(values) != 3:
            return False
    return True

@jit(nopython=True)
def check_diff4(a, b, c, d):
    """Check if four arrays have different elements at specified positions"""
    for i in ELEMENT_CHECK:
        values = set([a[i], b[i], c[i], d[i]])
        if len(values) != 4:
            return False
    return True

def main():
    # Start timing
    start_time = time.time()
    
    print("Generating combinations...")
    combinations = generate_combinations()
    print(f"Total combinations generated: {len(combinations)}")
    
    # Process into blocks
    block1, block2, block3, block4 = process_valid_combinations(combinations)
    print(f"Block sizes: {len(block1)}, {len(block2)}, {len(block3)}, {len(block4)}")
    
    # Find solutions
    solutions = []
    for a in block1:
        for b in block2:
            if not check_diff2(a, b):
                continue
            for c in block3:
                if not check_diff3(a, b, c):
                    continue
                for d in block4:
                    if check_diff4(a, b, c, d):
                        solutions.append([a, b, c, d])
                        print(f"Solution found! Total solutions: {len(solutions)}")
    
    # Save results
    np.save("solutions.npy", np.array(solutions))
    
    print(f"Total execution time: {(time.time() - start_time):.2f} seconds")
    print(f"Total solutions found: {len(solutions)}")

if __name__ == "__main__":
    main()
