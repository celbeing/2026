import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1017 애국가\\"

for tc in range(1, 2):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')


    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines('''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
''')