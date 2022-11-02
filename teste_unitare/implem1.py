def max_value(a, b, c):
    if a >= b and a >= c:
        max_val = a
    elif b >= c and b >= a:
        max_val = b
    else:
        max_val = c
    return max_val


if __name__ == "__main__":
    print(max_value(-8, 2, 4))
    print(max_value(12, -9, 18))
    print(max_value(12, 28, -9))
