from bs4 import BeautifulSoup
import requests
from config import settings
"""
    爬虫脚本demo
    爬取MIT课程网站的PDF
    原本目的是抓取校园网内部服务某个文件夹下的所有PDF文件,由于站方下架所有PDF，只能改变方向
    
    使用DynaConf包调用全局配置
    
    author: hessen
"""


def downloadFile(download_links):
    """
    download files
    :param download_links:
    :return:
    """
    print("====={:^20}=====".format("Stared Downloading"))
    print(download_links)
    print("====={:^20}=====".format("Over Download"))


def analyzeLink_PDF(root_link, link_start):
    """
    analyze root link, parse the PDF address
    :param root_link: the PDFs website
    :param link_start: web server https address header [Https://xxxx]
    :return: all target links
    """
    # contain all target_links
    targetLinks = []

    # 伪装浏览器头部
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "PHPSESSID=0dc480ae4ac40257fd4b9ec09c517d67"}

    print("====={:^20}=====".format("Analyzing links"))

    r = requests.get(root_link, send_headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html5lib")

        index = 1
        a_tags = soup.find_all("a")
        for tag in a_tags:
            linkEnd = tag.get('href')
            if linkEnd.endswith('.pdf'):
                targetLinks.append(link_start + linkEnd)
            index += 1

    print("Toatal links {:<5d}".format(index))
    return targetLinks
    # print(index)


if __name__ == "__main__":
    # load config
    root_link = settings.root_link
    link_start = settings.link_start
    dLinks = analyzeLink_PDF(root_link, link_start)
    downloadFile(dLinks)
