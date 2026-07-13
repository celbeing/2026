from decimal import Decimal, ROUND_FLOOR
from pathlib import Path


# 문제 설명
# 파이썬의 반올림 함수 round()는 사사오입이 아닌 오사오입 방식으로 반올림을 하기 때문에
# 정확한 반올림을 할 수 없다.
# 반올림 하고자 하는 자리 아래에서 +0.5를 한 다음 버림을 하면 반올림을 정확하게 할 수 있다.

# 입력
# 1: {N}\n

# 출력
# 1: {N을 소수점 아래 두 번째 자리까지 반올림하여 나타낸 수}\n

# 조건
# -100,000 <= N <= 100,000
# N은 소수점 아래 6자리까지 표현됨
CASES = [
    "-100000",
    "-99999.995000",
    "-12345.555555",
    "-100.005000",
    "-12.345600",
    "-2.675000",
    "-1.235000",
    "-0.005000",
    "-0.004900",
    "0",
    "0.004900",
    "0.005000",
    "1.234000",
    "1.235000",
    "2.675000",
    "12.345600",
    "99.999900",
    "12345.555555",
    "99999.995000",
    "100000",
]


def round_to_second_place(raw: str) -> str:
    value = Decimal(raw)
    scaled = (value * Decimal(100) + Decimal("0.5")).to_integral_value(rounding=ROUND_FLOOR)
    rounded = scaled / Decimal(100)
    return f"{rounded:.2f}"


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, raw in enumerate(CASES, 1):
        if raw in check:
            raise ValueError(f"중복 테스트케이스: {raw}")
        value = Decimal(raw)
        if not (Decimal("-100000") <= value <= Decimal("100000")):
            raise ValueError(f"범위 오류: {raw}")
        if -value.as_tuple().exponent > 6:
            raise ValueError(f"소수 자릿수 오류: {raw}")

        check.add(raw)
        (path / f"{tc}.in").write_text(f"{raw}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{round_to_second_place(raw)}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
