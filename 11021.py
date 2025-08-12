T = int(input())
count = 1

while T > 0:
    A, B = map(int, input().split())
    print(f"Case #{count}: {A+B}")
    count += 1
    T -= 1
