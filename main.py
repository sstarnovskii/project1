age = input("Ваш возраст, полных лет: ")
height = input("Ваш рост, в см: ")
weight = input("Ваш вес, в кг: ")
sex = input("Ваш пол (М или Ж): ")
lifestyle = int(input("Ваш образ жизни по шкале от 1 до 10, где 1 - полностью сидячий, неактивный образ жизни,\n10 - очень активный, спортивный образ жизни: "))
height = float(height)/100
imt = float(weight)/(float(height)**2)
if lifestyle <= 4:
    addwater = 0
elif  4 <= lifestyle <=8:
    addwater = 2
else: addwater = 4
print("Ваш индекс массы тела - ", round(imt, 2), ".", sep='')
print("Вам рекомендуется пить не менее", int(round(float(weight)/9)*0.25) + addwater, "л чистой воды в день.")
print(age, height, weight, sex, lifestyle, round(imt, 2))

