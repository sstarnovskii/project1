age = input("Ваш возраст, полных лет: ")
height = input("Ваш рост, в см: ")
weight = input("Ваш вес, в кг: ")
sex = input("Ваш пол (М или Ж): ")
print("Ваш образ жизни по шкале от 1 до 10, где 1 - полностью сидячий, неактивный образ жизни,")
lifestyle = input("10 - очень активный, спортивный образ жизни: ")
height = float(height)/100
imt = float(weight)/(float(height)**2)
print(age, height, weight, sex, lifestyle, round(imt, 2))

