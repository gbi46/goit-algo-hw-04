import random
import timeit
from statistics import median
import math
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Sorting algorithms ----------

def insertion_sort(arr):
    a = arr[:]  # work on a copy
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def timsort_builtin(arr):
    b = arr[:]  
    b.sort()
    return b

# ---------- Data generators ----------

def make_random(n):
    return [random.randint(-10**9, 10**9) for _ in range(n)]

def make_sorted(n):
    return list(range(n))

def make_reversed(n):
    return list(range(n, 0, -1))

def make_nearly_sorted(n, swaps=10):
    a = list(range(n))
    swaps = min(swaps, max(0, n // 10)) or 1
    for _ in range(swaps):
        i = random.randrange(n)
        j = random.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a

dataset_factories = {
    "random": make_random,
    "sorted": make_sorted,
    "reversed": make_reversed,
    "nearly_sorted": make_nearly_sorted,
}

algorithms = {
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Timsort": timsort_builtin,
}

# ---------- Benchmark ----------

sizes = [1000, 3000, 6000, 12000]
kinds = ["random", "sorted", "reversed", "nearly_sorted"]
repeats = 5

results = []

def time_algorithm(fn, data):
    t = timeit.Timer(lambda: fn(data))
    times = t.repeat(repeat=repeats, number=1)
    return min(times), median(times)

for n in sizes:
    base = {kind: dataset_factories[kind](n) for kind in kinds}
    for kind in kinds:
        data = base[kind]
        for alg_name, alg_fn in algorithms.items():
            if alg_name == "Insertion" and n > 6000 and kind in ("random", "reversed"):
                results.append({
                    "n": n, "dataset": kind, "algorithm": alg_name,
                    "best_s": math.nan, "median_s": math.nan, "note": "skipped"
                })
                continue
            best, med = time_algorithm(alg_fn, data)
            results.append({
                "n": n, "dataset": kind, "algorithm": alg_name,
                "best_s": best, "median_s": med, "note": ""
            })

df = pd.DataFrame(results).sort_values(["dataset", "n", "algorithm"])
df.to_csv("sorting_benchmark_results.csv", index=False)
print("Done. Wrote sorting_benchmark_results.csv")

# ---------- Plot (for random dataset) ----------

df_rand = df[(df["dataset"] == "random")].dropna(subset=["median_s"])
plt.figure(figsize=(7,5), dpi=150)
for alg in ["Insertion", "Merge", "Timsort"]:
    sub = df_rand[df_rand["algorithm"] == alg]
    plt.plot(sub["n"], sub["median_s"], marker="o", label=alg)
plt.xlabel("n (array length)")
plt.ylabel("Median time (s)")
plt.title("Sorting time vs n (dataset: random)")
plt.legend()
plt.tight_layout()
plt.savefig("sorting_benchmark_random.png")
print("Done. Wrote sorting_benchmark_random.png")
