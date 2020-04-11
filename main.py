from plyer import notification
import requests
from bs4 import BeautifulSoup
import plyer



def Noti(title,message):
    notification.notify(
        title= title, 
        message=message,
        timeout =5
        )

def getData(Url):

    r = requests.get(Url)
    return r.text


if __name__ == "__main__":
    Noti("Covid19", "http://covid.gov.pk/")

    MyHtmlData= getData("http://covid.gov.pk/")


    soup = BeautifulSoup(MyHtmlData, 'html.parser')
   # print(soup.prettify())
    
    for link in soup.find_all('a'):
        print(link.get('href'))

        