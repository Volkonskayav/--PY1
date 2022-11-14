from random import shuffle
def get_unique_list_numbers() -> list[int]:
    list1 = [i for i in range(-10, 11)]
    shuffle(list1)
    list1 = list1[:15]
    return list1
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))