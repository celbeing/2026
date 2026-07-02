import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1008 그대로 출력하기\\"

text = list("bus class coffee computer lightbulb pen dust mountain check python torch cat board summer cosmos block hand bottle".split())

for tc, i in enumerate(text):
    file = open(path + f'{tc+1}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{i}\n')

    file = open(path + f'{tc+1}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{i}\n')