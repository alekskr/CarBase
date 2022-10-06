import json
import pandas as pd


def intro():
    """Главное меню."""
    while True:
        print('''
   =База данных автомобилей=
1 - Список всех моделей
2 - Добавить новую модель
0 - Выход''')

        print('Введите:', end=' ')
        menu_item = int(input())
        if menu_item == 1:
            print_all_cars()
        elif menu_item == 2:
            create_new_car()
        elif menu_item == 0:
            exit()
        else:
            print('\nНеверный ввод.')


def create_new_car():
    """Занесение в базу нового автомобиля"""
    print('=Введите данные автомобиля=')
    auto = input('Марка: ').capitalize()
    model = input('Модель: ').capitalize()
    transmission = input('Механика/Автомат/Робот: ').capitalize()
    engine = input('Бензин/Дизель/Гибрид/Электро: ').capitalize()
    if engine == 'электро'.lower():
        engine_volume = input('Мощность, кВт: ') + 'кВт'
    else:
        engine_volume = input('Объем двигателя: ') + 'л'
    NewCar(auto, model, transmission, engine, engine_volume)
    # new_car = NewCar(auto, model, transmission, engine, engine_volume)
    # print(new_car.model)


def print_all_cars():
    """Вывод всех марок по алфавиту"""
    with open('auto.json', 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        print('\n=Список всех автомобилей=')

        # Сортировка сначала по ключу авто, затем по ключу модель:
        sorted_cars_dict = sorted(json_data, key=lambda x: (x['auto'], x['model']))

        # Вывод всех значений в строку, кроме значения engine_volume, после которого вывод идет с новой строки
        for i in sorted_cars_dict:
            for k, v in i.items():
                if k == 'engine_volume':
                    print(v)
                else:
                    print(v, end=' ')


class NewCar:
    """Создание нового экземпляра автомобиля"""
    def __init__(self, brand, model, transmission, engine, engine_volume):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.engine = engine
        self.engine_volume = engine_volume
        self.write_new_data_to_file()

    def write_new_data_to_file(self):
        new_data = {
            'auto': self.brand,
            'model': self.model,
            'transmission': self.transmission,
            'engine': self.engine,
            'engine_volume': self.engine_volume
        }
        with open('auto.json', 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            json_data.append(new_data)

        with open('auto.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    intro()
