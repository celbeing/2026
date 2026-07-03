import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1016 python\\"

for tc in range(1, 2):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')


    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines('''#####  #   # ##### #    #  ####  #    # 
#    #  # #    #   #    # #    # ##   # 
#    #   #     #   ###### #    # # #  # 
#####    #     #   #    # #    # #  # # 
#        #     #   #    # #    # #   ## 
#        #     #   #    #  ####  #    # 
''')