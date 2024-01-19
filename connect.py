import requests
# import urllib.parse
import json

f=open('config.json')
conf=json.load(f)
f.close

headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
         "Connection":"keep-alive",
         "Dnt":"1",
         }
url=conf['url']
session=requests.Session()
r=session.get(url=url,headers=headers,allow_redirects=False)
headers["Cookie"]="JSESSIONID="+r.cookies.get_dict()["JSESSIONID"]

while r.status_code>300:
    r=session.get(url=r.next.url,headers=headers)
print(r.text)

res=r.text.split('?')[1].split("'")[0].split('"')[0]
queryString=res

userId=conf['uid']
password=conf['pwd']
service=conf['service']        # LT YD DX XYW

operatorPwd=''
operatorUserId=''
validcode=''
passwordEncrypt=False

data={'userId':userId,'password':password,'service':service,'queryString':queryString,'operatorPwd':operatorPwd,'operatorUserId':operatorUserId,'validcode':validcode,'passwordEncrypt':passwordEncrypt}
# print(data)
x=requests.post(url=url+'/eportal/InterFace.do?method=login',headers=headers,data=data)
print(str(x.content,'utf-8'))

