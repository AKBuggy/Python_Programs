class Merge:
    @staticmethod
    def merge_arr(arr, left, mid, right):
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        return arr
