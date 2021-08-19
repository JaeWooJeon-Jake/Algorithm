pasta = []
juice = []

for _ in range(3):
    pasta.append(int(input()))

for _ in range(2):
    juice.append(int(input()))

min = (min(pasta) + min(juice)) * 1.1

print(round(min, 1))