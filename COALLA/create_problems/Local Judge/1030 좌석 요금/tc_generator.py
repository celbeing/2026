from random import randint

path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1030 좌석 요금\\"

for tc in range(1, 21):
    fst = randint(100, 200) * 10000
    bus = randint(50, 90) * 10000
    eco = randint(20, 30) * 10000

    mops = randint(15, 50) * 1000

    bag = randint(10, 50)
    limit = randint(5, 8) * 5
    k = randint(2, 5)
    cost = randint(5, 20) * 1000

    extra = 0 if bag <= limit else ((bag - limit + k - 1) // k) * cost

    first = fst + mops + extra
    busni = bus + mops + extra
    econo = eco + mops + extra

    # 최소한 이코노미는 탈 수 있게 생성
    low = econo
    money = randint(low // 1000, 2500) * 1000

    with open(path + f"{tc}.in", "w", encoding="utf-8") as file:
        file.write(f"{money} {bag}\n")
        file.write(f"{fst} {bus} {eco} {mops}\n")
        file.write(f"{limit} {k} {cost}\n")

    if money >= first:
        ans = "First"
    elif money >= busni:
        ans = "Business"
    else:
        ans = "Economy"

    with open(path + f"{tc}.out", "w", encoding="utf-8") as file:
        file.write(f"{ans}\n")