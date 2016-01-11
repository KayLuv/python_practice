# crawl imooc.com using python 
from lxml import html
import requests
import time
from myThread import MyThread
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
def crawler():
    for id in range (1,1000):
        print id
        crawer.getCourseFromUrl("http://www.imooc.com/view/"+repr(id))
        time.sleep(3)
def main():
    print '*** Starting crawler ***'
    threads = []
    for i in range(10):
        t = MyThread(crawler,())
        threads.append(t)
    for i in range(10):
        threads[i].start()
    for i in range(10):
        threads[i].join()
if __name__ == '__main__':
    main()