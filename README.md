# Итоговая контрольная работа 
### Информация о проекте
Необходимо организовать систему учета для питомника в котором живут
домашние и вьючные животные.  

### Задание  
1. Используя команду cat в терминале операционной системы Linux, создать
   два файла: Домашние животные (заполнив файл собаками, кошками,
   хомяками) и Вьючные животными (заполнив файл Лошадьми, верблюдами и
   ослы), а затем объединить их. Просмотреть содержимое созданного файла.
   Переименовать файл, дав ему новое имя (Друзья человека).

![Screenshot](/source/Screenshot_1.png)  

2. Создать директорию, переместить файл туда.  

![Screenshot](/source/Screenshot_2.png)  

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
   из этого репозитория.  

![Screenshot](/source/Screenshot_3.png)  
![Screenshot](/source/Screenshot_5.png)  
![Screenshot](/source/Screenshot_6.png)  
![Screenshot](/source/Screenshot_7.png)  

4. Установить и удалить deb-пакет с помощью dpkg.  

![Screenshot](/source/Screenshot_8.png)
![Screenshot](/source/Screenshot_9.png)
![Screenshot](/source/Screenshot_10.png)

5. Выложить историю команд в терминале ubuntu. 

```bash
cat >> Pets
cat >> PackAnimals
cat Pets PackAnimals > HumanFriends
cat HumanFriends
```
```bash
mkdir GBdir
cd GBdir/
mv HumanFriends GBdir/
ls 
```
```bash
sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server
```
```bash
sudo wget https://download.docker.com/linux/ubuntu/dists/jammy/pool/stable/amd64/docker-ce-cli_20.10.13~3-0~ubuntu-jammy_amd64.deb
sudo dpkg -i docker-ce-cli_20.10.13~3-0~ubuntu-jammy_amd64.deb
sudo dpkg -P docker-ce docker-ce-cli
```

6. Нарисовать диаграмму, в которой есть родительский класс, домашние
   животные и вьючные животные, в составы которых в случае домашних
   животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
   войдут: Лошади, верблюды и ослы.

![Screenshot](/source/Screenshot_11.png)

7. В подключенном MySQL репозитории создать базу данных “Друзья
   человека”

```sql
CREATE DATABASE Human_friends;
```

8. Создать таблицы с иерархией из диаграммы в БД

```sql
CREATE TABLE animal_classes
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Class_name VARCHAR(20)
);

INSERT INTO animal_classes (Class_name)
VALUES ('Packed_animals'),
       ('Home_animals');

CREATE TABLE home_animals
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Genus_name VARCHAR (20),
    Class_id INT,
    FOREIGN KEY (Class_id) REFERENCES animal_classes (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO home_animals (Genus_name, Class_id)
VALUES ('Cat', 2),
       ('Dog', 2),
       ('Hamster', 2);

CREATE TABLE cats
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE dogs
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE hamsters
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE packed_animals
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Genus_name VARCHAR (20),
    Class_id INT,
    FOREIGN KEY (Class_id) REFERENCES animal_classes (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO packed_animals (Genus_name, Class_id)
VALUES ('Horses', 1),
       ('Donkeys', 1),
       ('Camels', 1);

CREATE TABLE horses
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE donkeys
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE camels
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    Genus_id int,
    Foreign KEY (Genus_id) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
```
Результат:  

![Screenshot](/source/Screenshot_12.png)

9. Заполнить низкоуровневые таблицы именами(животных), командами
   которые они выполняют и датами рождения

```sql
INSERT INTO cats (Name, Birthday, Commands, Genus_id)
VALUES ('Пушок', '2015-01-01', 'кис-кис', 1),
       ('Рыжик', '2017-01-01', "ко мне рыжик!", 1),  
       ('Черныш', '2018-01-01', "брысь", 1);

INSERT INTO dogs (Name, Birthday, Commands, Genus_id)
VALUES ('Бим', '2022-07-05', 'ко мне, лежать, лапу, тихо', 2),
       ('Рекс', '2023-01-10', "сидеть, лежать, лапу", 2),
       ('Джек', '2022-08-23', "сидеть, ползи, лапу, след, фас", 2),
       ('Лола', '2020-07-15', "сидеть, лежать, фу, место", 2);

INSERT INTO hamsters (Name, Birthday, Commands, Genus_id)
VALUES ('Буся', '2020-10-12', '', 3),
       ('Чарли', '2021-03-12', "кувырок", 3),
       ('Тоша', '2022-07-11', "прыжок", 3),
       ('Кнопка', '2022-05-10', NULL, 3);

INSERT INTO horses (Name, Birthday, Commands, Genus_id)
VALUES ('Мустанг', '2020-09-22', 'бегом, шагом, рысью', 1),
       ('Рокки', '2017-05-25', "бегом, шагом, хоп", 1),
       ('Леди', '2016-01-21', "бегом, хоп, шагом, грр", 1),
       ('Торнадо', '2020-08-14', "бегом, голопом, хоп", 1);

INSERT INTO donkeys (Name, Birthday, Commands, Genus_id)
VALUES ('Пердун', '2019-01-15', "иди, стой", 2),
       ('Тарзан', '2020-03-12', "брр, пошел", 2),
       ('Пончик', '2021-04-21', "", 2),
       ('Марго', '2022-02-18', "поднимайся, бегом", 2);

INSERT INTO camels (Name, Birthday, Commands, Genus_id)
VALUES ('Хамид', '2022-04-19', "айла, хаджала", 3),
       ('Али', '2019-03-17', "обрирак", 3),
       ('Саид', '2015-10-10', "чак, тарг", 3),
       ('Фатима', '2022-02-10', "швай", 3);
```
Результат:

