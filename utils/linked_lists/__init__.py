class Node(object):
    def __init__(self):
        self._data = None
        self._next_obj = None
        self._prev_obj = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next_obj(self):
        return self._next_obj

    @next_obj.setter
    def next_obj(self, next_obj):
        self._next_obj = next_obj

    @property
    def prev_obj(self):
        return self._prev_obj

    @prev_obj.setter
    def prev_obj(self, prev_obj):
        self._prev_obj = prev_obj




