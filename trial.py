import re 
sourceTxt = "coming Annette   jfjfjjj fjfjfjj From Invoice Shipping 456"

shp = r"Shipping.*\d.*$"
shp1 = r"Shipping"

f_ans = re.findall(shp, sourceTxt)
print(f_ans)
