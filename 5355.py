T = int(input())  # number of testcases
for case in range(T):
    equation_list = input().split()
    num = float(equation_list[0])
    for operator in equation_list[1:]:
        if operator == "@":
            num *= 3
        elif operator == "%":
            num += 5
        elif operator == "#":
            num -= 7
        else:
            print("error detect")
    print(f"{num:.2f}")
