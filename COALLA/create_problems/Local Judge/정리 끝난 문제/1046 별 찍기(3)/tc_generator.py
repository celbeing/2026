# 문제
# 규칙을 파악하여 N에 따라 별을 찍는다.

# 입력
# 1 <= N <= 20

# 출력
# 가로, 세로가 N인 채워지지 않은 사각형을 별로 찍어 출력한다.
# 예1) N = 3
# ***
# * *
# ***
# 예2) N = 5
# *****
# *   *
# *   *
# *   *
# *****

# 기타
# 1~20까지의 모든 N을 순서를 섞어 TC로 구성한다.

from pathlib import Path
from random import Random


CASES = list(range(1, 21))
Random(1046).shuffle(CASES)


def make_hollow_square(n: int) -> str:
    if n <= 2:
        return "\n".join("*" * n for _ in range(n))

    middle = "*" + " " * (n - 2) + "*"
    return "\n".join(["*" * n, *[middle for _ in range(n - 2)], "*" * n])


def main() -> None:
    path = Path(__file__).resolve().parent

    for tc, n in enumerate(CASES, 1):
        answer = make_hollow_square(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8", newline="\n")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
