if __name__ == "__main__":
    # Write your solution here
    class Animal:
        """ Базовый класс животного. """

        def __init__(self, _name: str, _type: str):
            self._name = _name
            self._type = _type

        @property
        def name(self):
            return self._name

        @property
        def type(self):
            return self._type

        def __str__(self):
            return f"Животное {self.name}. Вид {self._type}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, type={self._type!r})"


    class Panda(Animal):
        """ Дочерний класс животного. """

        def __init__(self, _name: str, _type: str, population: int):
            super().__init__(_name, _type)
            if isinstance(population, int):
                if population > 0:
                    self.population = population
                else:
                    raise AttributeError(f'Неправильное количество животных: {population!r}')
            else:
                raise AttributeError(f'Неправильный тип для популяции: {population!r}')

        def __str__(self):
            return f"Животное {self._name}. Тип {self._type} Популяция: {self.population}"


    pass
