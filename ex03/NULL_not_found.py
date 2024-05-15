def NULL_not_found(obj: any) -> int:

    if obj is None:
        print("Nothing:", obj, type(obj))
    elif isinstance(obj, float) and obj != obj:
        print("Cheese:", obj, type(obj))
    elif obj == 0 and not isinstance(obj, bool):  # isinstance checks this variable is not bool type
        print("Zero:", obj, type(obj))
    elif obj == '':
        print("Empty:", type(obj))
    elif obj is False:  # because of that
        print("Fake:", obj, type(obj))
    else:
        print("Type not Found")
        return 1

    return 0
