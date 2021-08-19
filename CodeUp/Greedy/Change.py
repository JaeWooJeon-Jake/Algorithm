currencies = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
currencies.reverse()
count = 0

n = int(input())

for i in currencies:
    count += n // i
    n %= i

print(count)
