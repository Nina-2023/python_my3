def my_func(x, y):
    res = 1
    if y > 0:
        for i in range(abs(y)):
            res *= x
    else:
        for i in range(abs(y)):
            res /= x
    return res

print(my_func(2, -3))  # 0.125