def type_logger(func):
    def tag_wrapper(*args, **kwargs):
        print(f'{func.__name__}(', end='')
        print(*list(map(lambda x: f'{x}: {type(x)}', args)),
              *list(map(lambda x: f'{x}={kwargs[x]}: {type(kwargs[x])}', kwargs)),
              sep=', ', end='')
        print(')')
        markup = func(*args, **kwargs)
        print(f'result: {type(markup)}')
        return markup

    return tag_wrapper


@type_logger
def calc_cube(x, y, degree=3, info=''):
    return (x * y) ** degree


result = calc_cube(5, 2, degree=2, info='test')
print(result)
