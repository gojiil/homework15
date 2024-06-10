# Введите ваше решение ниже
class NegativeValueError(ValueError):
    pass

class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

            
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        try:
            if value < 0:
                raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        except NegativeValueError as e:
            logger.error(msg=e)
            return
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        try:
            if value < 0:
                raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        except NegativeValueError as e:
            logger.error(msg=e)
            return
        self._height = value

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        perimeter = 2 * (self.width + self.height)
        logger.info(f'Периметр прямоугольника равен {perimeter}')
        return perimeter

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        area = self.width * self.height
        logger.info(f'Площадь прямоугольника равна {area}')
        return area

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        logger.info(msg=f'В результате сложения получен новый прямоугольник со сторонами {width} и {height}')
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        logger.info(msg=f'В результате вычитания получен новый прямоугольник со сторонами {width} и {height}')
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"
    


if __name__ == "__main__":
    import logging

    FORMAT = '{levelname:<8} - {asctime}. ' \
    'в {created} секунд записала сообщение: {msg}'

    logging.basicConfig(filename='logfile.log', filemode='w', format=FORMAT, style='{', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)

    rect1 = Rectangle(5)
    rect2 = Rectangle(2, 4)
    rect3 = Rectangle(-3)
    rect4 = Rectangle(5, -7)

    rect1.area()
    rect2.perimeter()
    rect5 = rect1.__add__(rect2)
    rect6 = rect1.__sub__(rect2)
