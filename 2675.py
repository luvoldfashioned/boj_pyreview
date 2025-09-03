T = int(input())
while T != 0:
    R, S = input().split()
    new_string = ""
    for literal in S:
        new_string += int(R)*literal
    print(new_string)
    T -= 1
