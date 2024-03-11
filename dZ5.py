# N = int(input())
# numbers = []
# for _ in range(N):
#     number = int(input())
#     numbers.append(number)
# reversed_numbers = numbers[::-1]
# for number in reversed_numbers:
#     print(number)
# print(reversed_numbers)

# num = int(input())
# num1 = list(map(int, input().split()))
# newNum = [num1[-1]] + num1[:-1]
# print(newNum)

# m = int(input())
# n = int(input())
# a = []
# b = []

# for i in range(n):
#     a.append(int(input()))
# x = 0
# while x < len(a):
#     if a[x] + min(a) <= m:
#         b.append([a[x], min(a)])
#         a[x] += m
#         a[a.index(min(a))] += m
#     else:
#         if a[x] > m:
#             x += 1
#             continue
#         else:
#             b.append([a[x]])
#     x += 1
# print(len(b))