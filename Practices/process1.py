from multiprocessing import Process, Manager
import time


def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2
    print(num ** 2)
    #print('Finished computing')


if __name__ == "__main__":
    with Manager() as manager:
        results = manager.dict()  # ✅ shared dictionary

        processes = [Process(target=longSquare, args=(n, results)) for n in range(10)]

        [p.start() for p in processes]
        [p.join() for p in processes]

        print("Results:", dict(results))
