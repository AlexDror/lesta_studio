""" Тестовые задания для Lesta Studio """


# Задание 1
from typing import Any


def is_even(number: int) -> bool:
    """
    Проверка целого числа на четность.
    Данная реализация, возможно, менее читаема и интуитивно понятна,
    нежели стандартный подход с остатком от целочисленного деления,
    но более эффективна как по времени, так и по памяти.
    """
    return number & 1 == 0


# Задание 2
class CircularBuffer1():
    """
    Класс Циклический буфер 1
    params: size: int - размер буфера
    methods: push(value) - добавление элемента в буфер
             pop() - извлечение элемента из буфера
    remarks: Реализация класса очень простая, но медленная, поскольку
            метод списка pop(0) вызывает перемещения всех элементов списка
            на одну позицию ближе к началу
    """
    def __init__(self, size: int) -> None:
        self.__size: int = size
        self.__data: list = []

    def pop(self) -> Any:
        """ Извлекает элемент из буфера по принципу FIFO """
        if len(self.__data) > 0:
            return self.__data[0]

    def push(self, value: Any) -> None:
        """ Добавляет элемент в буфер """
        if len(self.__data) > 0:
            if len(self.__data) == self.__size:
                self.__data.pop(0)
            self.__data.append(value)


class CircularBuffer2():
    """
    Класс Циклический буфер 2
    params: size: int - размер буфера
    methods: push(value) - добавление элемента в буфер
             pop() - извлечение элемента из буфера
    remarks: Реализация класса немного сложнее, но значительно более
            эффективна по времени
    """
    def __init__(self, size: int) -> None:
        self.__size: int = size
        self.__data: list = []
        self.__index: int = 0

    def pop(self) -> Any:
        """ Извлекает элемент из буфера по принципу FIFO """
        if len(self.__data) > 0:
            return self.__data[self.__index - 1]

    def push(self, value: Any) -> None:
        """ Добавляет элемент в буфер """
        if len(self.__data) < self.__size:
            self.__data.append(value)
        else:
            self.__data[self.__index] = value
        self.__index = (self.__index + 1) % self.__size


# Задание 3
def partition(list_of_numbers: list, start: int, stop: int) -> int:
    """
    Выбираем опорный элемент, меняем элементы справа-слева, если надо
    """
    pivot: int = list_of_numbers[int((start + stop) / 2)]
    left: int = start - 1
    right: int = stop + 1
    while True:
        left += 1
        while list_of_numbers[left] < pivot:
            left += 1
        right -= 1
        while list_of_numbers[right] > pivot:
            right -= 1
        if left >= right:
            return right
        list_of_numbers[left], list_of_numbers[right] = list_of_numbers[right], list_of_numbers[left]


def quick_sort(list_of_numbers: list, start: int, stop: int) -> list:
    """
    Быстрая сортировка
    """
    if start < stop:
        partial: int = partition(list_of_numbers, start, stop)
        quick_sort(list_of_numbers, start, partial)
        quick_sort(list_of_numbers, partial + 1, stop)
    return list_of_numbers
