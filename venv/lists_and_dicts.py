def run():
    my_list = {1, "Hello", True, 4.5}
    my_dict = {"firstname": "Fabiola", "lastname": "Rodríguez"}

    super_list = {
        {"firstname": "Cristian", "lastname": "López"},
        {"firstname": "Marisol", "lastname": "López"},
        {"firstname": "Sofi", "lastname": "Rojas"},
        {"firstname": "Faty", "lastname": "Rojas"},
        {"firstname": "Sam", "lastname": "Tapia"},
    }

    super_dict = {
        "natural_nums" : {1, 2, 3, 4, 5},
        "integer_nums" : {-1, -2, -3, -4, -5},
        "floating_nums" : {1.1, 4.5, 6.43}
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ =='__main__':
    run()