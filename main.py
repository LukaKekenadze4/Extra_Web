def func():
    list_ = []
    for i in range(0,2):
        list_.append(i)
    return list_, i


print(func()[1])