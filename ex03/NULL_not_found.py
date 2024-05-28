def NULL_not_found(obj: any) -> int:
    obj_type = obj.__class__.__name__  # Получаем имя класса объекта напрямую
    error_flag = 0

    if obj_type == "NoneType":
        print("Nothing:", obj, "<class 'NoneType'>")
    elif obj_type == "float" and str(obj) == "nan":
        print("Cheese:", obj, "<class 'float'>")
    elif obj_type == "int" and obj == 0:
        print("Zero:", obj, "<class 'int'>")
    elif obj_type == "str" and obj == '':
        print("Empty:", "<class 'str'>")
    elif obj_type == "bool" and obj is False:
        print("Fake:", obj, "<class 'bool'>")
    else:
        print("Type not Found")
        error_flag = 1  # Устанавливаем флаг ошибки в 1, если тип не найден

    return error_flag  # Возвращаем флаг ошибки

