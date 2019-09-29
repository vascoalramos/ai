def selection_sort(lst):
    for i in range(len(lst)):
        # Find the minimum element in remaining unsorted lst
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the lst from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)
    return lst


def generic_selection_sort(lst, compare):
    for i in range(len(lst)):
        # Find the minimum element in remaining unsorted lst
        min_idx = i
        for j in range(i+1, len(lst)):
            if compare(lst[min_idx], lst[j]) > 0:
                min_idx = j
        # Swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def generic_bubble_sort(lst, compare):
    n = len(lst)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the lst from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if compare(lst[j], lst[j+1]) > 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def generic_partition(lst, low, high, compare):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if compare(lst[j], pivot) <= 0:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def generic_quick_sort(lst, low, high, compare):
    if low < high:
        pi = generic_partition(lst, low, high, compare)
        generic_quick_sort(lst, low, pi - 1, compare)
        generic_quick_sort(lst, pi + 1, high, compare)
    return lst


if __name__ == "__main__":
    lst = [-10, 3, 100, 2, -20, 5, 1, 4, 2]
    print(f"Selection sort: {selection_sort(lst[:])}")
    print(f"Bubble sort: {bubble_sort(lst[:])}")
    print(f"Quick sort: {quick_sort(lst[:], 0, len(lst) - 1)}")

    def compare(x, y): return x - y
    print(f"Generic selection sort: {generic_selection_sort(lst[:], compare)}")
    print(f"Generic bubble sort: {generic_bubble_sort(lst[:], compare)}")
    print(
        f"Generic quick sort: {generic_quick_sort(lst[:], 0, len(lst) - 1, compare)}")
