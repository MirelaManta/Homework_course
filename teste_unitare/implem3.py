def in_set(a, my_set):
    if a not in my_set:
        # my_set.add(a)
        # print('Am adaugat numarul nou in set.')
        return False
    else:
        # print('Nu am adaugat numarul nou in set. Acesta exista deja.')
        return True


if __name__ == '__main__':
    print(in_set(3, {2, 4, 7, 3, 9}))
    print(in_set(6, {1, 2, 4, 7, 3}))
