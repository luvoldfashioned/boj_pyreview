num = int(input())
i = 2
while i <= num:
    # for i in range(2, num+1):
    if num % i == 0:
        print(i)
        num /= i
        # print(num)
    else:
        i += 1
