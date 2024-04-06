from datetime import date,datetime
import requests
import pandas as pd
def get_exchange(code_="USD", date_=None):
    """
     code_ = 통화코드 
         예) USD 
     date_ = 예) '2024-01-02'
    """
    payload = {"ajax": "true",
            "curCd": "",
            "pbldDvCd": "0",
            "pbldSqn": "",
            "hid_key_data": "",
            "inqKindCd": "1",
            "hid_enc_data": "",
            "requestTarget": "searchContentDiv",}
    #날짜 형식 검사
    try:
        datetime.strptime(date_,"%Y-%m-%d")
    except:
        print("값 확인해!!") #return -1 값이 없으므로
        # return -1
        date_=str(date.today())  #오늘날짜가져오기
    
    
    
    payload['tmpInqStrDt'] = date_
    payload['inqStrDt'] = date_.replace("-", "")
    url = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"
    r = requests.post(url, data=payload)
    exchange = pd.read_html(r.text)[0]
    exchange.columns = ["_".join(x[:2]) for x in exchange.columns]
    return exchange.loc[exchange['통화_통화'].str.find(f"{code_.upper()}") > -1, '현찰_파실 때'].iloc[0,0]
# 웹으로하면 restapi 
# 이제 이거 내장함수로 변환


from datetime import date
if __name__=="__main__":
    print(f"오늘 usd 환율은 : {get_exchange('usd',str(date.today()))}")
    
    

