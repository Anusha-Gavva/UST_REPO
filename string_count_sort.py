input1="which is better python 2 or python 3"
dict1={}
out=input1.split()
for i in out:
    dict1[i] = out.count(i)
res_tup = sorted(dict1.items())
for i in res_tup:
    print(i)