from database import DatabaseConnection
from pet_repository import PetRepository
from view import View
from counter import Counter
from pet import Pet

class Controller:
    def __init__(self):
        self.db_connection = DatabaseConnection(
            dbname="Human_friends2",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        self.db_connection.connect()
        self.db_connection.create_table()

        self.pet_repository = PetRepository(self.db_connection.connection)
        self.view = View()
        self.counter = Counter()

    def main_menu(self):
        pet_count = self.pet_repository.get_pets_count()
        self.counter.set_count(pet_count)

        while True:
            self.view.display_main_menu()
            choice = input("Введите Ваш выбор: ")

            if choice == '0':
                all_pets = self.pet_repository.get_all_pets()
                self.view.display_pets(all_pets)
            elif choice == '1':
                self.add_new_pet()
            elif choice == '2':
                self.show_pet_class()
            elif choice == '3':
                self.show_pet_commands()
            elif choice == '4':
                self.train_pet_commands()
            elif choice == '5':
                self.remove_pet()
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

        self.db_connection.close()

    def add_new_pet(self):
        name = input("Введите имя животного: ")
        pet_class = input("Введите класс животного (Кошка, Собака или Хомяк): ")
        if name and pet_class:
            print("Создание питомца с именем:", name, "и классом:", pet_class)
            pet = Pet(name, pet_class)
            result_create = self.pet_repository.create_pet(pet)
            if result_create:
                self.counter.add()
                self.view.display_del_or_upd_pet(name, self.counter, 1)
        else:
            print("Пожалуйста, заполните все поля.")

    def show_pet_class(self):
        name = input("Введите имя животного для определения класса: ")
        pet_class = self.pet_repository.get_pet_class(name)
        self.view.display_pet_class(name, pet_class)

    def show_pet_commands(self):
        name = input("Введите имя животного для просмотра команд: ")
        commands = self.pet_repository.get_pet_commands(name)
        self.view.display_pet_commands(name, commands)

    def train_pet_commands(self):
        name = input("Введите имя животного, чтобы обучить новым командам: ")
        commands = self.pet_repository.get_pet_commands(name)
        if commands:
            command = input("Введите новую команду: ")
            updated_commands = commands[0] if commands[0] else []
            updated_commands.append(command)
            self.pet_repository.update_pet_commands(name, updated_commands)
            self.view.display_upd_com(command, name)
        else:
            print("Животное не найдено.")

    def remove_pet(self):
        name = input("Введите имя животного, которое хотите удалить: ")
        self.pet_repository.delete_pet(name)
        self.counter.rem()
        self.view.display_del_or_upd_pet(name, self.counter, 2)