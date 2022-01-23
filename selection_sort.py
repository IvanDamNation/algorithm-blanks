# Selection sort algorithm. Using time: O(n^2)
# Also, file has function of the smallest index in list.

def find_smallest(arr: list) -> int:
    """
    Function get list and find index of the smallest element.
    :param arr: list to sort
    :return: index of the smallest element of the list
    """
    smallest = arr[0]
    smallest_index = 0
    for index in range(1, len(arr)):
        if arr[index] < smallest:
            smallest = arr[index]
            smallest_index = index
    return smallest_index


def selection_sort(arr: list) -> list:
    """
    Main sorting function. Using "find_smallest" function as part
    of the algorythm.
    :param arr: list to sort
    :return: sorted list
    """
    new_arr = []
    for index in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    print(selection_sort([5, 3, 6, 2, 10]))
