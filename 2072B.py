def max_subsequences(t, test_cases):
    results = []
    for case in test_cases:
        n, s = case
        count_minus = s.count('-')
        count_underscore = s.count('_')
        
        if count_underscore == 0 or count_minus < 2:
            results.append(0)
            continue
        
        subsequences = count_minus * (count_minus - 1) // 2 * count_underscore
        results.append(subsequences)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

results = max_subsequences(t, test_cases)

for res in results:
    print(res)