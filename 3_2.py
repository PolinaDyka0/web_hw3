from typing import List
import time
from multiprocessing import Pool, cpu_count

def factorize_sync(*numbers: int) -> List[List[int]]:
    results = []
    for n in numbers:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        results.append(factors)
    return results

def paral(*numbers):
    with Pool(cpu_count()) as p:
        result = p.map(factorize_paral, numbers)
        p.close()  
        p.join()  
    return result
        
def factorize_paral(numbers):
    factors = []
    for i in range(1, numbers+1):
        if numbers % i == 0:
            factors.append(i)
    return factors

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    print("Time taken: %s seconds" % (time.time() - start_time))
    return result



if __name__ == "__main__":

    a, b, c, d = measure_time(factorize_sync, 128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


    a, b, c, d  = measure_time(lambda: paral(128, 255, 99999, 10651060))

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]






