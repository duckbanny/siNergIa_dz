# x = float(input())
# if x == 0:
#     print("нулевое число")
# elif x % 2 == 0:
#     if x > 0:
#         print("положительное четное число")
#     elif x < 0:
#         print("отрицательное четное число")
# else:
#     print("число не является четным")


# def number(x):
#     if x == 0:
#         return "нулевое число"
#     elif x % 2 == 0:
#         if x > 0:
#             return "положительное четное число"
#         elif x < 0:
#             return "отрицательное четное число"
#     else:
#         return "число не является четным"

# x = float(input())
# print(number(x))


# word = input()
# vowels = {'a', 'e', 'i', 'o', 'u'}
# vowelcount = 0
# consonantcount = 0
# for letter in word:
#     if letter in vowels:
#         vowelcount += 1
#     elif letter.isalpha():
#         consonantcount += 1
# if vowelcount == 0 or consonantcount == 0:
#     print(False)
# else:
#     print(f"Количество гласных букв: {vowelcount}")
#     print(f"Количество согласных букв: {consonantcount}") 

word = input()
xa = word.count("a")
xe = word.count("e")
xo = word.count("o")
xu = word.count("u")
xi = word.count("i")
countwordG = xa + xe + xo + xu + xi
countwordS = len(word) - countwordG
print("гласные", countwordG)
print("согласные", countwordS)
if xa != 0:
    print("a =", xa)
else:
    print("a =", False)
if xe != 0:
    print("e =", xe)
else:
    print("e =", False)    
if xo != 0:
    print("o =", xo)
else:
    print("o =", False)
if xu != 0:
    print("u =", xu)
else:
    print("u =", False)
if xi != 0:
    print("i =", xi)
else:
    print("i =", False)     

#gpt
word = input()
vowels = 'a', 'e', 'i', 'o', 'u'
vowelcounts = {vowel: word.count(vowel) for vowel in vowels}
consonantcount = len(word) - sum(vowelcounts.values())
print("гласные", sum(vowelcounts.values()))
print("согласные", consonantcount)
for vowel, count in vowelcounts.items():
    if count != 0:
        print(f"{vowel} =", count)
    else:
        print(f"{vowel} =", False)