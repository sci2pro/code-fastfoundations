import itertools
import multiprocessing
import random
import sys
import time


def calculate_geometric_series(a, r, n=10):
    time.sleep(1) # simulate a slow process
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)


def main():
    inputs = [(random.randint(1, 10), random.random(), random.randint(10, 100)) for _ in range(10)]
    print(f"{inputs[:10] = }")
    start = time.time()
    solutions = list(itertools.starmap(calculate_geometric_series, inputs))
    print(f"itertools.starmap took            {time.time() - start:.10f} seconds")
    print(f"{solutions[:10] = }")
    start = time.time()
    # create a pool; results returned
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        solutions = pool.starmap(calculate_geometric_series, inputs)
    print(f"multiprocessing.Pool.starmap took {time.time() - start:.10f} seconds")
    print(f"{solutions[:10] = }")
    return 0


if __name__ == '__main__':
    sys.exit(main())
