import time


class Parser(object):
    """
    parser fetched html content
    """
    def __init__(self, max_deep=-1):
        """
        constructor
        :param max_deep:
        """
        self._max_deep = max_deep

    def running(self, priority: int, deep: int, content: object) -> (int, list, object):
        """

        :return:
        """

    def parse_html(self, priority: int, url: str, content: object):
        """
        parse the content of url, must override this func
        :return: parse_state, url_list, to_save items
        """
        raise NotImplementedError
