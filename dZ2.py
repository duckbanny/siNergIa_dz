

# side1, side2 = map(float, input().split())
# p = 2 * (side1 + side2) 
# s = side1 * side2
# print("Периметр =", p, "\n" "Площадь =", s)



a = int(input())
x1 = a % 10
x2 = (a // 10) % 10
x3 = (a // 100) % 10
x4 = (a // 1000) % 10
x5 = a // 10000
result = (x2 ** x1 * x3 / (x5 - x4))
print(result)

a = int(input())
result = (a // 10 % 10) ** (a % 10) * (a // 100 % 10) / (a // 10000 - a // 1000 % 10)
print(result)

