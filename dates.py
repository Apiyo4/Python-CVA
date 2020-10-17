import calendar
import re
# for i in calendar.month_abbr:
#     print(i)
sourceTxt = "12/12/2020" 
# date_expr = r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:])
# print(date_expr)
# print(re.findall(date_expr, sourceTxt))
# fruits = [1,2,3,4]
# print(fruits[1:2])

date_format = [ r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_name[1:]),r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_name[1:])]

dats = []
f_dats = ''

for i in date_format:
    # print(i)
    if(re.findall(i, sourceTxt)):
        dats.extend(re.findall(i, sourceTxt))
    else:
        ans = re.findall('([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|2[0-9]|3[0-9])(.|-|\/)(20[0-9][0-9])',sourceTxt)
        ans_f = [''.join(ans[i]) for i in range(len(ans)) if i != []]
        dats.extend(ans_f)

for sublist in dats:
    if any(sublist): 
        f_dats = sublist
        break   
print(f_dats)      
# if isinstance(f_dats,str):
#     print(f_dats)
# else:
#     print(f_dats[0])