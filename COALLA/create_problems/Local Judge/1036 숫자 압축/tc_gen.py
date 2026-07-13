from pathlib import Path


# 문제 설명
# 어떤 자연수가 주어졌을 때, 그 수의 각 자리 수를 모두 더한 결과를 출력한다.

# 입력
# 1: {N}\n

# 출력
# 1: {N의 각 자리를 모두 더한 수}\n

# 조건
# 1 <= N <= 1,000,000,000
CASES = [
    1,
    5,
    9,
    10,
    11,
    99,
    100,
    101,
    123,
    909,
    1000,
    9999,
    12345,
    54321,
    100000,
    100001,
    987654321,
    999999999,
    1000000000,
    400000009,
]


def digit_sum(n: int) -> int:
    return sum(map(int, str(n)))


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 1_000_000_000:
            raise ValueError(f"범위 오류: {n}")

        check.add(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{digit_sum(n)}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
