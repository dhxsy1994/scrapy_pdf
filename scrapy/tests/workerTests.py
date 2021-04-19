import unittest
from bs4 import BeautifulSoup
import datetime
import requests
from scrapy import worker


class TestFetcher(worker.Fetcher):
    def fetch_url(self, url: str, repeat_time: int, priority: int):
        # TODO: make http get header
        r = requests.get(url)
        # TODO: return code logic
        if r.status_code == 200:
            return 1, (r.status_code, r.url, r.text)
        else:
            return 0, (r.status_code, r.url, r.text)


class TestParser(worker.Parser):
    def parse_html(self, url: str, content: object, deep: int, priority: int):
        """
        Parser imp
        :param url:
        :param content:
        :param deep:
        :param priority:
        :return:
        """
        status_code, url_now, html_text = content
        soup = BeautifulSoup(html_text, "html5lib")

        target_links = []
        link_start = "https://pdos.csail.mit.edu/6.824/"
        # TODO crawl the pdf process not 100% right
        index = 0
        a_tags = soup.find_all("a")
        for tag in a_tags:
            href_content = tag.get('href')
            if href_content.endswith('.pdf'):
                if href_content.startswith('http'):
                    target_links.append(href_content)
                    index += 1
                else:
                    target_links.append(link_start + href_content)
                    index += 1
            else:
                continue

        print("Total links {:<5d}".format(index))
        # TODO: return code logic
        return 1, target_links, {"url": url, "title": 'Web PDF files', "datetime": datetime.datetime.now()}


if __name__ == '__main__':
    fetcher = TestFetcher()
    parser = TestParser()
    test_url = "https://pdos.csail.mit.edu/6.824/schedule.html"

    f_state, content = fetcher.running(test_url, 1, 1)
    if f_state == 1:
        p_state, url_list, item = parser.running(test_url, content, 1, 1)
        print(url_list)
    else:
        print("Fetch error!")



