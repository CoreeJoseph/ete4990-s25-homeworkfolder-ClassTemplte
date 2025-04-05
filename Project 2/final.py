import time
import threading
import multiprocessing
import asyncio

def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n** 0.5) +1):
        if n % i ==0:
            return False
    return True

def find_highest_prime():
    start_time = time.time()
    highest_prime = 0
    n = 0
    while time.time() - start_time < 180: #3min = 180sec
        if is_prime(n):
            highest_prime = n
        n += 1
    print(f"Highest Prime Number: {highest_prime}")
    return highest_prime

def run_prime_finder():
    process = multiprocessing.Process(target = find_highest_prime)
    process.start()
    process.join()
    return find_highest_prime

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(f"Fibonacci of {n}: {a}")

async def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n}: {result}")

async def main(highest_prime):
    await asyncio.gather(factorial(highest_prime)) 

if __name__ == "__main__":
    highest_prime = run_prime_finder()
    fib_thread = threading.Thread(target=fibonacci, args=(highest_prime,))
    fib_thread.start()
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main(highest_prime))
    #    asyncio.gather(*(factorial(highest_prime),))
    #)
    #loop.close
    asyncio.run(main(highest_prime))
    fib_thread.join()
    print("Calculations are done!")
