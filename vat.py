import re
sourceTxt = 'the quick brown fox 10%'
totalAmount = 400
prcnt = r"([0-9][0-9]%$|[0-9]%$)"

if(re.findall(prcnt, sourceTxt)):
    f_ans = re.findall(prcnt, sourceTxt)[0]
else:
    f_ans = 0
prctg = f_ans[0:-1]


print(prctg)