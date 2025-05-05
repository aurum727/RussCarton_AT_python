from faker import Faker


class FakeData:
    fake = Faker("en_US")    # в данной строчке указывается язык, на котором будут генерироваться данные (ru_Ru - русский язык)

    def get_full_name(self):
        name = self.fake.first_name()   # получение случайного имени с помощью библиотеки Faker
        surname = self.fake.last_name()
        return f'{name} {surname}'

    def get_email(self):
        email = self.fake.email()    # получение случайного email с помощью библиотеки Faker
        return email

    def get_phone_number(self):
        phone_number = f'+7{self.fake.msisdn()[3:]}'  # получение случайного номера телефона с помощью библиотеки Faker
        return phone_number


if __name__ == "__main__":
    fake = FakeData()
    print(fake.get_full_name(), fake.get_email(), fake.get_phone_number())
