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
    def get_brand(self):
        return self.__brand

    @property
    def get_engine_power(self):
        return self.__engine_power

    @property
    @to_uppercase
    def get_gearbox(self):
        return self.__gearbox

    @property
    def get_number_of_axes(self):
        return self.__number_of_axes

    def set_brand(self,brand):
        self.__brand=brand
    def set_engine_power(self,engine_power):
        self.__engine_power=engine_power
    def set_gearbox(self,gearbox):
        self.__gearbox=gearbox
    def set_number_of_axes(self,number_of_axes):
        self.__number_of_axes=number_of_axes