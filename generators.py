from faker import Faker

fake = Faker()


def generate_login():
    return fake.user_name()


def generate_password():
    return fake.password(5)


def generate_name():
    return fake.first_name()

