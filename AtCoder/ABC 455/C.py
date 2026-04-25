n, k = map(int, input().split())
a = list(map(int, input().split()))

element = dict()
for t in a:
    if t in element:
        element[t] += 1
    else:
        element[t] = 1

counts = []
for e in element:
    counts.append(e*element[e])
counts.sort()

print(sum(counts[:-k]))