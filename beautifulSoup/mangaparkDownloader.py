from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen,Request  # Web client
from urllib.request import urlretrieve  # get URL raw Data
from pathlib import Path
from fpdf import FPDF
import sys,os,shutil
class MangaparkDownloader:
    baseURL="https://www.readlightnovel.org/"
    novelName=""
    chaptersURL=""
    def __init__(self,name):
        self.novelName = name.replace(" ","-")
        self.chaptersURL = self.baseURL+self.novelName
        self.chaptersPage = self.soupPetition(self.chaptersURL)
        
    
    def soupPetition(self,url):
        # opens the connection and downloads html page from url
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urlopen(request)
        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        page_soup = soup(response.read(), "html.parser")
        response.close()
        return page_soup
    
    def getAllChaptersURLS(self):
        # chapters are divided on blocks of ul inside divs but each ul holds the calss chapter-chs
        chapterLists=self.chaptersPage.findAll("ul",{"class":"chapter-chs"})
        urls=[]
        for chapterList in chapterLists:
            links = chapterList.findAll("a")
            if (links):
                for link in links:
                    urls.append(link["href"])
        return urls
    
    def getChapterText(self,chapterURL):
        chapterText = self.soupPetition(chapterURL).findAll("div",{"class":"hidden"})[0].text
        #chapterText=""
        #for chapterPiece in chapterPieces:
        #    chapterText += chapterPiece.text+"\n"
        print("obtained text for: "+chapterURL)
        return chapterText
    
    def downloadNovel(self,destination):
        urls = self.getAllChaptersURLS()
        chaptersTexts = []
        for url in urls:
            chaptersTexts.append(self.getChapterText(url))
        self.createBook(chaptersTexts,destination)
    
    def createBook(self,textChapters,destination):
        destination +="\\"+self.novelName
        pdfPath = destination+"\\"+self.novelName+".pdf"
        # if folder already existed,it deletes it
        if os.path.exists(destination):
            shutil.rmtree(destination, ignore_errors=True)
        os.mkdir(destination)
        
        # set UTF8 fonts
        import fpdf
        fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'fonts'))
        pdf = fpdf.FPDF()
        pdf.add_font("NotoSans", style="", fname="NotoSans-Regular.ttf", uni=True)
        pdf.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
        pdf.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
        pdf.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True)
        pdf.set_font("NotoSans", size=12)
        for textChapter in textChapters:
            pdf.add_page()
            pdf.set_xy(10.0,10.0)    
            pdf.set_text_color(76.0, 32.0, 250.0)
            pdf.multi_cell(0,10,textChapter)
        pdf.output(pdfPath,'F')
        
        

MyObject =MangaparkDownloader(sys.argv[1]) 
MyObject.downloadNovel("C:\\Users\\Sergio\\Desktop\\twilio\\beautifulSoup")
#MyObject.getChapterText("https://www.readlightnovel.org/release-that-witch/chapter-13")
#MyObject.createBook([MyObject.getChapterText("https://www.readlightnovel.org/release-that-witch/chapter-13")],"C:\\Users\\Sergio\\Desktop\\twilio\\beautifulSoup")
