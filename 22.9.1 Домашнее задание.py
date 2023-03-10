array = []
number = int()


while True:
    try:
        if not array:
            array = list(map(int, input("Введите последовательность 2 или более чисел в "
                                        "любом порядке через пробел: \n").split()))
        number = int(input("Введите любое число: \n"))
        break
    except ValueError:
        print("Введите число!")


def merge_sort(arr):  # "разделяй"
    if len(arr) < 2:  # если кусок массива меньше 2,
        return arr[:]  # выход из рекурсии
    else:
        middle = len(arr) // 2  # ищем середину
        left = merge_sort(arr[:middle])  # рекурсивно делим левую часть
        right = merge_sort(arr[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(arr, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2  # находим середину
    print(left, right)
    if arr[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif element < arr[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(arr, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(arr, element, middle + 1, right)


array = merge_sort(array)

i = binary_search(array, number, 0, len(array) - 1) if array[0] < number < array[-1] else 'не найден'

print('Отсортированный список', array)
print("Номер позиции наибольшего элемента меньше введенного пользователем числа: ", i)