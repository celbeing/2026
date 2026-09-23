#!/usr/bin/env python3
"""설득의 왕 테스트 생성기 (Python 3.9+, 외부 패키지 불필요).

python generate_persuasion.py --version easy --out tests/easy
python generate_persuasion.py --version hard --out tests/hard --seed 20260923
python generate_persuasion.py --self-test

각 파일은 독립 입력이다. 001_name.in / 001_name.ans 및 manifest.csv 생성.
기존 파일 덮어쓰기는 --overwrite가 있을 때만 허용한다.
"""
import argparse
import csv
import random
from pathlib import Path


class DSU:
    def __init__(self, n):
        self.p = [-1] * (n + 1)
        self.count = n

    def find(self, x):
        p = self.p
        root = x
        while p[root] >= 0:
            root = p[root]
        while x != root:
            parent = p[x]
            p[x] = root
            x = parent
        return root

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.p[a] > self.p[b]:
            a, b = b, a
        self.p[a] += self.p[b]
        self.p[b] = a
        self.count -= 1
        return True


def solve(n, k, edges):
    """역순으로 복구하며 그룹 수가 K 미만이 되는 경계를 찾는다."""
    if k == 1:
        return 0
    dsu = DSU(n)
    for i in range(len(edges) - 1, -1, -1):
        dsu.union(*edges[i])
        # 복구 후에는 앞의 i개를 삭제한 상태. K-1이 되면 답은 i+1.
        if dsu.count < k:
            return i + 1
    raise ValueError("Initially disconnected graph")


def brute(n, k, edges):
    """독립 검증: 매 삭제 단계마다 DFS로 연결 요소를 센다."""
    for removed in range(len(edges) + 1):
        adj = [[] for _ in range(n + 1)]
        for a, b in edges[removed:]:
            adj[a].append(b)
            adj[b].append(a)
        seen = [False] * (n + 1)
        groups = 0
        for start in range(1, n + 1):
            if seen[start]:
                continue
            groups += 1
            seen[start] = True
            stack = [start]
            while stack:
                for v in adj[stack.pop()]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
        if groups == k:
            return removed
    raise ValueError("K unreachable")


def validate(n, k, edges, limit):
    m = len(edges)
    if not (1 <= k <= n <= limit and n - 1 <= m <= limit):
        raise ValueError("N/M/K out of range")
    seen = set()
    dsu = DSU(n)
    for a, b in edges:
        if not 1 <= a < b <= n or (a, b) in seen:
            raise ValueError("Invalid or duplicate edge")
        seen.add((a, b))
        dsu.union(a, b)
    if dsu.count != 1:
        raise ValueError("Initially disconnected graph")


def random_graph(n, m, rng):
    """무작위 트리로 연결성을 보장한 후 서로 다른 간선을 추가한다."""
    if not n - 1 <= m <= n * (n - 1) // 2:
        raise ValueError("Impossible edge count")
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    edges = set()
    for i in range(1, n):
        edges.add(tuple(sorted((labels[i], labels[rng.randrange(i)]))))
    if m > n * (n - 1) // 4:
        remaining = [(a, b) for a in range(1, n + 1)
                     for b in range(a + 1, n + 1) if (a, b) not in edges]
        edges.update(rng.sample(remaining, m - len(edges)))
    else:
        while len(edges) < m:
            a, b = rng.sample(range(1, n + 1), 2)
            edges.add((min(a, b), max(a, b)))
    result = sorted(edges)  # 집합 순회 순서에 의존하지 않는다.
    rng.shuffle(result)
    return result


