from abc import ABC, abstractmethod
from typing import List, Tuple
from psycopg2 import Error
from pet import Pet
import psycopg2

class PetCRUDInterface(ABC):

    @abstractmethod
    # def create_pet(self, pet: Pet) -> None:
    def create_pet(self, pet: Pet) -> int:
        pass

    @abstractmethod
    def get_pet_class(self, name: str) -> str:
        pass

    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass

    @abstractmethod
    def get_all_pets(self) -> List[Tuple[str, str]]:
        pass

    @abstractmethod
    def get_pets_count(self) -> int:
        pass


class PetCommandsInterface(ABC):
    @abstractmethod
    def update_pet_commands(self, name: str, commands: List[str]) -> None:
        pass

    @abstractmethod
    def get_pet_commands(self, name: str) -> List[str]:
        pass


class PetRepository(PetCRUDInterface, PetCommandsInterface):
    def __init__(self, connection):
        self.connection = connection

    def create_pet(self, pet: Pet) -> int:
        try:
            with self.connection.cursor() as cursor:
                result_create = None
                cursor.execute("SELECT id FROM home_animals WHERE name = %s",
                               [pet.pet_class])
                result = cursor.fetchone()
                if result:
                    cursor.execute(
                        "INSERT INTO pets (name, animal_id, commands) VALUES (%s, %s, %s)",
                        (pet.name, result[0], pet.get_commands())
                    )
                    self.connection.commit()
                    result_create = 1
                else:
                    print(f"Не найден класс с именем '{pet.pet_class}' в таблице home_animals.")
                return result_create
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def get_pet_class(self, name: str) -> str:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT home_animals.name FROM pets JOIN home_animals"
                    " ON pets.animal_id = home_animals.id WHERE pets.name = %s",
                    (name,))
                result = cursor.fetchone()
                return result[0] if result else None
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def delete_pet(self, name: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM pets WHERE name = %s", (name,))
                self.connection.commit()
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def get_all_pets(self) -> List[Tuple[str, str]]:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT pets.name, home_animals.name, pets.commands FROM pets JOIN home_animals"
                    " ON pets.animal_id = home_animals.id ")
                return cursor.fetchall()
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def update_pet_commands(self, name: str, commands: List[str]) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE pets SET commands = %s WHERE name = %s", (commands, name))
                self.connection.commit()
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def get_pet_commands(self, name: str) -> List[str]:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT commands FROM pets WHERE name = %s", (name,))
                result = cursor.fetchone()
                return result
                # return result if result else []
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None

    def get_pets_count(self) -> int:
        try:
            with self.connection.cursor() as cursor:
                pet_count = None
                cursor.execute("SELECT COUNT(*) AS total_records FROM pets")
                result = cursor.fetchone()
                if result:
                    pet_count = result[0]
                return pet_count
        except (Exception, Error) as error:
            print(f"Ошибка в SQL запросе: {error}")
            self.connection = None