t = int(input())
tests = [tuple(map(int, input().split())) for _ in range(t)]

results = []
for case in tests:
    n, k, p = case
    max_sum = n * p
    min_sum = -n * p
    if k < min_sum or k > max_sum:
        results.append(-1)
        continue
    if k == 0:
        results.append(0)
        continue
    operations = abs(k) // p
    if abs(k) % p != 0:
        operations += 1
    results.append(operations)

for res in results:
    print(res)