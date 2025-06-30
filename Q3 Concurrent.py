import threading
import time
import random

# Thread to run multiple tasks together at the same time
# Function to generate 100 random numbers
def generate_random_numbers(num, results):
    # To slow down the programme, simulate the multithreading
    # Take a short break before starting next round
    time.sleep(0.1)
    random_numbers = [random.randint(0, 10000) for _ in range(100)]
    results[num] = random_numbers

def multi_threading_test():
    # List to store time
    total_times = []

    # Perform 10 rounds of testing
    for round_num in range(1, 11):
        # Resets the result on every new round start
        results = {}
        # Empty list to store threads
        threads = []

        # Build in Python function to calculate nanoseconds
        start_time = time.time_ns()

        # Create 3 threads using loop
        for i in range(3):
            # A build in functions in Python to create a new thread
            # Target is to call the functions to run and arguments
            # Result is a shared dictionary where each thread saves its output
            thread = threading.Thread(target=generate_random_numbers, args=(i, results))
            # Save the threads into the thread list
            threads.append(thread)
            # Runs the thread at same time
            thread.start()

        for thread in threads:
            # Wait for all the threads to finish before continue new round
            thread.join()

        end_time = time.time_ns()
        # Check how long the threads run
        elapsed_time = end_time - start_time
        total_times.append(elapsed_time)

        print(f"Round {round_num}: Time = {elapsed_time} ns")

    avg_time = sum(total_times) / len(total_times)
    return avg_time


def non_threading_test():
    total_times = []

    for round_num in range(1, 11):
        start_time = time.time_ns()
        results = {}

        for i in range(3):  # No threads
            # Not using thread, so will just call the function and loop it
            generate_random_numbers(i, results)

        end_time = time.time_ns()
        elapsed_time = end_time - start_time
        total_times.append(elapsed_time)

        print(f"Round {round_num}: Time = {elapsed_time} ns")

    avg_time = sum(total_times) / len(total_times)
    return avg_time



def main():
    print("\n\tMultithreading Results")
    print("===============================")
    multi_avg_time = multi_threading_test()

    print("\n\tNon-Threading Results")
    print("===============================")
    non_avg_time = non_threading_test()

    print("\n=========================================")
    print("\t\tAverage Time Comparison\n=========================================")
    print(f"Multithreading Average Time: {multi_avg_time:.2f} ns")
    print(f"Non-threading Average Time : {non_avg_time:.2f} ns")

if __name__ == "__main__":
    main()
