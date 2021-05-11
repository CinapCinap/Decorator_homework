import datetime


def printable(logs_path):
    def _printable(old_function):
        def new_function(*args, **kwargs):
            f_datetime = datetime.datetime.now()
            f_result = old_function(*args, **kwargs)
            with open(logs_path, 'a', encoding='utf-8') as file:
                file.write(f'{f_datetime} вызвана функция {old_function.__name__} '
                f'с параметрами {args} {kwargs} вернула результат {f_result}\n')
            return f_result
        return new_function
    return _printable
