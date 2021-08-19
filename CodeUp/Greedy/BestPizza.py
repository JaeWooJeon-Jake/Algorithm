n = int(input())
a, b = map(int, input().split())
c = int(input())

topping = []
for i in range(n):
    topping.append(int(input()))
topping.sort()
topping.reverse()

pizzas = []
pizzas.append((a,c))

for i in range(n):
    price = a + b*(i+1)
    cal = pizzas[i][1] + topping[i]
    pizzas.append((price, cal))

bestPizza = 0
for i in pizzas:
    tempPizza = i[1] // i[0]
    if tempPizza > bestPizza:
        bestPizza = tempPizza

print(bestPizza)