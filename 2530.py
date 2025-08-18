A, B, C = map(int, input().split())
taken_sec = int(input())

current_sec = A*3600 + B*60 + C

total_sec = taken_sec + current_sec

result_hour = (total_sec//3600) % 24
result_min = (total_sec % 3600)//60
result_sec = (total_sec % 3600) % 60


print(result_hour, result_min, result_sec)
