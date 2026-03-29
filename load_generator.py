import multiprocessing
import time


def stress():
    while True:
        pass


if __name__ == "__main__":
    print("🔥 Generating CPU load...")

    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=stress)
        p.start()
        processes.append(p)

    time.sleep(60)

    for p in processes:
        p.terminate()

    print("✅ Load test finished")