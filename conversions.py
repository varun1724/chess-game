import constant


def pixels_to_list(x_coord, y_coord):

    x, y = 0, 0

    for a, row in enumerate(constant.POS_LIST):
        for b, p in enumerate(row):
            if x_coord == p[0] and y_coord == p[1]:
                x = a
                y = b
    
    return x, y
    