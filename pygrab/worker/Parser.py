

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
        return

    def running(self, url: str, content: object, deep: int, priority: int) -> (int, list, object):
        """
        running parse_html
        :return:
            parse_state: state of parse
            url_list: Web content url, form a list
            item: _dict type
        """
        try:
            parse_state, url_list, item = self.parse_html(url, content, deep, priority)
        except Exception as err:
            parse_state, url_list, item = -1, [self.__class__.__name__, err], None

        return parse_state, url_list, item

    def parse_html(self, url: str, content: object, deep: int, priority: int):
        """
        parse the content of url, must override this func
        content: fetcher return object, contain a web page
        deep: the page depth
        :return:
            The return item will more flexible, we can define a web content data item like:
                {"url": url, "title": title.group("title").strip(), "datetime": datetime.datetime.now()}
            Or, we can only define a type of web PDF file item like:
                {"url": url, "title": 'Web PDF files', 'datetime': datetime.datetime.now()}
        """
        raise NotImplementedError
