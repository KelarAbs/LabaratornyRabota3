age = input("Введите возраст в диапазоне от 20 до 40 включительно: ")
age = int(age)
def age_corrector(x):
    number_age = str(x)
    number_age1 = number_age[0]
    number_age2 = number_age[1]
    str_number_age1 = ""
    str_number_age2 = ""
    
    #Первая часть числа
    
    if number_age1 == '2':
        str_number_age1 = "Двадцать"
    if number_age1 == '3':
        str_number_age1 = "Тридцать"
    if number_age1 == '4':
        str_number_age1 = "Сорок"
    
    #Вторая часть числа
    
    if number_age2 == '1':
        str_number_age2 = " один"
    if number_age2 == '2':
        str_number_age2 = " два"
    if number_age2 == '3':
        str_number_age2 = " три"
    if number_age2 == '4':
        str_number_age2 = " четыре"
    if number_age2 == '5':
        str_number_age2 = " пять"
    if number_age2 == '6':
        str_number_age2 = " шесть"
    if number_age2 == '7':
         str_number_age2 = " семь"
    if number_age2 == '8':
        str_number_age2 = " восемь"
    if number_age2 == '9':
        str_number_age2 = " девять"
    if number_age2 == '0':
        str_number_age2 = ""
    return str_number_age1 + str_number_age2

res_age_corrector = age_corrector(age)

if (int(age)<=40) and (int(age)>=20):
    if (age==20) or (age==30) or (age==40) or ((age>=25) and (age<30)) or ((age>=35) and (age<40)):
        print(res_age_corrector + ' лет')
    if (str(age)[1]=='1'):
        print(res_age_corrector + ' год')
    if (str(age)[1]=='2') or (str(age)[1]=='3') or (str(age)[1]=='4'):
        print(res_age_corrector + ' года')
else:
    print("Неверный диапозон возраста")

