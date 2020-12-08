



def list_comp2(input_list):
    """
    make this into a list comprehension

    example:

    >> list_comp2([[1,1],[2,2]])
    >> [1,1,2,2]
    """

    # flatten_list = []
    # for sublist in input_list:
    #     for item in sublist:
            # flatten_list.append(item)

    flatten_list = [sub_list[0] for sub_list in input_list for entry in sub_list]

    return flatten_list

