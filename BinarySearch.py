def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1
    return None

my_list = [1,7,19,22,157,212,222]

print(f'Необходимый эл-т под индексом: {binary_search(my_list, 222)}')
