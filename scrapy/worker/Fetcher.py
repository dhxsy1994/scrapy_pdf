import time


class Fetcher(object):
    """
    Fetcher class, fetch the website
    This class can be inherited.
    """
    def __init__(self, sleep_interval=0, repeat_max=3):
        """
        constructor
        :param sleep_interval: sleep interval seconds
        :param repeat_max: try max time
        """
        self._sleep_interval = sleep_interval
        self._repeat_max = repeat_max
        return

    def running(self, url: str, repeat_time: int, priority: int) -> (int, object):
        """
        running func
        :param url: link
        :param repeat_time: repeat times
        :param priority:
        :return:
            fetch_state:
                can be -1(fetch failed), 0(need repeat), 1(fetch success)
            content:
                which waits to be parsed, can be any object, or exception[class_name, err]
        """
        time.sleep(self._sleep_interval)
        try:
            fetch_state, content = self.fetch_url(url, repeat_time, priority)
        except Exception as err:
            # TODO: fetch repeat_time control?
            fetch_state, content = (-1 if repeat_time > self._repeat_max else 0), [self.__class__.__name__, err]

        return fetch_state, content

    def fetch_url(self, url: str, repeat_time: int, priority: int):
        """
        need override this func, otherwise raise error
        :return: fetch_state, content
        """
        raise NotImplementedError