![Screenshot](/source/Screenshot_13.png)

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
    питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

```sql
SET SQL_SAFE_UPDATES = 0;
DELETE FROM camels;

SELECT Name, Birthday, Commands FROM horses
UNION SELECT  Name, Birthday, Commands FROM donkeys;
```
Результат:

![Screenshot](/source/Screenshot_14.png)
    
11. Создать новую таблицу “молодые животные” в которую попадут все
    животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
    до месяца подсчитать возраст животных в новой таблице

```sql
CREATE TEMPORARY TABLE animals AS 
SELECT *, 'Лошади' as genus FROM horses
UNION SELECT *, 'Ослы' AS genus FROM donkeys
UNION SELECT *, 'Собаки' AS genus FROM dogs
UNION SELECT *, 'Кошки' AS genus FROM cats
UNION SELECT *, 'Хомяки' AS genus FROM hamsters;

CREATE TABLE young_animal AS
SELECT Name, Birthday, Commands, genus, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_month
FROM animals WHERE Birthday BETWEEN ADDDATE(curdate(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
 
SELECT * FROM young_animal;
``` 
Результат:

![Screenshot](/source/Screenshot_15.png)

12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
    прошлую принадлежность к старым таблицам.

```sql
SELECT h.Name, h.Birthday, h.Commands, pack.Genus_name, young.Age_in_month 
FROM horses h
LEFT JOIN young_animal young ON young.Name = h.Name
LEFT JOIN packed_animals pack ON pack.Id = h.Genus_id
UNION 
SELECT d.Name, d.Birthday, d.Commands, pack.Genus_name, young.Age_in_month 
FROM donkeys d 
LEFT JOIN young_animal young ON young.Name = d.Name
LEFT JOIN packed_animals pack ON pack.Id = d.Genus_id
UNION
SELECT c.Name, c.Birthday, c.Commands, home.Genus_name, young.Age_in_month 
FROM cats c
LEFT JOIN young_animal young ON young.Name = c.Name
LEFT JOIN home_animals home ON home.Id = c.Genus_id
UNION
SELECT d.Name, d.Birthday, d.Commands, home.Genus_name, young.Age_in_month 
FROM dogs d
LEFT JOIN young_animal young ON young.Name = d.Name
LEFT JOIN home_animals home ON home.Id = d.Genus_id
UNION
SELECT hm.Name, hm.Birthday, hm.Commands, home.Genus_name, young.Age_in_month 
FROM hamsters hm
LEFT JOIN young_animal young ON young.Name = hm.Name
LEFT JOIN home_animals home ON home.Id = hm.Genus_id;
```
Результат:

![Screenshot](/source/Screenshot_16.png)

13. Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

Реализовано с помощью SOLID, MVC и взаимодействия с базой данных PostgreSQL "human_friends2"::

SOLID принципы:
Single Responsibility Principle (Принцип единственной ответственности):

Pet класс отвечает за представление данных о животном и его командах.
Counter класс управляет счетчиком и контролирует доступ к его изменению.
PetCRUDInterface и PetCommandsInterface представляют интерфейсы для работы с данными животных и их командами.
PetRepository реализует эти интерфейсы и работает с базой данных.
В целом, классы имеют четкие обязанности, соответствующие их названиям, что соответствует принципу единственной ответственности.

Open/Closed Principle (Принцип открытости/закрытости):

Код в основном замкнут на изменения, которые не требуют изменения исходного кода классов, за исключением, возможно, доработки SQL-запросов в PetRepository.
Liskov Substitution Principle (Принцип подстановки Барбары Лисков):

Наследование не используется в коде прямо, однако интерфейсы (PetCRUDInterface и PetCommandsInterface) гарантируют, что все реализующие их классы будут поддерживать одинаковый набор методов.
Interface Segregation Principle (Принцип разделения интерфейса):

Интерфейсы довольно узкие и конкретные (PetCRUDInterface и PetCommandsInterface), что соответствует этому принципу.
Dependency Inversion Principle (Принцип инверсии зависимостей):

Класс PetRepository зависит от абстракций (PetCRUDInterface и PetCommandsInterface), а не от конкретной реализации. Это позволяет легко заменять или расширять поведение без изменения самого репозитория.

MVC (Model-View-Controller):
Model (Модель): Представлены классы Pet, Counter, PetCRUDInterface, PetCommandsInterface, PetRepository и DatabaseConnection. Они отвечают за работу с данными, хранение, обработку и взаимодействие с базой данных.

View (Представление): Класс View отвечает за отображение данных пользователю. Он содержит методы для вывода информации о животных, командах и главного меню программы.

Controller (Контроллер): Класс Controller связывает модель и представление. Он инициализирует соединение с базой данных, создает объекты для работы с данными (PetRepository) и управляет основным меню программы.

![Screenshot](/source/Screenshot_17.png)
![Screenshot](/source/Screenshot_18.png)

14. Написать программу, имитирующую работу реестра домашних животных.
    В программе должен быть реализован следующий функционал:

    14.1 Завести новое животное  
    14.2 определять животное в правильный класс  
    14.3 увидеть список команд, которое выполняет животное  
    14.4 обучить животное новым командам  
    14.5 Реализовать навигацию по меню  

15. Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
    значение внутренней̆ int переменной на 1 при нажатие “Завести новое
    животное” Сделайте так, чтобы с объектом такого типа можно было работать в
    блоке try-with-resources. Нужно бросить исключение, если работа с объектом
    типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
    считать в ресурсе try, если при заведения животного заполнены все поля.
    
![Screenshot](/source/Screenshot_19.png)