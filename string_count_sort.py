def string_count_sort(input_string):
    dict1={}
    out=input_string.split()
    for i in out:
        dict1[i] = out.count(i)
    res_tup = sorted(dict1.items())
    return res_tup