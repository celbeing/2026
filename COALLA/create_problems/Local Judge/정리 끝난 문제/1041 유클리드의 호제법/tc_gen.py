from pathlib import Path


# 문제 설명
# 두 자연수 A, B를 두고 유클리드 호제법을 실행해 수의 변화를 계속 출력한다.

# 입력
# 1: {A} {B}\n

# 출력
# 1: {A} {B}
# 2: {B} {A%B}
# 3: ...
# k: {gcd(A, B)} {0}

# 조건
# 1 <= A, B <= 1,000,000
CASES = [
    (1, 1),
    (2, 1),
    (1, 2),
    (12, 8),
    (18, 24),
    (21, 13),
    (48, 18),
    (99, 78),
    (100, 10),
    (270, 192),
    (1024, 64),
    (12345, 54321),
    (99991, 97),
    (100000, 99999),
    (123456, 789012),
    (999983, 2),
    (1000000, 1),
    (1000000, 999999),
    (832040, 514229),
    (999936, 999744),
]


def euclid_steps(a: int, b: int) -> str:
    lines = []
    while True:
        lines.append(f"{a} {b}")
        if b == 0:
            return "\n".join(lines) + "\n"
        a, b = b, a % b


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 20:
        raise ValueError("테스트케이스는 기본 20개로 구성합니다.")

    check = set()
    for tc, case in enumerate(CASES, 1):
        a, b = case
        if case in check:
            raise ValueError(f"중복 테스트케이스: {case}")
        if not (1 <= a <= 1_000_000 and 1 <= b <= 1_000_000):
            raise ValueError(f"범위 오류: {case}")

        check.add(case)
        (path / f"{tc}.in").write_text(f"{a} {b}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(euclid_steps(a, b), encoding="utf-8")


if __name__ == "__main__":
    main()