def cases(limit, rng, random_count):
    yield 'singleton', 1, 1, []
    yield 'two_k1', 2, 1, [(1, 2)]
    yield 'two_k2', 2, 2, [(1, 2)]
    sample = [(1, 2), (2, 3), (1, 3), (3, 4)]
    yield 'sample1', 4, 3, sample
    yield 'sample2', 10, 5, [(2, 3), (7, 8), (5, 7), (5, 6),
                            (4, 6), (2, 10), (3, 5), (1, 2),
                            (3, 4), (3, 6), (8, 10), (7, 9)]
    yield 'plateau_k2', 4, 2, [(1, 2), (2, 3), (2, 4), (3, 4)]
    yield 'same_graph_k1', 4, 1, sample
    yield 'same_graph_kn', 4, 4, sample
    for k in (2, limit // 2, limit):
        yield f'path_k{k}', limit, k, [(i, i + 1) for i in range(1, limit)]
    star = [(1, i) for i in range(2, limit + 1)]
    rng.shuffle(star)
    yield 'star_shuffled', limit, limit // 2, star
    cycle = [(i, i + 1) for i in range(1, limit)] + [(1, limit)]
    yield 'cycle_k2', limit, 2, cycle
    yield 'cycle_kn', limit, limit, cycle
    # 다수의 사이클 간선을 먼저 제거해 긴 정체 구간을 만든다.
    dense_n = 2
    while (dense_n + 1) * dense_n // 2 <= limit:
        dense_n += 1
    tree = [(i, i + 1) for i in range(1, dense_n)]
    extra = [(a, b) for a in range(1, dense_n + 1)
             for b in range(a + 2, dense_n + 1)]
    rng.shuffle(extra)
    yield 'dense_cycles_first', dense_n, 2, extra + tree
    # 첫 간선으로 고립된 학생을 만든 뒤 오래 K=2를 유지한다.
    shifted = [(a + 1, b + 1) for a, b in (extra + tree)]
    if len(shifted) + 1 > limit:
        shifted.pop(0)  # 트리는 보존한다.
    yield 'long_plateau_k2', dense_n + 1, 2, [(1, 2)] + shifted
    yield 'max_random_k1', limit // 2, 1, random_graph(limit // 2, limit, rng)
    yield 'max_random_mid', limit // 2, limit // 4, random_graph(limit // 2, limit, rng)
    yield 'max_random_kn', limit // 2, limit // 2, random_graph(limit // 2, limit, rng)
    for i in range(random_count):
        # 작은 무작위 사례는 모든 정답을 DFS로도 검증한다.
        n = rng.randint(2, 30)
        m = rng.randint(n - 1, min(limit, n * (n - 1) // 2))
        yield f'random_{i + 1:03}', n, rng.randint(1, n), random_graph(n, m, rng)


def self_test():
    rng = random.Random(81723)
    checks = 0
    for _ in range(200):
        n = rng.randint(1, 12)
        m = rng.randint(n - 1, n * (n - 1) // 2)
        edges = random_graph(n, m, rng)
        validate(n, 1, edges, 1000)
        for k in range(1, n + 1):
            if solve(n, k, edges) != brute(n, k, edges):
                raise AssertionError((n, k, edges))
            checks += 1
    print(f'Self-test passed: {checks} DFS comparisons')


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--version', choices=['easy', 'hard'], default='hard')
    parser.add_argument('--out', type=Path, default=None)
    parser.add_argument('--seed', type=int, default=20260923)
    parser.add_argument('--random-count', type=int, default=20)
    parser.add_argument('--overwrite', action='store_true')
    parser.add_argument('--self-test', action='store_true', help='검증만 실행하고 종료')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.random_count < 0:
        parser.error('--random-count must be nonnegative')
    limit = 1000 if args.version == 'easy' else 200000
    out = args.out or Path('tests') / args.version
    if out.exists() and any(out.iterdir()) and not args.overwrite:
        parser.error(f'{out} is not empty; use a new directory or --overwrite')
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for index, (name, n, k, edges) in enumerate(
            cases(limit, random.Random(args.seed), args.random_count), 1):
        validate(n, k, edges, limit)
        answer = solve(n, k, edges)
        if n <= 30 and answer != brute(n, k, edges):
            raise AssertionError(f'DFS mismatch: {name}')
        stem = f'{index:03}_{name}'
        with (out / f'{stem}.in').open('w', encoding='utf-8', newline='\n') as f:
            f.write(f'{n} {len(edges)} {k}\n')
            f.writelines(f'{a} {b}\n' for a, b in edges)
        (out / f'{stem}.ans').write_text(f'{answer}\n', encoding='utf-8')
        rows.append([stem, n, len(edges), k, answer, args.seed, args.version])
        print(f'{stem}: N={n}, M={len(edges)}, K={k}, answer={answer}')
    with (out / 'manifest.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['case', 'N', 'M', 'K', 'answer', 'seed', 'version'])
        writer.writerows(rows)
    print(f'Generated {len(rows)} input/answer pairs in {out.resolve()}')


if __name__ == '__main__':
    main()
