
n = int(input())
locations = []
answer = -1
for _ in range(n):
    D, A = map(int, input().split())
    locations.append((D, A))

min_distance_sum = float('inf')
for i in range(n):
    distance_sum = 0
    for j in range(n):
        distance_sum += abs(locations[i][0] - locations[j][0]) * locations[j][1]
    if distance_sum < min_distance_sum:
        min_distance_sum = distance_sum
        answer = i + 1

print(answer)

