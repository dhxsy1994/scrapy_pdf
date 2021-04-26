import sys


class Saver(object):
    """
    class of saver
    """
    def __init__(self, save_pipe=sys.stdout):
        """
        default to stdout
        :param save_pipe: save point
        """
        self._save_pipe = save_pipe
        return

    def running(self, url: str, deep: int, item: object, priority: int):
        """
        working function
        :param url:
        :param deep:
        :param item:
        :param priority:
        :return:
        """
        try:
            save_state, save_result = self.save_item(url, deep, item, priority)
        except Exception as err:
            save_state, save_result = -1, [self.__class__.__name__, err]

    def save_item(self, url: str, deep: int, item: object, priority: int):
        """
        must override
        :param url:
        :param deep:
        :param item:
        :param priority:
        :return:
        """
        raise NotImplementedError

