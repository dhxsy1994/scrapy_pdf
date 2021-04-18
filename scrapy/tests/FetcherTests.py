import unittest
import requests
from scrapy import worker


class TestFetcher(worker.Fetcher):
    def fetch_url(self, url: str, repeat_time: int, priority: int):
        r = requests.get(url)
        if r.status_code == 200:
            return 1, (r.url, r.text)
        else:
            return 0, (r.url, r.text)


if __name__ == '__main__':
    fetcher = TestFetcher(sleep_interval=0, repeat_max=1)
    test_url = 'https://pdos.csail.mit.edu/6.824/1'
    state, content = fetcher.running(test_url, 1, 3)
    print(state, content)



