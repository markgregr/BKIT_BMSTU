import sys
import math

# получение коэффициентов
def get_coef(index, prompt):
    try:
        coef = float(sys.argv[index])
    except:
        while(True):
            try:
                coef = float(input(prompt))
                break
            except ValueError:
                print("Введён неправильный коэффициент.")
    return coef

def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D==0.0:
        root = -b / (2.0 * a)
        if root>0:
            result += [math.sqrt(root), -math.sqrt(root)]
        if b==0:
            result.append(0)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1>0:
            result+=[math.sqrt(root1), -math.sqrt(root1)]
        if root2 > 0:
            result += [math.sqrt(root2), -math.sqrt(root2)]
        if root1 == 0 or root2 == 0:
            result.append(0)
            return result
    return result

def main():  # основная функция
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
