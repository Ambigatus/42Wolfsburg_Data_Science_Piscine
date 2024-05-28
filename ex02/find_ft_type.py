def all_thing_is_obj(obj: any) -> int:
    obj_type = obj.__class__.__name__  # Get the object's class name directly
    # __class__ - directly taking class of object
    # __name__ - directly taking name of object, without using type() function

    if obj_type == "list":
        print("List :", "<class 'list'>")
    elif obj_type == "tuple":
        print("Tuple :", "<class 'tuple'>")
    elif obj_type == "set":
        print("Set :", "<class 'set'>")
    elif obj_type == "dict":
        print("Dict :", "<class 'dict'>")
    elif obj_type == "str":
        print(f"{obj} is in the kitchen :", "<class 'str'>")
    else:
        print("Type not found")

    return 42
