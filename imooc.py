# crawl imooc.com using python 
from lxml import html
import requests
import time

class CourseCrawler:

    def getCourseFromUrl(self,link):
        try:
            coursePage = requests.get(link)
            tree = html.fromstring(coursePage.text)
            name = tree.xpath('//div[@class="hd"]/h2/text()')[0]
            brief = tree.xpath('//div[@class="course-brief"]/p/text()')[0]
            satisfaction = tree.xpath('//div[@class="satisfaction-degree-info"]/h4/text()')[0]
            course = Course(name,brief,satisfaction)
            print course
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
        self.satisfaction.encode("UTF-8"))
crawer = CourseCrawler()
for id in range (100,500):
    print id
    crawer.getCourseFromUrl("http://www.imooc.com/view/"+repr(id))
    time.sleep(3)
