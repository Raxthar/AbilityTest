def max_list(list):
    temp = 0
    for i in list:
        if list.count(i) > temp:
            max_str = i
            temp = list.count(i)
    return max_str
