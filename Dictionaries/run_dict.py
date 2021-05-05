# dictionaries
def __main__():
    # define a dictionary:
    my_dict = {"brand": "BMW", "model": "X1", "year": "2019"}

    # get the value of the key
    key1_value = my_dict["brand"]
    key2_value = my_dict.get("model")
    print(key1_value)
    print(key2_value)

    # get all the keys
    print(my_dict.keys())

    # get all the values
    print(my_dict.values())

    # modify value and see changed value
    my_dict["year"] = "2021"
    print(my_dict.get("year"))
    print(my_dict.values())


__main__()
