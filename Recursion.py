def test_dif_params(txt, *args, default_='По умолчанию', **kwargs):
    print(txt)
    print(*args)
    print(default_)
    print(kwargs)


test_dif_params('простой набор всего', 1, 2, 3, 4, name='Ivan', surname='Ivanov')


def recurs(num):
    if num < 0:
        return f'не производится'
    elif 0 <= num <= 1:
        return 1
    else:
        return num * recurs(num - 1)


print(recurs(5))
