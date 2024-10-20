from string_count_sort import string_count_sort as scs
from data_reader import get_data
input1 = get_data("data_files/data_string.txt")
for i in scs(input1):
    print(i)