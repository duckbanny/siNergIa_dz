#Введите вид питомца, его возраст и кличку

# a_pet, age, name_animal = input(), input(), input()
# print("Это", a_pet, "по кличке", name_animal, "Возраст:", age, "года.")


#тест по биологии для студентов.Напишите по порядку 9 этапов развития человека

# a1 = "Ardipithecus"
# a2 = "Australopithecus"
# a3 = "Paranthropus"
# a4 = "A skilled man"
# a5 = "The man is upright"
# a6 = "The man is upright"
# a7 = "The Flores man"
# a8 = "Neanderthals"
# a9 = "Homo sapiens"

# print(a1, a2, a3, a4, a5, a6, a7, a8, a9, sep="=>")



# Создаем пустой список для хранения стадий развития
stages = []

# Запрашиваем у пользователя ввод 9 стадий развития
for i in range(9):
    stage = input(f'Введите {i+1}-ю стадию развития человека: ')
    stages.append(stage)

# Выводим на экран список введенных стадий развития в одну строку с запятой в качестве разделителя
print("Стадии развития человека:", " => ".join(stages))
print("Верный ответ:Ardipithecus","Australopithecus","Paranthropus","A skilled man","The man is upright","The man is upright", "The Flores man","Neanderthals","Homo sapiens", sep="=>")