number = int(input())
counter = 0
for i in range(number):
    number1 = int(input())
    if number1 == 0:
        counter += 1
print(counter)     

counter = sum(1 for _ in range(int(input())) if int(input()) == 0)
print(counter)

number = int(input())
counter = 0
