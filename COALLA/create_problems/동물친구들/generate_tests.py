"""Deterministic fixtures; small answers use an independent time-expanded oracle.
Run in this directory. Existing numbered fixtures are overwritten.
"""
from pathlib import Path
from random import Random


def oracle(n, edges, windows, k):
    # Explore actual edges one second/time jump at a time; no Floyd or subset DP.
    adj = [[] for _ in range(n + 1)]
    for u, v, t in edges:
        adj[u].append((v, t))
        adj[v].append((u, t))
    visible = [[0] * (n + 1) for _ in range(k + 1)]
    for i, a, b in windows:
        for t in range(a, b + 1):
            visible[t][i] = 1 << (i - 1)
    states = [set() for _ in range(k + 1)]
    states[0].add((0, 0))
    answer = 0
    for t, bucket in enumerate(states):
        for u, mask in bucket:
            mask |= visible[t][u]
            if u == 0:
                answer = max(answer, mask.bit_count())
            if t < k:
                states[t + 1].add((u, mask))
            for v, cost in adj[u]:
                if t + cost <= k:
                    states[t + cost].add((v, mask))
    return answer


def main():
    rng = Random(20261026)
    cases = []

    def add(label, n, edges, windows, k, expected=None):
        if expected is None:
            expected = oracle(n, edges, windows, k)
        cases.append((label, n, edges, windows, k, expected))

    add('example 1: waiting', 3, [(0,1,2),(1,2,2),(2,3,2),(3,0,3)], [(1,3,4),(2,5,6),(3,7,8)],12)
    add('example 2: revisit and exact deadline',2,[(0,1,3),(1,2,1)],[(1,0,2),(1,5,6),(2,4,4)],8)
    add('example 3: cannot return',1,[(0,1,3)],[(1,3,5)],5)
    add('no windows, minimum K',1,[(0,1,1)],[],1)
    add('instant window, exact return',1,[(0,1,1)],[(1,1,1)],2)
    add('expired before arrival',1,[(0,1,2)],[(1,0,1)],10)
    add('waiting until opening',1,[(0,1,1)],[(1,8,8)],9)
    add('parallel edges and overlapping unsorted windows',2,[(0,1,9),(0,1,1),(1,2,1)],[(1,3,7),(1,1,4),(1,1,4),(2,2,2)],8)
    add('shortest route via another cage',3,[(0,1,1),(1,2,1),(2,3,1),(0,3,20)],[(1,1,1),(2,2,2),(3,3,3)],6)
    add('repeated sighting counts once',1,[(0,1,1)],[(1,0,2),(1,4,6),(1,8,10)],12)
    add('missing animals',3,[(0,1,1),(0,2,1),(0,3,1)],[(2,2,4)],8)
    add('all windows at time zero',3,[(0,1,1),(1,2,1),(2,3,1)],[(i,0,0) for i in range(1,4)],10)
    for trial in range(60):
        n = rng.randint(1,6)
        k = rng.randint(2,25)
        edges = [(i,rng.randrange(i),rng.randint(1,6)) for i in range(1,n+1)]
        for _ in range(rng.randint(0,12)):
            u,v = rng.sample(range(n+1),2)
            edges.append((u,v,rng.randint(1,10)))
        windows=[]
        for _ in range(rng.randint(0,25)):
            a=rng.randint(0,k)
            windows.append((rng.randint(1,n),a,rng.randint(a,k)))
        add(f'random small {trial+1}: independent oracle',n,edges,windows,k)
    # Star metric: each distinct animal costs at least two seconds round trip.
    star=[(0,i,1) for i in range(1,16)]
    add('N maximum, all animals',15,star,[(i,0,30) for i in range(1,16)],30,15)
    add('N maximum, budget excludes one',15,star,[(i,0,28) for i in range(1,16)],28,14)
    # Parallel unit edges preserve the star metric. Exactly 3,000 windows.
    edges=star+[(0,rng.randint(1,15),rng.randint(1,10**9)) for _ in range(985)]
    windows=[(i,100*j,100*j+50) for i in range(1,16) for j in range(200)]
    rng.shuffle(windows)
    add('L M maximum, disjoint windows, large K',15,edges,windows,10**9,15)
    add('large weights and unavailable return',15,[(0,i,10**9) for i in range(1,16)],[(i,10**9,10**9) for i in range(1,16)],10**9,0)
    add('M maximum, overlapping and duplicate windows',15,star,[(i,0,30) for i in range(1,16) for _ in range(200)],30,15)
    add('simultaneous instant windows: only one animal',15,star,[(i,15,15) for i in range(1,16)],30,1)
    out=Path(__file__).resolve().parent/'tests'
    out.mkdir(exist_ok=True)
    manifest=['# Test cases', '', 'Small cases use a time-expanded graph oracle on the original edges.', 'Large cases use the stated star-metric bounds or an explicit feasible tour.', '']
    for number,(label,n,edges,windows,k,expected) in enumerate(cases,1):
        lines=[f'{n} {len(edges)} {len(windows)} {k}']
        lines += [' '.join(map(str,e)) for e in edges]
        lines += [' '.join(map(str,w)) for w in windows]
        (out/f'{number}.in').write_text('\n'.join(lines)+'\n')
        (out/f'{number}.out').write_text(f'{expected}\n')
        manifest.append(f'- {number}: {label}; answer {expected}')
    (out/'README.md').write_text('\n'.join(manifest)+'\n')
    print(f'Generated {len(cases)} cases')


if __name__ == '__main__':
    main()
