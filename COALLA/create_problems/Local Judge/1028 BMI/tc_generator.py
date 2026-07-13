from random import random, randint, shuffle
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1028 BMI\\"

def BMI(h:float, w:float) -> str:
    bmi = w/((h/100)**2)
    if bmi >= 35: return "고도비만"
    elif bmi >= 30: return "비만"
    elif bmi >= 25: return "과체중"
    elif bmi >= 18.5: return "표준체중"
    else: return "저체중"

num = []
for i in range(4):
    p = randint(150, 184)
    if p in check: p = randint(150, 184)
    check.add(p)
    num.append(p)
for i in range(4):
    p = randint(185, 249)
    if p in check: p = randint(185, 249)
    check.add(p)
    num.append(p)
for i in range(4):
    p = randint(250, 299)
    if p in check: p = randint(250, 299)
    check.add(p)
    num.append(p)
for i in range(4):
    p = randint(300, 349)
    if p in check: p = randint(300, 349)
    check.add(p)
    num.append(p)
for i in range(4):
    p = randint(350, 400)
    if p in check: p = randint(350, 400)
    check.add(p)
    num.append(p)
shuffle(num)
for tc in range(1, 21):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    bmi = num.pop()
    h = randint(1400, 2000)/10
    t = int(bmi*((h/100)**2))/10

    w = file.writelines(f'{h} {t}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{BMI(h, t)}\n')