def binary_search(list_search:list, item:int):
    low = 0
    high = len(list_search) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list_search[mid]

        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return "Элемент не найден"

my_list = [0,2,4,6,8,10,20,50,100]

print(f'Необходимый эл-т под индексом: {binary_search(my_list, 111)}')
