import time


def selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time()
    return arr, end_time - start_time


def main():
    num_inputs = int(input("Enter the number of inputs: "))
    for i in range(num_inputs):
        arr = list(map(int, input(f"Enter input {i + 1} (space-separated integers): ").split()))
        sorted_arr, time_taken = selection_sort(arr)
        print(f"Sorted array {i + 1}: {sorted_arr}")
        print(f"Time taken to sort input {i + 1}: {time_taken:.6f} seconds")
        print("Time complexity: O(n^2)\n")


if __name__ == "__main__":
    main()
