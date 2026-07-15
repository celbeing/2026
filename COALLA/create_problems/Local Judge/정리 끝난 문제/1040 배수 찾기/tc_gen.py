from pathlib import Path


# 문제 설명
# 주어진 범위 [A, B] 내에서 K의 배수가 몇 개인지 출력한다.

# 입력
# 1: {A} {B} {K}\n

# 출력
# 1: {[A, B] 범위 내 K의 배수의 갯수}\n

# 조건
# 1 <= A < B < 1,000,000
# 2 <= K <= 100
CASES = [
    (1, 2, 2),
    (1, 10, 2),
    (1, 10, 3),
    (2, 10, 5),
    (3, 20, 4),
    (10, 99, 10),
    (11, 99, 10),
    (50, 100, 7),
    (99, 101, 100),
    (100, 1000, 25),
    (123, 4567, 13),
    (999, 9999, 9),
    (1000, 2000, 37),
    (12345, 98765, 99),
    (54321, 654321, 17),
    (99900, 99999, 100),
    (111111, 222222, 11),
    (400000, 800000, 64),
    (999998, 999999, 2),
    (1, 999999, 100),
]


def multiple_count(a: int, b: int, k: int) -> int:
    return b // k - (a - 1) // k


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, case in enumerate(CASES, 1):
        a, b, k = case
        if case in check:
            raise ValueError(f"중복 테스트케이스: {case}")
        if not (1 <= a < b < 1_000_000 and 2 <= k <= 100):
            raise ValueError(f"범위 오류: {case}")

        check.add(case)
        (path / f"{tc}.in").write_text(f"{a} {b} {k}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{multiple_count(a, b, k)}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
