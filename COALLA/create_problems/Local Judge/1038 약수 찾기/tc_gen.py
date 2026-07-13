from pathlib import Path


# 문제 설명
# 주어지는 자연수의 모든 약수를 찾아 하나씩 출력한다.

# 입력
# 1: {N}\n

# 출력
# 1: {N의 가장 작은 약수}
# 2: {그 다음으로 작은 약수}
# ...
# k: {N의 가장 큰 약수}

# 조건
# 1 <= N <= 1,000,000
CASES = [
    1,
    2,
    3,
    4,
    6,
    12,
    16,
    28,
    36,
    49,
    97,
    100,
    121,
    360,
    997,
    1024,
    12345,
    99991,
    999983,
    1000000,
]


def divisors(n: int):
    small = []
    large = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    return small + large[::-1]


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 1_000_000:
            raise ValueError(f"범위 오류: {n}")

        check.add(n)
        answer = "\n".join(map(str, divisors(n))) + "\n"
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(answer, encoding="utf-8")


if __name__ == "__main__":
    main()
