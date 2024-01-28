from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        # self.__value = None
        # self.__value = value
        self.value = value
        # self.value = self.check_phone(value)
    
    @property
    def check_phone(self):
        return self.value

    # Перевірка на коректність веденого номера телефону setter для value класу Phone.
    @check_phone.setter
    def check_phone(self, new_value):  # Реалізовано валідацію номера телефону (має бути 10 цифр).
        if len(new_value) == 10 and new_value.isdecimal():
        # if len(value) != 10 and  not value.isdecimal():
            # return value
            self.value = new_value
            # raise ValueError("Phone must contain 10 digits only!")
        else:
            raise ValueError("Phone must contain 10 digits only!")
        # self._value = value


class Birthday(Field):
    def __init__(self, value):
        # self.__value = None
        self.value = value
        # self._value = value
    
    @property
    def set_birthday(self):
        # return self._value
        return self.value
        # return self.__value

    # Перевірка на коректність веденого дня народження setter для value класу Birthday.
    @set_birthday.setter
    def set_birthday(self, new_value):
        if new_value:
            self.value = datetime.strptime(new_value, "%d/%m/%Y")


class Record:
    '''Record: Додавання телефонів. Видалення телефонів. Редагування телефонів. Пошук телефону.
    Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday'''
    def __init__(self, name, birthday = None):
        self.name = Name(name)  # Реалізовано зберігання об'єкта Name в окремому атрибуті.
        self.phones = []  # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
        self.birthday = Birthday(birthday)  # опціональний аргумент класу Birthday

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    # Реалізовано методи для:
    def add_phone(self, phone: str):  # додавання - add_phone
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):  # видалення - remove_phone
        for i in range(len(self.phones)):
            if str(self.phones[i]) == phone:
                return self.phones.pop(i)

    def edit_phone(self, phone: str, new_phone: str):  # редагування - edit_phone
        is_exists = self.find_phone(phone)
        if is_exists:
            get_index = self.phones.index(is_exists)
            self.phones[get_index] = Phone(new_phone)
        else:
            raise ValueError(f'Phone {phone} not found!')

    def find_phone(self, phone: str):  # пошуку об'єктів Phone - find_phone
        for item in filter(lambda i: i.__str__() == phone, self.phones):
            return item
    
    def days_to_birthday(self):  # повертає кількість днів до наступного дня народження.
        # pass
        if self.birthday:
            return self.birthday - datetime.now()
        return "Empty Birthday field!"


class AddressBook(UserDict):
    '''AddressBook: Додавання записів. Пошук записів за іменем. Видалення записів за іменем.'''
    """Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value."""
    # Реалізовано метод add_record, який додає запис до self.data.
    def add_record(self, record: Record):  # Додавання запису.
        self.data[record.name.value] = record

    def find(self, name):  # Реалізовано метод find, який знаходить запис за ім'ям.
        return self.data.get(name)

    def delete(self, name):  # Реалізовано метод delete, який видаляє запис за ім'ям.
        if name in self.data:
            return f'Record with {self.data.pop(name)} was removed!'
    
    def iterator(self):  # повертає генератор за записами AddressBook (за одну ітерацію повертає N записів).
        pass


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
# john_record = Record("John")
john_record = Record("John", "27/02/2024")
john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
john_record.add_phone("555555")
john_record.add_phone("555qq5555")

print(john_record.birthday)
print(john_record.days_to_birthday())

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")


# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)



# # Using datetime.strptime()
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# dt
