# Quick sort algorithm. Using time (middle): O(n * log n)
import random


def quicksort(array):
    if len(array) < 2:
        return array

    else:
        rand_index = random.randint(1, len(array) - 1)
        search_array = array[:]
        pivot = search_array.pop(rand_index)
        less = [i for i in search_array if i <= pivot]

        greater = [i for i in search_array if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    user_array = [10, 5, 2, 3]
    print(quicksort(user_array))
