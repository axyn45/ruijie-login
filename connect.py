import requests
import json

def connect(url,headers):
    session=requests.Session()
    rs=session.get(url=url,headers=headers,allow_redirects=False)
    headers["Cookie"]="JSESSIONID="+rs.cookies.get_dict()["JSESSIONID"]

    while rs.status_code>299 and rs.status_code<400:
        rs=session.get(url=rs.next.url,headers=headers)

    res=rs.text.split('?')[1].split("'")[0].split('"')[0]
    queryString=res

    userId=conf['uid']
    password=conf['pwd']
    service=conf['service']        # LT YD DX XYW
    operatorPwd=''
    operatorUserId=''
    validcode=''
    passwordEncrypt=False

    data={'userId':userId,'password':password,'service':service,'queryString':queryString,'operatorPwd':operatorPwd,'operatorUserId':operatorUserId,'validcode':validcode,'passwordEncrypt':passwordEncrypt}
    x=requests.post(url=url+'/eportal/InterFace.do?method=login',headers=headers,data=data)
    print(str(x.content,'utf-8'))


f=open('./config.json')
conf=json.load(f)
f.close

headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
         "Connection":"keep-alive",
         "Dnt":"1",
         }
url=conf['url']

r=requests.get(url+"/eportal/InterFace.do?method=getOnlineUserInfo",headers=headers).text
connection_status=json.loads(r)['isSuccessService']

if(connection_status!="true"):
    connect(url,headers)
    print("Successfully Connected")
else:
    print("Already Connected")

# */2 * * * * cd /root/autoconnect && ./connect.sh > ./run.log 2>&1