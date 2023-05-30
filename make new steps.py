import csv


# Checks just 'y'\'n' input
def yes_or_no():
    while True:
        answer = input("Всё введено правильно? 'y'\'n' >>> ")
        if answer == 'y':
            break
        elif answer == 'n':
            print('Ввод отменён')
            return True
        else:
            print('\nНеправильный ввод!\n')
            continue


# Checks name of new file for originality
def check_step(n):
    try:
        with open(f'{n}_step.csv', 'r') as x:
            return False
    except:
        return True


while True:
    step = input('Введите ЦИФРОЙ номер файла для новых слов >>> ')
    if step.isdigit():
        if check_step(step):
            file_name = f'{step}_step.csv'
            break
        else:
            print('\nТакой файл уже есть!\n')
            continue
    else:
        print('\nНеправильный ввод!\n')

new_words = []
print('\nДля создания нового файла нужно ввести 30 новых слов\n')
while len(new_words) < 30:
    eng_word = input('Слово на английском >>> ')
    rus_word = input('Слово на русском >>> ')
    pronunciation = input('Как произносится >>> ')
    restart = yes_or_no()
    if restart:
        continue
    else:
        new_word = dict(eng=eng_word, rus=rus_word,
                        accent=pronunciation, counter=0)
        new_words.append(new_word)

with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
    header = ['eng', 'rus', 'accent', 'counter']
    writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
    writer.writeheader()
    writer.writerows(new_words)
print("Новый файл успешно создан")
print("Название файла ->", f'"{file_name}"')
