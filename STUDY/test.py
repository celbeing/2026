a = [i for i in range(1, 100) if i % 3 == 0]
for b in a:
    print(b)

fib = []
fib = [1 if i < 2 else (fib[-1]+fib[-2]) for i in range(1, 100)]
print(fib)