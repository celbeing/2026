from pathlib import Path


# 문제 설명
# 콜라츠 추측에 따라 1이 될 때까지 자연수 N의 변화를 출력한다.

# 입력
# 1: {N}\n

# 출력
# 1: {N}
# 2: {1번 변환된 수}
# ...
# k: {1}

# 조건
# 1 <= N <= 1,000,000,000
# 이 문제의 tc는 N이 1인 것 1개와 변환 횟수가 10 이하인 것 10개, 변환 횟수가 20 이하인 것 10개와 N=27인 것 1개로 한다.
CASES = [
    1,
    2,
    3,
    4,
    5,
    6,
    8,
    10,
    12,
    13,
    16,
    7,
    9,
    11,
    14,
    15,
    17,
    18,
    19,
    22,
    23,
    27,
]


def collatz_sequence(n: int):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence


def main() -> None:
    path = Path(__file__).resolve().parent

    if len(CASES) != 22:
        raise ValueError("이 문제는 주석 조건에 따라 테스트케이스 22개로 구성합니다.")

    check = set()
    count_one = count_short = count_mid = count_27 = 0
    for tc, n in enumerate(CASES, 1):
        if n in check:
            raise ValueError(f"중복 테스트케이스: {n}")
        if not 1 <= n <= 1_000_000_000:
            raise ValueError(f"범위 오류: {n}")

        sequence = collatz_sequence(n)
        steps = len(sequence) - 1
        count_one += n == 1
        count_short += n != 1 and steps <= 10
        count_mid += n != 1 and n != 27 and 10 < steps <= 20
        count_27 += n == 27

        check.add(n)
        answer = "\n".join(map(str, sequence)) + "\n"
        (path / f"{tc}.in").write_text(f"{n}\n", encoding="utf-8")
        (path / f"{tc}.out").write_text(answer, encoding="utf-8")

    if (count_one, count_short, count_mid, count_27) != (1, 10, 10, 1):
        raise ValueError(
            "tc 분포 오류: "
            f"N=1 {count_one}, 10회 이하 {count_short}, 20회 이하 {count_mid}, N=27 {count_27}"
        )


if __name__ == "__main__":
    main()
