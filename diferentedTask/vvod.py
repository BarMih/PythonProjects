# обьявляем массив жескостей
array = []
nakazanie = ''
repeat = True


# Валидность
def pravilnoLi(name, flt, mns, null, one):
    # Убираем пробелы
    name = name.strip()
    # Пустая строка
    if name == '':
        name = None
        warning = print('Вы ввели пустую строку. Повторите попытку ввода.')
    # Буквы или цифры
    elif name.isalnum() is True:
        # Цифра
        if name.isdigit() is True:
            # 0
            if int(name) == 0:
                if null is False:
                    if flt is False and mns is False and null is False:
                        name = None
                        warning = print('Вы ввели 0. Необходимо как минимум 2 элемента. Повторите попытку ввода.')
                    elif null is False and one is True:
                        name = None
                        warning = print('Вы ввели 0. Необходимо ввести корректную величину. Повторите попытку ввода.')
                    # else:
                # правильное усилие
                # else:

            # 1
            elif int(name) == 1 and flt is False and one is False:
                name = None
                warning = print('Вы ввели меньше 2. Необходимо как минимум 2 элемента. Повторите попытку ввода.')
            # Правильно
            # else:

        # Буква
        elif name.isalpha() is True:
            # Мат
            if name == 'hyu' or name == 'cyka' or name == 'pidr' or name == 'blyad':
                name = None
                warning = print('Материться нельзя!')
                nakazanie = 'Неудачник'
            # Буква
            else:
                name = None
                warning = print('Вы ввели буквы. Повторите попытку ввода.')
        # Буква и цифра
        else:
            name = None
            warning = print('Вы ввели буквы и цифры. Повторите попытку ввода.')
    # Спецсимволы
    else:
        tochka = False
        for i in range(len(name)):
            if name[i] == '.':
                tochka = True
        # Отрицательное
        if name[0] == '-' and mns is False:
            name = None
            warning = print('Вы ввели отрицательное значение. Повторите попытку ввода.')
        elif name[0] == '-' and mns is True:
            name
        # Цифра с плавающей запятой
        elif tochka is True:
            if float(name) % 2 != float(0) and float(name) % 2 != float(1):
                if flt is False and null is False:
                    name = None
                    warning = print(
                        'Вы ввели число c плавающей запятой. Количество элементов может быть только целым числом Повторите попытку ввода.')
                elif null is True:
                    name = None
                    warning = print(
                        'Вы ввели число c плавающей запятой. Количество точек может быть только целым числом Повторите попытку ввода.')
            # Правильно
            else:
                name = str(name.rstrip('0,.'))
        # Спецсимвол
        else:
            name = None
            warning = print('Вы ввели спецсимвол либо опечатались. Повторите попытку ввода.')
    return name


def hotiteLi(text):
    m = ''
    while m != '1' and m != '0' and m.lower() != 'да' and m.lower() != 'нет':
        m = input(text)
    return m


def roundNum(num, kolZnakPoslZap):
    num = round(num * 10 ** int(kolZnakPoslZap))/(10 ** int(kolZnakPoslZap))
    return num


# заполняем массив жесткостей
def masiveGestkosti():
    el = None
    while el == None:
        el = input('Введите число элементов ' + nakazanie)
        el = pravilnoLi(el, False, False, False, False)
    m = hotiteLi('Хотите ввести значения жесткости элементов вручную? (Иначе все будет равно 1) ')
    if m == '1' or m.lower() == 'да':
        for i in range(int(el)):
            vvodG = None
            while vvodG == None:
                vvodG = input('Введите жесткость ' + str(i + 1) + '-го элемента' + ' ')
                vvodG = pravilnoLi(vvodG, True, False, False, True)
                if vvodG != None:
                    array.append(vvodG)
    elif m == '0' or m.lower() == 'нет':
        for i in range(int(el)):
            array.append(1)
    print('')
    return array


arrayUsiliy = []


# заполняем массив усилий
def masiveYsiliy():
    uzli = len(array) - 1
    arrayUsiliy.append(0)
    m = hotiteLi('Хотите ввести значения усилий в узлах вручную? (Иначе все будет равно 1) ')
    if m == '1' or m.lower() == 'да':
        for i in range(int(len(array) - 1)):
            vvodY = None
            while vvodY == None:
                vvodY = input('Введите усилие в ' + str(i + 2) + '-ом узле ')
                vvodY = pravilnoLi(vvodY, True, True, True, True)
                if vvodY != None:
                    arrayUsiliy.append(vvodY)
    else:
        for i in range(int(len(array) - 1)):
            arrayUsiliy.append(1)
    arrayUsiliy.append(0)
    print('')
    return arrayUsiliy


L = []


# заполняем массив длин
def masiveLength():
    m = hotiteLi('Хотите ввести значения длин элементов вручную? (Иначе все будет равно 1) ')
    if m == '1' or m.lower() == 'да':
        for i in range(int(len(array))):
            vvodL = None
            while vvodL == None:
                vvodL = input('Введите длину ' + str(i + 1) + '-ого участка' + ' ')
                vvodL = pravilnoLi(vvodL, True, False, False, True)
                if vvodL != None:
                    L.append(vvodL)
    else:
        for i in range(int(len(array))):
            L.append(1)
    print('')
    return L


masiveGestkosti()

balka = []


def chertezUzlov():
    print('Предварительный чертеж балки, включите воображение')
    for i in range(len(array) * 2 + 1):
        if i % 2 == 0:
            balka.append('F' + str(round(i / 2 + 1)))
        else:
            balka.append('----')
    print('F1' + ' и ' + 'F' + str(round(i / 2 + 1)) + '- заделки')
    return balka


chertezUzlov()
print(balka, ' --> X', '\n')
masiveLength()
masiveYsiliy()
# вывод массивов
print('Массив жесткостей элементов EF\n', array, '\n')
print('Массив длин элементов L\n', L, '\n')
print('Массив узловых усилий F\n', arrayUsiliy, '\n')

balkaM = []


def chertezUzlovM():
    print('Чертеж балки в масштабе с узловыми усилиями')
    for i in range(len(array) * 2 + 1):
        if i % 2 == 0:
            balkaM.append(arrayUsiliy[round(i / 2)])
        else:
            balkaM.append(('-' * int(L[round((i - 1) / 2)])))
    balkaM[0] = 'F1'
    balkaM[-1] = 'F' + str(round(i / 2 + 1))
    print('F1' + ' и ' + 'F' + str(round(i / 2 + 1)) + '- заделки')
    return balkaM


chertezUzlovM()

print(balkaM, ' --> X', '\n')
