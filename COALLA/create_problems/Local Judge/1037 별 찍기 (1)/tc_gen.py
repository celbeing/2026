from pathlib import Path


# 문제 설명
# 별(*)을 규칙에 따라 찍는다.
# 만약 N = 3이라면
# *
# **
# ***
# 으로 별을 찍는다.
# 만약 N = 5라면
# *
# **
# ***
# ****
# *****
# 으로 별을 찍는다.

# 입력
# 1: {N}\n

# 출력
# for i in range(1, N+1):
#     print('*'*i)

# 조건
# 1 <= N <= 100
CASES = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    15,
    20,
    25,
    30,
    50,
    75,
    99,
    100,
]


def stars(n: int) -> str:
    return "\n".join("*" * i for i in range(1, n + 1)) + "\n"


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 100:
            raise ValueError(f"범위 오류: {n}")

        check.add(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(stars(n), encoding="utf-8")


if __name__ == "__main__":
    main()
