from multiprocessing import Process, Manager
import time

def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2  # store result in shared dictionary
    print(f"Square of {num} is {num**2}")

if __name__ == "__main__":
    with Manager() as manager:
        results = manager.dict()

        p1 = Process(target=longSquare, args=(1, results))
        p2 = Process(target=longSquare, args=(2, results))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print(dict(results))  # convert manager dict to normal dict