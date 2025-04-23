def process_data(data, operation, process='values'):
    try:
        if not callable(operation):
            raise TypeError
        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        elif isinstance(data, dict):
            if process == 'keys':
                return {operation(k): v for k, v in data.items()}
            elif process == 'values':
                return {k: operation(v) for k, v in data.items()}
            elif process == 'items':
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                raise ValueError
        else:
            raise TypeError
    except Exception as e:
        return f"Помилка: {e}"


def filter_data(data, predicate):
    try:
        if not callable(predicate):
            raise TypeError
        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        elif isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        else:
            raise TypeError
    except Exception as e:
        return f"Помилка: {e}"


def combine_values(*args, separator='', initial=None):
    try:
        if not args:
            return None
        first_type = type(args[0])
        if first_type == str:
            return separator.join(str(arg) for arg in args)
        elif first_type in (int, float):
            result = initial if initial is not None else 0
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError
                result += arg
            return result
        else:
            raise TypeError
    except Exception as e:
        return f"Помилка: {e}"


# Тестування від користувача
def user_test():
    print("Оберіть функцію для тестування:")
    print("1 — process_data")
    print("2 — filter_data")
    print("3 — combine_values")
    choice = input("Введіть номер функції: ")

    if choice == "1":
        data_type = input("Тип колекції (list, tuple, dict): ")
        if data_type == "list":
            data = [1, 2, 3, 4]
            result = process_data(data, lambda x: x * 2)
        elif data_type == "tuple":
            data = (10, 20, 30)
            result = process_data(data, lambda x: x + 5)
        elif data_type == "dict":
            data = {"a": 1, "b": 2}
            process = input("Що обробляти (keys, values, items): ")
            result = process_data(data, lambda x: str(x).upper(), process)
        else:
            result = "Невідомий тип даних"
        print("Результат:", result)

    elif choice == "2":
        data_type = input("Тип колекції (list, tuple, dict): ")
        if data_type == "list":
            data = [1, 2, 3, 4, 5]
            result = filter_data(data, lambda x: x % 2 == 0)
        elif data_type == "tuple":
            data = (5, 10, 15)
            result = filter_data(data, lambda x: x > 7)
        elif data_type == "dict":
            data = {"a": 3, "b": 10, "c": 5}
            result = filter_data(data, lambda item: item[1] >= 5)
        else:
            result = "Невідомий тип даних"
        print("Результат:", result)

    elif choice == "3":
        mode = input("Тип (числа або рядки): ")
        if mode == "числа":
            result = combine_values(1, 2, 3, initial=10)
        elif mode == "рядки":
            result = combine_values("hello", "world", separator="-")
        else:
            result = "Невідомий тип"
        print("Результат:", result)

    else:
        print("Невірний вибір.")


user_test()
