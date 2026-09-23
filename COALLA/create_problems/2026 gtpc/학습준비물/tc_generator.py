#!/usr/bin/env python3
"""학습준비물 테스트 생성기. Python 3.9+, 외부 패키지 불필요.

python generate_supplies.py --out tests/supplies
python generate_supplies.py --seed 42 --random-count 30

N <= 100000, 1 <= W,L <= 40000.
모든 직사각형의 왼쪽 아래 꼭짓점은 동일하다. 합집합 넓이를 출력한다.
각 입력은 독립 파일이며 같은 이름의 .ans와 대응된다.
"""
import argparse
import csv
import random
from pathlib import Path

MAX_N = 100_000
MAX_SIDE = 40_000


def answer(papers):
    """너비별 최대 높이의 suffix maximum 합으로 합집합 넓이를 계산한다."""
    heights = [0] * (MAX_SIDE + 1)
    for w, h in papers:
        if h > heights[w]:
            heights[w] = h
    total = 0
    height = 0
    for w in range(MAX_SIDE, 0, -1):
        height = max(height, heights[w])
        total += height
    return total


def cases(rng, random_count):
    yield 'minimum', [(1, 1)]
    yield 'maximum_square', [(MAX_SIDE, MAX_SIDE)]
    yield 'thin_horizontal', [(MAX_SIDE, 1)]
    yield 'thin_vertical', [(1, MAX_SIDE)]
    yield 'example_staircase', [(2, 5), (4, 3), (3, 4)]
    yield 'cross', [(1, MAX_SIDE), (MAX_SIDE, 1)]
    yield 'equal_width', [(7, h) for h in (3, 12, 1, 12, 9)]
    yield 'equal_height', [(w, 7) for w in (3, 12, 1, 12, 9)]
    yield 'duplicates_small', [(3, 8)] * 12
    yield 'nested_small', [(1, 1), (4, 5), (2, 3), (8, 9), (4, 5)]
    yield 'gaps', [(1, 40000), (123, 25000), (9876, 17000), (40000, 2)]
    yield 'near_maximum', [(39999, 40000), (40000, 39999)]
    stair = [(w, MAX_SIDE + 1 - w) for w in range(1, MAX_SIDE + 1)]
    yield 'staircase_ascending', stair
    yield 'staircase_descending', stair[::-1]
    shuffled = stair.copy()
    rng.shuffle(shuffled)
    yield 'staircase_shuffled', shuffled
    yield 'nested_ascending', [(w, w) for w in range(1, MAX_SIDE + 1)]
    yield 'nested_descending', [(w, w) for w in range(MAX_SIDE, 0, -1)]
    yield 'max_n_minimum', [(1, 1)] * MAX_N
    yield 'max_n_maximum', [(MAX_SIDE, MAX_SIDE)] * MAX_N
    yield 'max_n_cross', [(1, MAX_SIDE), (MAX_SIDE, 1)] * (MAX_N // 2)
    yield 'max_n_equal_width', [(MAX_SIDE, rng.randint(1, MAX_SIDE)) for _ in range(MAX_N)]
    yield 'max_n_equal_height', [(rng.randint(1, MAX_SIDE), MAX_SIDE) for _ in range(MAX_N)]
    # 동일한 폭의 높이를 덮어쓰는 오답: 최댓값이 먼저 나오고 작은 값이 뒤따른다.
    yield 'same_width_max_first', [(MAX_SIDE, MAX_SIDE)] + [(MAX_SIDE, 1)] * (MAX_N - 1)
    yield 'same_width_max_last', [(MAX_SIDE, 1)] * (MAX_N - 1) + [(MAX_SIDE, MAX_SIDE)]
    repeated = (stair * 3)[:MAX_N]
    rng.shuffle(repeated)
    yield 'max_n_staircase', repeated
    random_papers = [(rng.randint(1, MAX_SIDE), rng.randint(1, MAX_SIDE))
                     for _ in range(MAX_N)]
    yield 'max_n_uniform', random_papers
    # 같은 종이 집합의 입력 순서를 바꾼 쌍.
    yield 'max_n_uniform_reversed', random_papers[::-1]
    small = [(rng.randint(1, 1000), rng.randint(1, 1000)) for _ in range(MAX_N - 1)]
    yield 'covering_paper_first', [(MAX_SIDE, MAX_SIDE)] + small
    yield 'covering_paper_last', small + [(MAX_SIDE, MAX_SIDE)]
    for i in range(random_count):
        if i % 3 == 0:
            n, bound = rng.randint(1, 30), 20
        elif i % 3 == 1:
            n, bound = rng.randint(100, 2000), MAX_SIDE
        else:
            n, bound = rng.randint(MAX_N // 2, MAX_N), MAX_SIDE
        yield f'random_{i + 1:03}', [(rng.randint(1, bound), rng.randint(1, bound))
                                     for _ in range(n)]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, default=Path('tests/supplies'))
    parser.add_argument('--seed', type=int, default=20260923)
    parser.add_argument('--random-count', type=int, default=20)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    if args.random_count < 0:
        parser.error('--random-count must be nonnegative')
    if args.out.exists() and any(args.out.iterdir()) and not args.overwrite:
        parser.error(f'{args.out} is not empty; use a new directory or --overwrite')
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, (name, papers) in enumerate(cases(random.Random(args.seed), args.random_count), 1):
        # 생성 데이터의 범위만 확인한다. 별도 정답 코드 대조는 하지 않는다.
        if not 1 <= len(papers) <= MAX_N:
            raise ValueError(f'N out of range: {name}')
        if any(not (1 <= w <= MAX_SIDE and 1 <= h <= MAX_SIDE) for w, h in papers):
            raise ValueError(f'W/L out of range: {name}')
        result = answer(papers)
        stem = f'{i:03}_{name}'
        with (args.out / f'{stem}.in').open('w', encoding='utf-8', newline='\n') as f:
            f.write(f'{len(papers)}\n')
            f.writelines(f'{w} {h}\n' for w, h in papers)
        with (args.out / f'{stem}.ans').open('w', encoding='utf-8', newline='\n') as f:
            f.write(f'{result}\n')
        rows.append([stem, len(papers), max(w for w, _ in papers),
                     max(h for _, h in papers), result, args.seed])
        print(f'{stem}: N={len(papers)}, answer={result}')
    with (args.out / 'manifest.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['case', 'N', 'max_W', 'max_L', 'answer', 'seed'])
        writer.writerows(rows)
    print(f'Generated {len(rows)} input/answer pairs in {args.out.resolve()}')


if __name__ == '__main__':
    main()
