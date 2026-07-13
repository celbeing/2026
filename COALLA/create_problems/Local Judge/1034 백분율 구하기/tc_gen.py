from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


# 문제 설명
# {기준량}과 {비교하는 양}이 주어졌을 때, {기준량}에 대한 {비교하는 양}의 백분율을 소수점 아래 둘째 자리까지 반올림하여 나타내기

# 입력
# 1: {기준량}v{비교하는 양}

# 출력
# 1: {기준량에 대한 비교하는 양의 백분율}

# 조건
# 0 <= {비교하는 양} < {기준량} <= 1,000,000,000
CASES = [
    (1, 0),
    (2, 1),
    (3, 1),
    (3, 2),
    (4, 1),
    (5, 2),
    (7, 3),
    (8, 7),
    (10, 9),
    (11, 1),
    (12, 5),
    (99, 98),
    (100, 33),
    (101, 50),
    (256, 128),
    (999, 1),
    (1000, 999),
    (123456789, 98765432),
    (999999999, 123456789),
    (1000000000, 999999999),
]


def percentage(base: int, amount: int) -> str:
    value = Decimal(amount) * Decimal(100) / Decimal(base)
    rounded = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{rounded:.2f}"


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, case in enumerate(CASES, 1):
        base, amount = case
        if case in check:
            raise ValueError(f"중복 테스트케이스: {case}")
        if not (0 <= amount < base <= 1_000_000_000):
            raise ValueError(f"범위 오류: {case}")

        check.add(case)
        (path / f"{tc}.in").write_text(f"{base} {amount}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{percentage(base, amount)}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
