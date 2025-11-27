S = input().strip()
N = int(input().strip())
arr = list(map(int, input().split()))

for num in arr:
    print(S * num)
