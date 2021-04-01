from vvod import hotiteLi as hotiteLi, array as array, pravilnoLi as pravilnoLi, L as L
from raschet import masssiveFunFormForEachElementInTochka as masssiveFunFormForEachElementInTochka, N as N, U as U,okr as okr, roundNum as roundNum
# PeremeshenieElementaVTochke = 0


def sluchPeremeshenie():
    PeremeshenieElementaVTochke = 0
    element = None
    while element == None:
        element = input('Введите номер элемента от 1 до ' + str(len(array)) + ' ')
        element = pravilnoLi(element, False, False, False, True)
        if element != None:
            element = int(element)
            if element <= len(array) and element > 0:
                m = '1'
                while m == '1':
                    x = input('Введите координату от 0 до 1 в ' + str(element) + ' элементе в долях от ' + str(
                        L[element - 1]) + ' м ')
                    x = float(x)
                    if x <= 1 and x >= 0:
                        masssiveFunFormForEachElementInTochka(x)
                        PeremeshenieElementaVTochke = N[element - 1][0] * U[element - 1] + N[element - 1][1] * U[
                            element]
                        if okr is True:
                            PeremeshenieElementaVTochke = roundNum(PeremeshenieElementaVTochke, kolZnakPoslZap)
                        print(PeremeshenieElementaVTochke)
                        m = hotiteLi('Хотите снова найти перемещение в ' + str(element) + ' элементе? ')
                    else:
                        print('Непрвильная координата\n')
            else:
                print('Непрвильный номер элемента\n')
    return PeremeshenieElementaVTochke


m = hotiteLi('Хотите найти перемещение в указанной точке? ')
if m == '1' or m.lower() == 'да':
    m = '1'
    while m == '1' or m.lower() == 'да':
        sluchPeremeshenie()
        m = hotiteLi('Хотите снова найти перемещение в указанной точке? ')

print('')

arrT = []

rasDef = False
maxDef = False


def skolkoTochek(rasDef, maxDef):
    kolT = None
    while kolT == None:
        if rasDef is True:
            kolT = input('Сколько точек хотите рассмотреть в каждом элементе? (Не считая узловых точек) ')
        elif maxDef is True:
            kolT = input('На сколько точек хотите разбить элементы? ')
        kolT = pravilnoLi(kolT, False, False, True, True)
    for i in range(int(kolT) + 2):
        arrT.append(1 / (int(kolT) + 1) * i)
    return arrT


arrRas = []
for i in range(len(array)):
    arrRas.append([])


def makeArrayRaspredelenya():
    skolkoTochek(True, False)
    for i in range(len(array)):
        for j in range(len(arrT)):
            masssiveFunFormForEachElementInTochka(arrT[j])
            PeremeshenieElementaVTochke = N[i][0] * U[i] + N[i][1] * U[i + 1]
            if okr is True:
                PeremeshenieElementaVTochke = roundNum(PeremeshenieElementaVTochke, kolZnakPoslZap)
            arrRas[i].append(PeremeshenieElementaVTochke)
    return arrRas


m = hotiteLi('Хотите посмотреть распределение перемещений по элементам? ')
if m == '1' or m.lower() == 'да':
    makeArrayRaspredelenya()
    print(arrRas)

print('')

arrRas = []
for i in range(len(array)):
    arrRas.append([])


a = roundNum(40, 2)

arrT = []
Max = ['','','']

def seekMax():
    skolkoTochek(False, True)
    for i in range(len(array)):
        for j in range(len(arrT)):
            masssiveFunFormForEachElementInTochka(arrT[j])
            PeremeshenieElementaVTochke = N[i][0] * U[i] + N[i][1] * U[i + 1]
            if okr is True:
                PeremeshenieElementaVTochke = roundNum(PeremeshenieElementaVTochke, kolZnakPoslZap)
            arrRas[i].append(PeremeshenieElementaVTochke)
    Max[0] = arrRas[0][0]
    for i in range(len(arrRas)):
        for j in range(len(arrRas[i]) - 1):
            if arrRas[i][j + 1] > arrRas[i][j]:
                if okr is True:
                    arrRas[i][j + 1] = roundNum(arrRas[i][j + 1], kolZnakPoslZap)
                Max[0] = arrRas[i][j + 1]
                Max[1] = i
                Max[2] = j
    return Max


m = hotiteLi('Хотите найти максимальное перемещение? ')
if m == '1' or m.lower() == 'да':
    max = seekMax()
    print('Максимальное значение перемещения ' + str(max[0]) + ' в элементе ' + str(max[1]) + ' в точке ' + str(max[2]))

print('\n' + 'Конец решения')
