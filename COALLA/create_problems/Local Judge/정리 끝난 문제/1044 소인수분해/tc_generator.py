# 문제
# 자연수 N을 입력으로 받았을 때, N의 소인수를 작은 것부터 모두 출력하기
# 1은 소인수가 아니다.

# 입력
# 2 <= N <= 1,000,000

# 출력
# N의 소인수를 중복 없이 오름차순으로 한 줄에 하나씩 출력

# 기타
# N = 2^15 와 N = 999,983 을 TC에 포함
# TC는 모두 20개

from pathlib import Path


CASES = [
    2,
    3,
    4,
    6,
    12,
    49,
    72,
    97,
    360,
    1024,
    32768,
    59049,
    99991,
    999983,
    1000000,
    999900,
    30030,
    720720,
    524288,
    782946,
]


def prime_factors(n: int) -> list[int]:
    factors = []
    value = n
    divisor = 2

    while divisor * divisor <= value:
        if value % divisor == 0:
            while value % divisor == 0:
                value //= divisor
                factors.append(divisor)
        divisor += 1 if divisor == 2 else 2

    if value > 1:
        factors.append(value)

    return factors


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("TC는 모두 20개여야 합니다.")
    if len(set(CASES)) != len(CASES):
        raise ValueError("중복 테스트케이스가 있습니다.")

    for tc, n in enumerate(CASES, 1):
        if not (1 <= n <= 1_000_000):
            raise ValueError(f"N 범위 오류: {n}")

        answer = "\n".join(map(str, prime_factors(n)))
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8", newline="\n")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
