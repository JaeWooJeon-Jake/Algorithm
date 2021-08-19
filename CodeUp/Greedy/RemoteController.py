count = 0

a, b = map(int, input().split())

while a != b:
    if abs(a-b) >= 8:
        if a > b:
            a = a - 10
            print("10도 내림")
        else:
            a = a + 10
            print("10도 올림")
        count += 1
    elif 3 <= abs(a-b) < 8:
        if a > b:
            a = a - 5
            print("5도 내림")
        else:
            a = a + 5
            print("5도 올림")
        count += 1
    else:
        if a > b:
            a = a - 1
            print("1도 내림")
        else:
            a = a + 1
            print("1도 올림")
        count += 1

print(count)
