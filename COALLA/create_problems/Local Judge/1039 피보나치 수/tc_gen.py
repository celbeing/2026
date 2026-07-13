from pathlib import Path


# 문제 설명
# 0번 항을 1, 1번 항을 1로 하는 피보나치 수열의 N번째 항을 찾는다.

# 입력
# 1: {N}\n

# 출력
# 1: {피보나치 수열의 N번째 항}\n

# 조건
# 1 <= N <= 1,000
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
    20,
    30,
    40,
    50,
    75,
    100,
    250,
    500,
    750,
    1000,
]


def fibonacci(n: int) -> int:
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 1000:
            raise ValueError(f"범위 오류: {n}")

        check.add(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{fibonacci(n)}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
