import time
from multiprocessing import Pool, cpu_count


def factorize_sync(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def get_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]


def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(get_factors, numbers)
    return result


if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    print("Синхронна версія:")
    start_time = time.time()
    sync_result = factorize_sync(*numbers)
    end_time = time.time()
    print(f"Time: {end_time - start_time} seconds")
    for factors in sync_result:
        print(factors)

    print("\nПаралельна версія:")
    start_time = time.time()
    parallel_result = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Time: {end_time - start_time} seconds")
    for factors in parallel_result:
        print(factors)

    a, b, c, d = parallel_result
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

