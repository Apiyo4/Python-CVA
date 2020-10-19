import re 
sourceTxt = "coming Annette Invoice jfjfjjj fjfjfjj From"
prt = r"\d.*"
# >>> print(re.match(r'From\s+', 'Fromage amk'))
# None
# >>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')  
# <re.Match object; span=(0, 5), match='From '>
# f_ans = re.match(prt, sourceTxt)[0]
for i in sourceTxt:
    s= ''
    if i.isnumeric():
        continue
    else:
        s='yes'
print(s)


# print(f_ans.group())


# frm = r"From :"
# frm1 = r"From"
# frm2= r"Invoice"

# # f_ans = re.findall(frm, sourceTxt)[0]
# if(re.findall(frm, sourceTxt)):
#     f_ans = re.findall(frm, sourceTxt)[0]
# elif(re.findall(frm1, sourceTxt)):
#     f_ans = re.findall(frm1, sourceTxt)[0]
# elif(re.findall(frm2, sourceTxt)):
#     f_ans = re.findall(frm2, sourceTxt)[0]
# else:
#     f_ans = 0
# print(f_ans)