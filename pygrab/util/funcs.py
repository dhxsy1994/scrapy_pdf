
from urllib import parse as urllib_parse
import os
import re

"""
some convenient funcs for url operations
"""


def check_url_legal(url):
    """
    check a url is legal or not
    :param url: input a url string
    :return: Ture or False
    """
    # pattern is ignore the Capital and Small: 'A' or 'a'
    pattern = re.compile(r'''http[s]?:[^\s]+?\.[^\s]+''', flags=re.IGNORECASE)
    if pattern.match(url) is not None:
        return True
    else:
        return False


def url_join(url, base_url, encoding='utf-8'):
    """
    joined a legal url from a url string
    :param url:
    :param base_url:
    :param encoding: default is utf-8
    :return:
    """
    # parse.quote is function to encode the special characters. there include some typical.
    return urllib_parse.urljoin(base_url, urllib_parse.quote(url, safe="%/:=&?~#+!$,;'@()*[]|", encoding=encoding))


def get_url_params(url, encoding='utf-8'):
    """
    parse url params to two parts, main_body and query_body
    :param url:
    :param encoding: default is utf-8
    :return: main_body, query_body [array]
    """
    # Parse a URL into six components, returning a 6-item named tuple.
    parts = urllib_parse.urlparse(url, allow_fragments=True)

    main_part = (parts.scheme, parts.netloc, parts.path, parts.params, '', '')
    # TODO: merge or not ?
    query_part = parts.query
    return urllib_parse.urlunparse(main_part), urllib_parse.parse_qs(query_part, encoding=encoding)


def get_num_from_string(string, ignore_sign=False):
    """
    get a num from the string
    :param string:
    :param ignore_sign: dont care '+, -'
    :return:
    """
    res = re.search(r"(?P<sign>-?)(?P<num>\d+(\.\d+)?)", string.replace(",", ""), flags=re.IGNORECASE)
    if res is not None:
        return float((res.group("sign") if not ignore_sign else "") + res.group("num"))
    else:
        return None


def get_string_strip(string, replace_char=' '):
    """
    get the string strip character
    :param string:
    :param replace_char:
    :return:
    """
    if re.sub(r"\s+", replace_char, string, flags=re.IGNORECASE).strip() is not None:
        return string
    else:
        return ""


if __name__ == "__main__":
    """
    funcs tester, for correct
    """
    # check url
    url = "https://blog.csdn.net/xuyawei_xyw/article/details/85050606"
    url2 = "https://zhuanlan.zhihu.com/p/143238944"
    url3 = "https://www.szu.edu.cn/"
    print(check_url_legal(url))
    print(check_url_legal(url2))
    print(check_url_legal(url3))
    # url_join
    print(url_join("#thanks.htm", url3, encoding='utf-8'))
    # get_url_params
    print(get_url_params("https://my.hupu.com/search?q=%E8%8B%B9%E6%9E%9C%E6%BE%B3%E9%97%A8&fid=&type=undefined"
                         "&sortby=general"))
    # get_num_from_string
    print(get_num_from_string("1,000,000,000.3889"))

