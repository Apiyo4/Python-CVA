import re
sourceTxt = 'the quick brown fox 10%  145.6 Invoice : 333700'
# totalAmount = 400
# # prcnt = r"Invoice\s[a-zA-Z]?\s?\:\s\d.*$"
# prcnt = r"Invoice.*\.*$"
# prcnt1 =  r"INV.*\-\d.*$"
prcnt1 =  r"[0-9.]+\d*?"


# if(re.findall(prcnt, sourceTxt)):
#     f_ans = re.findall(prcnt, sourceTxt)[0]
# elif (re.findall(prcnt1, sourceTxt)):
#     f_ans = re.findall(prcnt1, sourceTxt)[0]
# else:
#     f_ans=0
prctg = re.findall(prcnt1, sourceTxt)


print(prctg )




# invoice 2
#  def invoice_2(sourceTxt):
                
                # global new_d
                # arr = ["Invoice","Invoice Number", "Invoice number"]
               
                # for i in arr :
                #     if  i in list(new_d.keys()):
                #         borders = new_d[i]
                #         break
            #         else:
            #             borders = ""
            #     return borders
           
            # def get_all_numbers(sourceTxt):
            #     ans = re.findall(r"[0-9.]+\d*?", sourceTxt)
            #     return ans
            
            # def Get_invoice_in_pdf_2(sourceTxt):
            #     brdr = invoice_2(sourceTxt)
            #     nums = get_all_numbers(sourceTxt) 
            #     num_bdr = []
            #     global new_d
            #     if nums:
            #         if isinstance(nums, str) and nums in list(new_d.keys()):
            #             num_bdr = new_d[nums]
            #         else :
            #             num_bdr = '' 
            #     else:
            #         pass
            #     print(num_bdr,new_d.keys())
            #     pass