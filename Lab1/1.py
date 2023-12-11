import doctest


class Tree:
    def __init__(self, height: int, age: int, type_tree: str):
        """
        Создание и подготовка к работе объекта "дерево"

        :param height: высота дерева
        :param age: возраст дерева
        :param type_tree: вид дерева

        Примеры:
        >>> tree = Tree(500, 20, "oak")  # инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError("высота должна быть типа int")
        if height < 0:
            raise ValueError("высота должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("возраст должен быть типа int")
        if age < 0:
            raise ValueError("возраст должен быть положительным числом")
        self.age = age

        self.type_tree = type_tree

    def shed_leaves(self) -> bool:
        """
        Функция которая проверяет дерево сбрасывает листья

        :return: дерево сбрасывает листья

        Примеры:
        >>> tree = Tree(500, 20, "oak")
        >>> tree.shed_leaves()
        """

    def get_type(self) -> str:
        """
        Вернет тип дерева

        :return: тип дерева

        Примеры:
        >>> tree = Tree(500, 20, "oak")
        >>> tree.get_type()
        """


class Book:
    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "книга"

        :param title: название книги
        :param author: имя автора
        :param page_count: число страниц

        Примеры:
        >>> book = Book("Echoes of the past", "Maria Sklodovskaya", 278)  # инициализация экземпляра класса
        """
        if not isinstance(page_count, int):
            raise TypeError("число страниц должно быть типа int")
        if page_count < 0:
            raise ValueError("число страниц должно быть положительным числом")
        self.height = page_count

        self.title = title
        self.author = author

    def open(self) -> None:
        """
        открыть книгу

        Примеры:
        >>> book = Book("Echoes of the past", "Maria Sklodovskaya", 278)
        >>> book.open()
        """

    def next(self) -> None:
        """
        перелистнуть страницу

        Примеры:
        >>> book = Book("Echoes of the past", "Maria Sklodovskaya", 278)
        >>> book.next()
        """

    def back(self) -> None:
        """
        Предыдущая страница

        Примеры:
        >>> book = Book("Echoes of the past", "Maria Sklodovskaya", 278)
        >>> book.back()
        """


class Fruit:
    def __init__(self, name: str, color: str):
        """
                Создание и подготовка к работе объекта "фрукт"

                :param name: название фрукта
                :param color: цвет фрукта

                Примеры:
                >>> apple = Fruit("apple", "red")  # инициализация экземпляра класса
                """
        self.name = name
        self.color = color

    def slice(self) -> None:
        """
        нарезать фрукт

        :return: ваш фрукт нарезан

        Примеры:
        >>> apple = Fruit("apple", "red")
        >>> apple.slice()
        """

    def eat(self) -> None:
        """
        съесть фрукт

        :return: фрукт съели

        Примеры:
        >>> apple = Fruit("apple", "red")
        >>> apple.eat()
        """


if __name__ == "__main__":
    doctest.testmod()
