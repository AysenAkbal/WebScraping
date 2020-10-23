import requests
from bs4 import BeautifulSoup

#request modulumuz ile kazima islemi yapacagimiz web sitemizin kaynak kodunu alalim

header_param = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"}

glassdoor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm", headers = header_param)
print(glassdoor.status_code)

#status_code 403 olarak donebilir
#boyle durumlarda site guvenlik acisindan korunmustur user agent girilmesi gerekir

# yazilan header_param degeri request icerisinde headers = header_param seklinde yazilir

jobs = glassdoor.content
soup = BeautifulSoup(jobs,"html.parser")

print(soup.find("h1"))

all_jobs = soup.find_all("p" ,{"class":"h2 m-0 entryWinner pb-std pb-md-0"})
#print(all_jobs)

for job in all_jobs:
    print(job.a.text)

all_data = soup.find_all("div", { "class" : "col-6 col-lg-4 dataPoint"})

for data in all_data:
    print(data.text)