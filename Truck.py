def to_uppercase(func):
    def wrapper(*args, **kwargs):
        # Вызываем оригинальный метод
        result = func(*args, **kwargs)
        # Проверяем, является ли результат строкой
        if isinstance(result, str):
            return result.upper()  # Преобразуем строку в верхний регистр
        return result  # Возвращаем оригинальный результат, если это не строка

    return wrapper

class Truck:
    def __init__(self, brand: str='',engine_power: int=0,gearbox: str='',number_of_axes:int=0):
        self.__brand=brand
        self.__engine_power=engine_power
        self.__gearbox=gearbox
        self.__number_of_axes=number_of_axes

    @to_uppercase
    def check_brand(self, brand):
            return self.__brand.lower()==brand.lower()

    @property
    @to_uppercase
    def brand(self): # def brand
        return self.__brand

    @property
    def engine_power(self):
        return self.__engine_power

    @property
    @to_uppercase
    def gearbox(self):
        return self.__gearbox

    @property
    def number_of_axes(self):
        return self.__number_of_axes

#__str__
    @brand.setter
    def brand(self,brand): # brand
        self.__brand=brand

    @engine_power.setter
    def engine_power(self,engine_power):
        self.__engine_power=engine_power

    @gearbox.setter
    def gearbox(self,gearbox):
        self.__gearbox=gearbox

    @number_of_axes.setter
    def number_of_axes(self,number_of_axes):
        self.__number_of_axes=number_of_axes

    def __str__(self):
        return (f'Brand: {self.brand}\n'
                f'Engine power: {self.engine_power}\n'
                f'Type of Gearbox: {self.gearbox}\n'
                f'Number of axes: {self.number_of_axes}')