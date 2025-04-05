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

def find_highest_prime(queue):
    start_time = time.time()
    highest_prime = 0
    n = 0
    count = 0
    max_limit = 75
    while time.time() - start_time < 180 and n < max_limit: #3min = 180sec
        if is_prime(n):
            highest_prime = n
            count += 1
        n += 1
    queue.put((highest_prime, count))   
    #print(f"Highest Prime Number: {highest_prime}")
    #return highest_prime

def run_prime_finder():
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target = find_highest_prime, args=(queue,))
    process.start()
    process.join()
    return queue.get()

def fibonacci(n, result_queue):
    #if n > 500:
    #    print(f"skippping fibonacci, too large: {n}")
    #    return
    a, b = 0, 1
    count = 0
    for _ in range(n):
        a, b = b, a + b
        count += 1
    result_queue.put((a, count))

async def factorial(n):
    result = 1
    count = 0
    for i in range(1, n+1):
        result *= i
        count += 1
    return result, count

async def main(highest_prime):
    fact_result, fact_count = await factorial(highest_prime) 
    return fact_result, fact_count

if __name__ == "__main__":
    #highest_prime = run_prime_finder()
    highest_prime, multi_count = run_prime_finder()
    fib_queue = multiprocessing.Queue
    fib_thread = threading.Thread(target=fibonacci, args=(highest_prime,))
    fib_thread.start()
    fib_result, fib_count = fibonacci(highest_prime)
    fact_result, fact_count = asyncio.run(main(highest_prime))

    fib_thread.join()
    fib_result, fib_count = fib_queue.get()

    print("These are the results:")
    print(f"Multi core: {highest_prime} ({multi_count})")
    print(f"Async: {fact_result} ({fact_count})")
    print(f"Threaded: {fib_result} ({fib_count})")


    #fib_thread = threading.Thread(target=fibonacci, args=(highest_prime,))
    #fib_thread.start()
    
    #try:
    #    loop = asyncio.get_event_loop()
    #    if loop.is_running():
    #        asyncio.ensure_future(main(highest_prime))
    #    else:
    #        asyncio.run(main(highest_prime)) 
    #except RuntimeError:
    #    asyncio.run(main(highest_prime))
    #loop.run_until_complete(main(highest_prime))
    #    asyncio.gather(*(factorial(highest_prime),))
    #)
    #loop.close()
    #asyncio.run(main(highest_prime))
    #fib_thread.join()
    #print("Calculations are done!")

