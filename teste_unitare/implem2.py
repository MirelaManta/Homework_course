def compare(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}.')
        return 1
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}.')
        return -1
    else:
        print('Numerele sunt egale.')
        return 0


if __name__ == '__main__':
    compare(5, 9)
    compare(7, -2)
    compare(8, 8)
