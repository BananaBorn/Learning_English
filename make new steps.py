import csv

# {'eng' : '', 'rus' : '', 'accent' : '', 'counter' : 0},

step_1 = [
    {'eng' : 'i', 'rus' : 'я', 'accent' : 'ай', 'counter' : 0},
    {'eng' : 'he', 'rus' : "он", 'accent' : 'хи', 'counter' : 0},
    {'eng' : 'she', 'rus' : "она", 'accent' : 'щи', 'counter' : 0},
    {'eng' : 'you', 'rus' : "ты", 'accent' : 'ю', 'counter' : 0},
    {'eng' : 'they', 'rus' : "они", 'accent' : 'зей', 'counter' : 0},
    {'eng' : 'we', 'rus' : "мы", 'accent' : 'ви', 'counter' : 0},
    {'eng' : 'me', 'rus' : "мне", 'accent' : 'ми', 'counter' : 0},
    {'eng' : 'them', 'rus' : "им", 'accent' : 'зем', 'counter' : 0},
    {'eng' : 'is', 'rus' : "есть", 'accent' : 'из', 'counter' : 0},
    {'eng' : 'are', 'rus' : "есть", 'accent' : 'а:', 'counter' : 0},
    {'eng' : 'it', 'rus' : "это", 'accent' : 'ит', 'counter' : 0},
    {'eng' : 'him', 'rus' : "ему", 'accent' : 'хим', 'counter' : 0},
    {'eng' : 'my', 'rus' : "моё", 'accent' : 'май', 'counter' : 0},
    {'eng' : 'your', 'rus' : "твоё", 'accent' : 'йор', 'counter' : 0},
    {'eng' : 'ours', 'rus' : "наше", 'accent' : 'ауерс', 'counter' : 0},
    {'eng' : 'his', 'rus' : "его", 'accent' : 'хиз', 'counter' : 0},
    {'eng' : 'her', 'rus' : "её", 'accent' : 'хё', 'counter' : 0},
    {'eng' : 'us', 'rus' : "нам", 'accent' : 'ас', 'counter' : 0}
    ]

with open('1_step.csv', 'w', newline ='') as file:
    head = ['eng', 'rus', 'accent', 'counter']
    writer = csv.DictWriter(file, fieldnames=head, delimiter=';')
    writer.writeheader()
    writer.writerows(step_1)
