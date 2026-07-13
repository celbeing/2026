from pathlib import Path


DAYS = ["월", "화", "수", "목", "금", "토", "일"]

# 입력: 첫 번째 줄에 오늘이 무슨요일인지 한 글자로 주어진다. (예: 목)
#      두 번째 줄에 앞으로 며칠 후의 요일을 알아볼 것인지 1 이상 1000 이하의 n이 주어진다.
# 출력: 오늘로부터 n일 후가 무슨 요일인지 한 글자로 출력한다.
CASES = [
    ("월", 1),
    ("화", 2),
    ("수", 3),
    ("목", 4),
    ("금", 5),
    ("토", 6),
    ("일", 7),
    ("월", 8),
    ("화", 13),
    ("수", 14),
    ("목", 30),
    ("금", 31),
    ("토", 365),
    ("일", 366),
    ("월", 999),
    ("화", 1000),
    ("수", 997),
    ("목", 998),
    ("금", 500),
    ("토", 123),
]


def weekday_after(today: str, n: int) -> str:
    return DAYS[(DAYS.index(today) + n) % len(DAYS)]


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) > 20:
        raise ValueError("테스트케이스는 20개를 넘을 수 없습니다.")

    check = set()
    for tc, (today, n) in enumerate(CASES, 1):
        if (today, n) in check:
            raise ValueError(f"중복 테스트케이스: {today} {n}")
        if today not in DAYS:
            raise ValueError(f"잘못된 요일: {today}")
        if not 1 <= n <= 1000:
            raise ValueError(f"n 범위 오류: {n}")

        check.add((today, n))
        answer = weekday_after(today, n)

        (path / f"{tc}.in").write_text(f"{today}\n{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(f"{answer}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
