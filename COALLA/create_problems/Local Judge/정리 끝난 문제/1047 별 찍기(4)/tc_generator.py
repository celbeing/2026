# 문제
# 규칙에 따라 N에 맞는 별을 찍는다.

# 입력
# 1 <= N <= 20

# 출력
# 좌상단에 직각인 변이 오는 직각이등변삼각형 형태로 별을 찍는다.
# 예1) N = 3
# ***
# **
# *
# 예2) N = 7
# *******
# ******
# *****
# ****
# ***
# **
# *

# 기타
# 1~20의 모든 N을 순서를 섞어 TC로 구성한다.

from pathlib import Path
from random import Random


CASES = list(range(1, 21))
Random(1047).shuffle(CASES)


def make_left_triangle(n: int) -> str:
    return "\n".join("*" * length for length in range(n, 0, -1))


def main() -> None:
    path = Path(__file__).resolve().parent

    for tc, n in enumerate(CASES, 1):
        answer = make_left_triangle(n)
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8", newline="\n")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
