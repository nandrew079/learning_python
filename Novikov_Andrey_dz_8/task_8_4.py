def val_checker(func_checking):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if type(i) == int:
                    if not func_checking(i):
                        msg = f'wrong val {i}'
                        raise ValueError(msg)
                else:
                    msg = f'wrong val {i}'
                    raise ValueError(msg)
            markup = func(*args, **kwargs)
            return markup
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-4)
