class Fraction:
    """Класс представляет собой дробь"""
    def __init__(self, numerator: int, denominator: int):
        """
        numerator:     числитель представляет собой целое неотрицательное число
        denominator:   знаменатель представляет собой целое неотрицательное число
        """
        if isinstance(numerator, int) and numerator >= 0:
            self.__numerator = numerator
        else:
            raise ValueError('Числитель должен быть целым неотрицательным числом')
        if isinstance(denominator, int) and denominator > 0:
            self.__denominator = denominator
        elif isinstance(denominator, int) and denominator == 0:
            raise ZeroDivisionError('Знаменатель не может быть равным 0')
        else:
            raise ValueError('Знаменатель должен быть целым неотрицательным числом')

    @property
    def numerator(self) -> int:
        return self.__numerator
    
    @numerator.setter
    def numerator(self, numer: int):
        try:
            if isinstance(numer, int) and numer >= 0:
                self.__numerator = numer
            else:
                raise ValueError('Числитель должен быть целым неотрицательным числом')
        except ValueError as err:
            print(err)

    @property
    def denominator(self) -> int:
        return self.__denominator
    
    @denominator.setter
    def denominator(self, denom: int):
        try:
            if isinstance(denom, int) and denom > 0:
                self.__denominator = denom
            elif isinstance(denom, int) and denom == 0:
                raise ZeroDivisionError('Знаменатель не может быть равным 0')
            else:
                raise ValueError('Знаменатель должен быть целым неотрицательным числом')
        except (ZeroDivisionError, ValueError) as err:
            print(err)
    
    def read(self):
        """Метод считывает числитель и знаменатель с клавиатуры"""
        try:
            self.numerator = int(input('Введите числитель: '))
            self.denominator = int(input('Введите знаменатель: '))
        except Exception:
            print('Аргумент должен быть целым неотрицательным числом')
    
    def ipart(self) -> int:
        """Метод возвращает целую часть дроби"""
        return self.numerator // self.denominator
    
    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'
