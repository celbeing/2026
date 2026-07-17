# 문제
# 규칙을 파악해 주어지는 자연수 N에 맞춰 별(*)을 찍는다.

# 입력
# 1 <= N <= 20

# 출력
# 가로, 세로 N인 사각형을 *로 가득 채운다.
# 예1) N = 3
# ***
# ***
# ***
# 예2) N = 4
# ****
# ****
# ****
# ****

# 기타
# 1~20까지의 수를 순서를 섞어 모두 TC로 구성한다.

from pathlib import Path
from random import Random


CASES = list(range(1, 21))
Random(1045).shuffle(CASES)


def make_square(n: int) -> str:
    return "\n".join("*" * n for _ in range(n))


def main() -> None:
    path = Path(__file__).resolve().parent

    for tc, n in enumerate(CASES, 1):
        answer = make_square(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8", newline="\n")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
