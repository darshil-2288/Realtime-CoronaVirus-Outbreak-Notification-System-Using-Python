from socket import timeout
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\darshil\python\projects\covidfiction\save.ico",
        timeout=10
    )
def getData(url):
    r=requests.get(url)
    return r.text




if  __name__== '__main__':
    while True:  
                #notifyMe("Hii Darshil","lets stops the spread of this virus together")
                myHtmlData=getData("https://prsindia.org/covid-19/cases")
                soup=BeautifulSoup(myHtmlData,'html.parser')
                myDataStr=""
                for tr in soup.find_all('tbody'):
                    myDataStr += tr.get_text()
                myDataStr=myDataStr[1:]    
                ItemList=myDataStr.split('\n')
                states=['31Tamil','20Madhya']
                for item in ItemList[1:36]:
                    dataList=item.split()
                    if dataList[0] in states:
                    
                        nTitle="cases of covide-19"
                        nText=f"{dataList[0]}"
                        notifyMe(nTitle,nText)
                time.sleep(20)        
