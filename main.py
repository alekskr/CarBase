import json
import pandas as pd


def intro():
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
    """занести в базу новый автомобиль"""
    print('=Введите данные автомобиля=')
    new_car = NewCar(input('auto: ').capitalize(),
                     input('model: ').capitalize(),
                     input('transmission: ').lower(),
                     input('engine: '))
    print(new_car.model)


def print_all_cars():
    """вывести список марок"""
    with open('auto.json', 'r') as json_file:
        cars = json.load(json_file)
        print('=Список всех автомобилей=')
        # print(cars)

        for i in cars:
            print(i['auto'], i['model'], i['transmission'], i['engine'])


class NewCar:
    def __init__(self, brand, model, transmission, engine):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.engine = engine
        self.write_new_data_to_file()

    def write_new_data_to_file(self):
        new_data = {
            'auto': self.brand,
            'model': self.model,
            'transmission': self.transmission,
            'engine': self.engine
        }
        with open('auto.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_data.append(new_data)

        with open('auto.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    intro()

# new_car = {'auto': input('auto: ').capitalize(),
#            'model': input('model: ').capitalize(),
#            'transmission': input('transmission: ').lower(),
#            'engine': input('engine: ')}

# with open('C:\\Python projects\\study\\инструкции, циклы, функции, модули и т.д\\auto.json', 'r') as json_file:
#     json_data = json.load(json_file)
#     print(json_data)
#     json_data.append(new_car)
#
# with open('C:\\Python projects\\study\\инструкции, циклы, функции, модули и т.д\\auto.json', 'w') as json_file:
#     json.dump(json_data, json_file)

