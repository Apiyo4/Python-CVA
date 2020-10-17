arr = [[[], [], []],[[], [], [4]],[[], [], []],[[], [], [5]],[[], [], []]]
f_dats = []
# for sublist in dats:
#     if any(sublist): 
#         f_dats = [f_dats, *sublist]
#         break         

# for i in f_dats:
#     if i:
#         print(i[0])
for sublist in arr:
    if any(sublist): 
        f_dats = sublist
        break   
    # print(f_dats) 
if isinstance(f_dats,str):
    return f_dats
else:
    for i in f_dats:
        if any(i):
            return i[0]

