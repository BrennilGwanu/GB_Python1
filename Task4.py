# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def Cranes():
    c = int(input("Кол-во журавликов: "))
    c1 = int(c * 0.25)
    c2 = int(c * 0.5)
    print (c2, c1, c1)

Cranes()