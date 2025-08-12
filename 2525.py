current_hour, current_min = map(int, input().split())
needed_time = int(input())

total_min = current_hour * 60 + current_min + needed_time
result_hour = (total_min // 60) % 24
result_min = total_min % 60

print(result_hour, result_min)
