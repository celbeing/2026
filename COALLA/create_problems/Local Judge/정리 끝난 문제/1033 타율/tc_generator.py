from pathlib import Path


# 야구 선수의 타율을 계산한다.
# 입력: 선수가 안타를 치지 못한 횟수 A와 안타를 친 횟수 B가 공백으로 구분되어 주어진다.
#      0 <= B <= A < 100
#      새로운 경기에서 선수가 안타를 치지 못한 횟수 C와 새로운 경기에서 안타를 친 횟수 D가 공백으로 구분되어 주어진다.
# 출력: 선수의 타율을 '/'로 구분하여 분수 형태로 출력한다. (예: B+D/A+B+C+D)
CASES = [
    (0, 0, 1, 0),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (2, 1, 3, 2),
    (99, 0, 99, 0),
    (99, 99, 99, 99),
    (50, 25, 40, 20),
    (10, 10, 0, 0),
    (0, 0, 10, 5),
    (20, 0, 0, 0),
    (5, 3, 7, 0),
    (7, 0, 5, 5),
    (13, 7, 29, 11),
    (88, 44, 12, 6),
    (98, 97, 1, 1),
    (99, 1, 2, 2),
    (3, 2, 99, 50),
    (42, 21, 57, 57),
    (6, 6, 6, 0),
    (70, 35, 0, 0),
]


def batting_average_fraction(a: int, b: int, c: int, d: int) -> str:
    return f"{b + d}/{a + b + c + d}"


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) > 20:
        raise ValueError("테스트케이스는 20개를 넘을 수 없습니다.")

    check = set()
    for tc, case in enumerate(CASES, 1):
        a, b, c, d = case
        if case in check:
            raise ValueError(f"중복 테스트케이스: {case}")
        if not (0 <= b <= a < 100):
            raise ValueError(f"A, B 범위 오류: {case}")
        if not (0 <= d <= c < 100):
            raise ValueError(f"C, D 범위 오류: {case}")
        if a + b + c + d == 0:
            raise ValueError(f"분모가 0인 테스트케이스: {case}")

        check.add(case)
        answer = batting_average_fraction(a, b, c, d)

        (path / f"{tc}.in").write_text(f"{a} {b}\n{c} {d}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
