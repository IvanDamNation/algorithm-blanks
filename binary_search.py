# Binary search algorithm. Using time: O(log n)
# Sort search list before usage!

def binary_search(search_list, item):
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) / 2
        guess = search_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    test = [11, 30, 57, 87, 99]
    
    print(binary_search(test, 30))  # => 1
    print(binary_search(test, -1))  # => None
