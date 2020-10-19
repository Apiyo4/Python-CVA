# import re

# sourceTxt = "I love math Order"
# prcnt = r"Purchase.*\d.*$"
# prcnt1 = r"Ord.*\d.*$"
# prcnt2 = r"Ord.*\D"
# if (re.findall(prcnt, sourceTxt)):
#     ans = re.findall(prcnt, sourceTxt)[0]
#     f_ans_split = ans.split()
#     for i in f_ans_split:
#         if i.isnumeric():
#             f_ans = i
#         else:
#             f_ans = ''
# elif(re.findall(prcnt1, sourceTxt)):
#     ans = re.findall(prcnt1, sourceTxt)[0]
#     f_ans_split = ans.split()
#     for i in f_ans_split:
#         if i.isnumeric():
#             f_ans = i
#         else:
#             f_ans = ''
# elif (re.findall(prcnt2, sourceTxt)):
#     f_ans = re.findall(prcnt2, sourceTxt)[0]
# else:
#     f_ans = ''
# print(f_ans)


