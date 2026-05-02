import timeit


def benchmark_list_comprehension():
    result = timeit.timeit(
        "[x * 2 for x in range(10000)]",
        number=1000
    )
    print("List comprehension:", result)


def benchmark_for_loop():
    code = """
result = []
for x in range(10000):
    result.append(x * 2)
"""
    result = timeit.timeit(code, number=1000)
    print("For loop with append:", result)


def benchmark_string_join():
    code = """
words = ["python"] * 10000
result = "".join(words)
"""
    result = timeit.timeit(code, number=1000)
    print("String join:", result)


def benchmark_string_plus():
    code = """
result = ""
for _ in range(10000):
    result += "python"
"""
    result = timeit.timeit(code, number=100)
    print("String +=:", result)


def benchmark_dict_lookup():
    code = """
data = {i: i * 2 for i in range(10000)}
for i in range(10000):
    value = data[i]
"""
    result = timeit.timeit(code, number=1000)
    print("Dict lookup:", result)


def benchmark_list_search():
    code = """
data = list(range(10000))
for i in range(100):
    value = 9999 in data
"""
    result = timeit.timeit(code, number=1000)
    print("List search:", result)


if __name__ == "__main__":
    print("Benchmark 1: list comprehension vs for loop")
    benchmark_list_comprehension()
    benchmark_for_loop()

    print("\nBenchmark 2: string join vs string +=")
    benchmark_string_join()
    benchmark_string_plus()

    print("\nBenchmark 3: dict lookup vs list search")
    benchmark_dict_lookup()
    benchmark_list_search()