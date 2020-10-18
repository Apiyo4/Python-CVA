import re
arr = ["123", "the word", "234", "3,000"]
sourceTxt = "The amount is 3 000.05"
# /^\d*\.?\d*$/
lst = r"\d.*,\d{3}\.?\d*$"
spc = r"\d.*\s\d{3}\.\d*$"
# lst = r"^\d+(?:,\d*)?$"
ans = []
ttl = []
f_ans = re.findall(spc, sourceTxt)[0].split(',')
# for i in arr:
#     if(re.findall(lst, i)):
#         ans.extend(re.findall(lst, i))
#     elif i.isnumeric() and len(i)<4:
#         ans.extend(i)
# if ans:
#     for i in ans:
#         rem_c = i.split(',')
#         ttl.append("".join(rem_c))
#         f_ans = max(ttl) 
        
print(f_ans)
            
# # num = "1,234"
# # lst = r".*,\d{3}$"
# # ans=[]
# # ttl = []
# # for i in arr:
# #     if(re.findall(lst, i)):
# #         ans.append(i)
# #     elif i.isnumeric():
# #         ans.append(i)
# # for i in ans:
# #     rem_c = i.split(',')
# #     ttl.append("".join(rem_c))
# # print(max(ttl), ans) 

# # if length(i) > 3 and 


# # txt = "The rain in Spain"
# # x = re.search("^The.*Spain$", txt)

# # arr1 = "1,234"
# # rem_c = arr1.split(',')
# # ttl = ''
# # for i in rem_c:
# #     ttl= ttl + i
# # print(ttl)
