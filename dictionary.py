import itertools

def generate_passwords():
    for length in range(4, 9):
        for password in itertools.product(range(10), repeat=length):
            yield ''.join(map(str, password))

with open('passwords.txt', 'w') as file:
    for password in generate_passwords():
        file.write(password + '\n')

print("Пароли были сохранены в файл passwords.txt")
