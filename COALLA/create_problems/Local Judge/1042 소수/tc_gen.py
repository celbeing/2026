from pathlib import Path


# 문제 설명
# 주어지는 자연수 N이 소수인지 판별한다.

# 입력
# 1: {N}\n

# 출력
# 1: {'Yes' if N is prime else 'No'}

# 조건
# 1 <= N <= 1,000,000
# 이 문제의 tc는 N이 1인 것 1개, 소수인 것 10개, 합성수인 것 10개로 한다.
CASES = [
    1,
    2,
    3,
    5,
    7,
    11,
    97,
    997,
    7919,
    104729,
    999983,
    4,
    6,
    9,
    25,
    49,
    121,
    1001,
    99999,
    999981,
    1000000,
]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 21:
        raise ValueError("이 문제는 주석 조건에 따라 테스트케이스 21개로 구성합니다.")

    check = set()
    ones = primes = composites = 0
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 1_000_000:
            raise ValueError(f"범위 오류: {n}")

        prime = is_prime(n)
        ones += n == 1
        primes += prime
        composites += n > 1 and not prime

        check.add(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{'Yes' if prime else 'No'}\n", encoding="utf-8")

    if (ones, primes, composites) != (1, 10, 10):
        raise ValueError(f"tc 분포 오류: 1={ones}, 소수={primes}, 합성수={composites}")


if __name__ == "__main__":
    main()
