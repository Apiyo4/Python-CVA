# imports
import re
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import calendar

def InvAns(strUrl):
    
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    else:
        print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


    # print("===== Batch Read File - remote =====")

    remote_image_handw_text_url = strUrl

    recognize_handw_results = computervision_client.read(remote_image_handw_text_url,  raw=True)

    operation_location_remote = recognize_handw_results.headers["Operation-Location"]

    operation_id = operation_location_remote.split("/")[-1]

    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)
    d = {}
    abcA = []
    defgA = []
    hijA = []
    klmA = []
    nopA= []
    qrsA = []
    uvwA = []
    flat_list = []
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            
            for sourceTxt in text_result.lines:
                new_d = {}
                new_d[sourceTxt.text] = sourceTxt.bounding_box
                flat_list.append(sourceTxt.text)


                def Get_shipping_in_pdf(sourceTxt):
                    # print(cf)
                    shp = r"Shipping.*\d.*$"
                    shp1 = r"Shipping"
                    if (re.findall(shp, sourceTxt)):
                        ans = re.findall(shp, sourceTxt)[0]
                        f_ans_split = ans.split()
                        for i in f_ans_split:
                            if i.isnumeric():
                                print(i)
                                f_ans = i
                            else:
                                f_ans = ''
                    elif (re.findall(shp1, sourceTxt)):
                        f_ans = re.findall(shp1, sourceTxt)[0]   
                    else:
                        f_ans = "0"
                    return f_ans
                
                def Get_company_in_pdf(sourceTxt):
                    frm = r"From:"
                    frm1 = r"From"
                    frm2= r"Invoice"
                    if(re.findall(frm, sourceTxt)):
                        f_ans = re.findall(frm, sourceTxt)[0]
                    elif(re.findall(frm1, sourceTxt)):
                        f_ans = re.findall(frm1, sourceTxt)[0]
                    elif(re.findall(frm2, sourceTxt)):
                        f_ans = re.findall(frm2, sourceTxt)[0]
                    else:
                        f_ans = 0
                    # print(f_ans)    
                    return f_ans
                
                def Get_order_in_pdf(sourceTxt):
                    prcnt = r"Purchase.*\d.*$"
                    prcnt1 = r"Ord.*\d.*$"
                    prcnt2 = r"Ord.*\D"
                    if (re.findall(prcnt, sourceTxt)):
                        ans = re.findall(prcnt, sourceTxt)[0]
                        f_ans_split = ans.split()
                        for i in f_ans_split:
                            if i.isnumeric():
                                f_ans = i
                            else:
                                f_ans = ''
                    elif(re.findall(prcnt1, sourceTxt)):
                        ans = re.findall(prcnt1, sourceTxt)[0]
                        f_ans_split = ans.split()
                        for i in f_ans_split:
                            if i.isnumeric():
                                f_ans = i
                            else:
                                f_ans = ''
                    elif (re.findall(prcnt2, sourceTxt)):
                        f_ans = re.findall(prcnt2, sourceTxt)[0]   
                    else:
                        f_ans = ''
                    return f_ans

                def Get_invoice_in_pdf(sourceTxt):
                    
                    prcnt = r"Invoice.*\d.*$"
                    prcnt1 =  r"INV.*\-\d.*$"
                    f_ans = ''
                    if (re.findall(prcnt1, sourceTxt)):
                        f_ans = re.findall(prcnt1, sourceTxt)[0]
                    elif(re.findall(prcnt, sourceTxt)):
                        ans = re.findall(prcnt, sourceTxt)[0]
                        f_ans_split = ans.split()
                        for i in f_ans_split:
                            if i.isnumeric():
                                f_ans = i 
                            else:
                                f_ans = '' 
                    else:
                        f_ans = '' 
                    return f_ans

                def Get_vat_in_document(sourceTxt):
                    
                    prcnt = r"([0-9][0-9]%$|[0-9]%$)"

                    if(re.findall(prcnt, sourceTxt)):
                        f_ans = re.findall(prcnt, sourceTxt)[0]
                    else:
                        f_ans = 0
        
                    return f_ans
                
                def Get_total_amount_in_pdf(sourceTxt):
                    lst = r"\d.*,\d{3}\.?\d*$"
                    dcm = r"\d.*\..?\d*$"
                    spc = r"\d.*\s\d{3}\.\d*$"
                    ans=[]
                    ttl = []
                    f_ans = []
                    if(re.findall(lst, sourceTxt)):
                        ans.extend(re.findall(lst, sourceTxt))
                    elif re.findall(dcm, sourceTxt):
                        ans.extend(re.findall(dcm, sourceTxt))
                    elif re.findall(spc, sourceTxt):
                        ans.extend(re.findall(spc, sourceTxt))    
                    if ans:
                        for i in ans:
                            rem_c = i.split(',')
                            try:
                                ttl.append(float("".join(rem_c)))
                            except ValueError:
                                pass    
                
                    if ttl == []:
                        pass
                    else:
                        f_ans.extend(ttl)   
                        
                    return f_ans
                    
                def Get_date_in_pdf(sourceTxt):
                    date_format = [ r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_name[1:]),r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_name[1:])]

                    dats = []
                    f_dats = ''
                    


                    for i in date_format:
                        if(re.findall(i, sourceTxt)):
                            dats.extend(re.findall(i, sourceTxt))
                        else:
                            ans = re.findall(r'([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|2[0-9]|3[0-9])(.|-|\/)(20[0-9][0-9])',sourceTxt)
                            ans_f = [''.join(ans[i]) for i in range(len(ans))]
                            dats.extend(ans_f)
                    for sublist in dats:

                        if any(sublist): 
                            f_dats = sublist
                            break   
                    return f_dats

                
                abc = Get_date_in_pdf(sourceTxt.text)
                defg = Get_total_amount_in_pdf(sourceTxt.text)
                hij = Get_vat_in_document(sourceTxt.text)
                klm = Get_invoice_in_pdf(sourceTxt.text)
                nop = Get_order_in_pdf(sourceTxt.text)
                qrs = Get_company_in_pdf(sourceTxt.text)
                uvw = Get_shipping_in_pdf(sourceTxt.text)
                
                
                if abc=="" and defg=="" and hij:
                    continue
                elif abc:
                    abcA.append(abc)
                    continue
                elif  defg:
                    defgA.append(defg)
                    continue
                elif hij:
                    hijA.append(hij)
                elif klm:
                    klmA.append(klm)
                elif nop:
                    nopA.append(nop) 
                elif qrs:
                    print(qrs)
                    qrsA.append(qrs)
                elif uvw:
                    uvwA.append(uvw) 


            def get_index_ord(inp, lst): 
            
                indx = lst.index(inp)
                f_ans = lst[indx + 1]
                return f_ans
            def get_indx_purchase(inp, lst):
                indx = int(lst.index(inp))
                f_ans = ''
                for i in lst[indx:indx+4]:
                    if i.isnumeric():
                        f_ans = i
                        break
                    else:
                        f_ans =''

                return f_ans
            def get_company_name(inp,lst):

                idx = int(lst.index(inp))
                f_ans = ''
                f_indx = int(idx + 1)
                for i in lst[f_indx]:
                    if i.isnumeric():
                        f_ans = lst[f_indx + 1]
                    else:
                        f_ans = lst[f_indx]
                return f_ans
            def get_company_name_2(sublist, lst):
                f_ans = ''
                print(sublist)
                if "From:" in sublist:
                    f_ans = get_company_name("From:", lst)
                    print(f_ans)
                elif "From" in sublist:
                    f_ans = get_company_name("From", lst)
                elif "Invoice" in sublist:
                    f_ans = get_company_name("Invoice", lst)
                else:
                    f_ans =  lst[0]
                return f_ans  
            def Get_shipping_cost(inp, lst):
                f_ans = ''
                inpt = ''
                if inp:
                    inpt = inp[0]
                else:
                    inpt = "0"
            
                if inpt.isnumeric():
                    f_ans = inpt
                else:
                    indx = lst.index(inpt)
                    f_indx = int(indx + 1)
                    f_ans = lst[f_indx]
                    if f_ans.isnumeric():
                        f_ans = lst[f_indx]
                    else:
                        f_ans = 0
                return f_ans
            
            order_2 = get_index_ord(nopA[0], flat_list) 
            company_name = get_company_name_2(qrsA, flat_list)
            purchase_2 = get_indx_purchase("Invoice", flat_list)
                
        def vat_2(inp):
            ans_vat = ''
            new_set = list(set([i[0] for i in inp]))
            new_set.sort()
            if  new_set[-1] - new_set[-2] in new_set:
                ans_vat = new_set[-1] - new_set[-2] 
            else:
                ans_vat = 0
            return ans_vat
        vat_2ans = vat_2(defgA)
        shipping = int(Get_shipping_cost(uvwA, flat_list))
                
        
        # print(shipping)
        
        d["date"] = min(abcA)
        d["total_amount"] = max(defgA)[0]
        d["vat"] = vat_2ans - shipping if int(hijA[0][0:-1]) /100 * d["total_amount"] == 0 else int(hijA[0][0:-1]) /100 * d["total_amount"] - shipping
        d["invoice_number"] = klmA[0] if klmA[0] else purchase_2
        d["purchase_order_number"] = nopA[0] if nopA[0].isnumeric() else order_2
        d["supplier_name"] = company_name
    # print("Apiyo", d)
    return d

print(InvAns("https://slicedinvoices.com/pdf/wordpress-pdf-invoice-plugin-sample.pdf"))


