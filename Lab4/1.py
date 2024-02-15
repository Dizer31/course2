import doctest


class Vehicle:
    """Базовый класс для транспортных средств"""

    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор класса Vehicle.


        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("tesla", "E100", 1965)
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Vehicle(brand=\"{self.brand}\", model=\"{self.model}\", year={self.year})"

    def start(self) -> None:
        """Запускает двигатель транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("tesla", "E100", 1965)
        >>> vehicle.start()
        """

    def stop(self) -> None:
        """Останавливает двигатель транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("tesla", "E100", 1965)
        >>> vehicle.stop()
        """


class Car(Vehicle):
    """Дочерний класс для автомобиля"""

    def __init__(self, brand: str, model: str, year: int, color: str):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param color: Цвет автомобиля.

        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        """
        super().__init__(brand, model, year)
        self.color = color

    def __str__(self) -> str:
        return f"{self.color} {self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Car(brand=\"{self.brand}\", model=\"{self.model}\", year={self.year}, color=\"{self.color}\")"

    def lock_doors(self) -> None:
        """Закрывает двери автомобиля.

        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        >>> tesla.lock_doors()
        """
        self.doors_locked = True

    def unlock_doors(self) -> None:
        """Открывает двери автомобиля.

        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        >>> tesla.unlock_doors()
        """
        self.doors_locked = False

    def stop(self) -> None:
        """Останавливает двигатель автомобиля.

        Метод перегружен, так как необходимо выключить музыку
        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        >>> tesla.stop()
        """
        self.engine_running = False
        self.turn_off_music()

    def play_music(self, song: str) -> None:
        """
        Воспроизводит музыку в автомобиле.

        :param song: Название песни.

        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        >>> tesla.play_music("Never Gonna Give You Up")
        """
        self.current_song = song

    def turn_off_music(self) -> None:
        """
        Выключить музыку в автомобиле.

        Примеры:
        >>> tesla = Car("tesla", "model s", 2012, "red")
        >>> tesla.turn_off_music()
        """
        self.current_song = None


if __name__ == "__main__":
    doctest.testmod()
