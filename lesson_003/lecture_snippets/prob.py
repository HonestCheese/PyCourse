from dis import dis


def  some_func(param):
    a = 43
    print(a, param)
    return a
dis(some_func)