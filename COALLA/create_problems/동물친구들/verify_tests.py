"""Validate fixture constraints and run every numbered input against solution.py."""
from pathlib import Path
import subprocess
import sys
import time


def main():
    root=Path(__file__).resolve().parent
    cases=sorted((root/'tests').glob('*.in'),key=lambda p:int(p.stem))
    assert cases and [int(p.stem) for p in cases]==list(range(1,len(cases)+1))
    assert {p.stem for p in cases}=={p.stem for p in (root/'tests').glob('*.out')}
    slowest=(0,None)
    for path in cases:
        lines=path.read_text().splitlines()
        n,l,m,k=map(int,lines[0].split())
        assert 1<=n<=15 and n<=l<=1000 and 0<=m<=3000 and 1<=k<=10**9
        assert len(lines)==1+l+m
        graph=[[] for _ in range(n+1)]
        for line in lines[1:1+l]:
            u,v,t=map(int,line.split())
            assert 0<=u<=n and 0<=v<=n and u!=v and 1<=t<=10**9
            graph[u].append(v); graph[v].append(u)
        visited={0}; stack=[0]
        while stack:
            for v in graph[stack.pop()]:
                if v not in visited:
                    visited.add(v); stack.append(v)
        assert len(visited)==n+1
        for line in lines[1+l:]:
            i,a,b=map(int,line.split())
            assert 1<=i<=n and 0<=a<=b<=k
        expected=path.with_suffix('.out').read_text().split()
        assert len(expected)==1 and 0<=int(expected[0])<=n
        start=time.perf_counter()
        result=subprocess.run([sys.executable,str(root/'solution.py')],input=path.read_bytes(),capture_output=True,timeout=15,check=True)
        elapsed=time.perf_counter()-start
        assert result.stdout.decode().split()==expected, (path.name,result.stdout,expected)
        if elapsed>slowest[0]: slowest=(elapsed,path.name)
    print(f'PASS {len(cases)}/{len(cases)}; slowest {slowest[1]}: {slowest[0]:.3f}s')


if __name__=='__main__':
    main()
