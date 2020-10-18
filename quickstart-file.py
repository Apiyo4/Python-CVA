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

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

print("===== Batch Read File - remote =====")

remote_image_handw_text_url = "https://slicedinvoices.com/pdf/wordpress-pdf-invoice-plugin-sample.pdf"

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
if get_handw_text_results.status == OperationStatusCodes.succeeded:
    for text_result in get_handw_text_results.analyze_result.read_results:
       
        for sourceTxt in text_result.lines:
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
               
                asd = max(f_ans) if f_ans else 0  
                    
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
    print(hijA)
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
    
    
    d["date"] = min(abcA)
    d["total_amount"] = max(defgA)[0]
    d["vat"] = vat_2ans if int(hijA[0][0:-1]) /100 * d["total_amount"] == 0 else int(hijA[0][0:-1]) /100 * d["total_amount"]
   
    print( d)
print("Apiyo")

