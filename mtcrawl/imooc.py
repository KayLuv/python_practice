# crawl imooc.com using python 
from lxml import html
import requests
import time
import threading
tLock = threading.Lock()
class CourseCrawler:

    def getCourseFromUrl(self,link):
        try:
            coursePage = requests.get(link)
            tree = html.fromstring(coursePage.text)
            name = tree.xpath('//div[@class="hd"]/h2/text()')[0]
            brief = tree.xpath('//div[@class="course-brief"]/p/text()')[0]
            satisfaction = tree.xpath('//div[@class="satisfaction-degree-info"]/h4/text()')[0]
            course = Course(name,brief,satisfaction)
            with open('./result.txt',"a+") as code:
                code.write(str(course))
        except:
            print "Unexist Courses"

class Course:
    def __init__(self,name,brief,satisfaction):
        self.name = name
        self.brief = brief
        self.satisfaction = satisfaction

    def __str__(self):
        return ("Name: " +
        self.name.encode("UTF-8") +
        "\nBrief: " + 
        self.brief.encode("UTF-8") +
        "\nStaisfaction: " +
        self.satisfaction.encode("UTF-8")) + "\n\n"
crawer = CourseCrawler()
def crawler(id):
    print id
    crawer.getCourseFromUrl("http://www.imooc.com/view/"+id)
    time.sleep(3)
def main():
    print '*** Starting crawler ***'
    try:
        for id in xrange(100):
            threads = []
            for i in range(10):
                t = threading.Thread(target = crawler,args = (str(i+10*id),))
                threads.append(t)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
    except:
        pass
    print '*** crawler End ***'
if __name__ == '__main__':
    main()


