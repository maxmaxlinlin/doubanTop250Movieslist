#C:\Users\maxma>python
#Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class doubanMovie():
    def main_fuction(self):
        #create a new file named filename
        filename = "豆瓣电影top250.csv"
        page =1
        while page<25:
            headers = "movieName, movieRating, movieQuote, movieYear, movieDirector\n "
            if page==1:
                my_url='https://movie.douban.com/top250'
            else:
                my_url='https://movie.douban.com/top250?start='+str(25*(page-1))+'&filter='

            #opening up connection grabbing the page
            uClient=uReq(my_url)
            page_hrml= uClient.read()
            uClient.close()
            #html parsing grab the content and parse it into html file
            page_soup=soup(page_hrml,"html.parser")
            #grab each product
            containers= page_soup.findAll("div",{"class":"item"})
            if page ==1:
                f=open(filename,'w',encoding="utf8")
            elif page>1:
                f=open(filename,'a',encoding="utf8")
            for container in containers:
                movieName=container.findAll("span",{"title"})[0].text.strip()
                movieRating=container.findAll("span",{"rating_num"})[0].text.strip()
                movieQuote=container.findAll("p",{"quote"})[0].text.strip()
                movieYear=self.getYear(container.findAll("p",{""})[0].text.strip())
                movieDirector=self.getDirector(container.findAll("p",{""})[0].text.strip())
                print("Movie: "+movieName+". Rating: "+movieRating+", quote:"+movieQuote+" Year: "+movieYear+""+movieDirector)
                f.write(movieName+","+movieRating+","+movieYear+","+movieQuote+","+movieDirector+"\n")
            page+=1
        f.close()



    def getDirector(self,ooo):
        for index in range(len(ooo)):
                if ooo[index]==":":
                         for  index2 in range(index,len(ooo)):
                            if ooo[index2]=='主':
                                global director
                                director=ooo[index+1:index2]
        return director



    def getYear(self,kkk):
        for index in range(len(kkk)):
             if kkk[index]=='1'and kkk[index+1]=='9':
                 year=kkk[index:index+4]
             if kkk[index]=='2'and kkk[index+1]=='0':
                 year=kkk[index:index+4]
        return year


movie = doubanMovie()
movie.main_fuction()
