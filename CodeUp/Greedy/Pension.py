def check(n):
    if len(day[n]) == 0:
        return 0

    max = 0
    for i in day[n]:
        temp = 0
        for j in range(n, t):
            if i in day[j]:
                temp += 1
            else:
                break

        if max < temp:
            max = temp
    return max


n, m = map(int, input().split())

day = [[]]

for _ in range(n):
    rooms = []
    a = list(input())
    for i in range(m):
        if a[i] == 'O':
            rooms.append(i + 1)
    day.append(rooms)

s, t = map(int, input().split())

cnt = -1
today = s

while today < t:
    stay = check(today)

    if stay == 0:
        cnt = -1
        break

    cnt += 1
    today += stay

print(cnt)
