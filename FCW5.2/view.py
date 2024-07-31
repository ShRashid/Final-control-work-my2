class View:
    def __init__(self):
        pass

    def display_pets(self, pets):
        # Выводит список всех животных
        print("Список животных:")
        if pets:
            print("Список всех животных:")
            for pet in pets:
                print(f"Имя: {pet[0]}, Класс: {pet[1]}, Список команд: {pet[2]}")
        else:
            print("Нет животных в базе данных.")

    def display_pet_class(self, name, pet_class):
    # Выводит имя и класс животного
        if pet_class:
            print(f"{name} - это {pet_class}.")
        else:
            print("Животное не найдено.")

    def display_pet_commands(self, name, commands):
    # Выводит имя и комманды животного
        if commands:
            if commands[0]:
                print(f"Команды для {name}: {', '.join(commands[0])}")
            else:
                print("Животное не имеет команд.")
        else:
            print("Животное не найдено.")

    def display_main_menu(self):
    # Выводит меню
        print("0. Вывести список животных")
        print("1. Завести новое животное")
        print("2. Посмотреть принадлежность животного к классу")
        print("3. Посмотреть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Удалить животное")
        print("6. Выход")

    def display_del_or_upd_pet(self, name, counter, operation):
        if operation == 1:
            print(f"Новое животное '{name}' заведено. Всего животных: {counter.get_count()}")
        else:
            print(f"Животное '{name}' было удалено. Всего животных '{counter.get_count()}'")

    def display_upd_com(self, command, name):
        print(f"Команда '{command}' добавлена для животного {name}.")