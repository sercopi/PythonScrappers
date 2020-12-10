from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen,Request  # Web client
from urllib.request import urlretrieve  # get URL raw Data
import sys,os
# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = sys.argv[1]
destination = sys.argv[2]
threadName=page_url.split("/")[-1]
print(page_url)
os.mkdir(destination+"\\"+threadName)
# opens the connection and downloads html page from url
headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}

request = Request(page_url)
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
response = urlopen(request)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(response.read(), "html.parser")
response.close()
comments = page_soup.findAll("a", {"class": "fileThumb"})
imageCounter=1
for comment in comments:
    imageURL = comment["href"]
    urlretrieve("https:"+imageURL,destination+"\\"+threadName+"\\"+str(imageCounter)+".jpg")
    imageCounter+=1