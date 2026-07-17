# 문제
# 별 찍기 (4)를 좌우 반전한 문제

# 입력
# 1 <= N <= 20

# 출력
# 예1) N = 4
# ****
#  ***
#   **
#    *
# 예2) N = 6
# ******
#  *****
#   ****
#    ***
#     **
#      *

# 기타
# 1~20의 N을 순서를 섞어 모두 TC로 구성한다.

from pathlib import Path
from random import Random


CASES = list(range(1, 21))
Random(1048).shuffle(CASES)


def make_right_triangle(n: int) -> str:
    return "\n".join(" " * indent + "*" * (n - indent) for indent in range(n))


def main() -> None:
    path = Path(__file__).resolve().parent

    for tc, n in enumerate(CASES, 1):
        answer = make_right_triangle(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8", newline="\n")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
