# -*- coding: utf-8 -*-


class NodeBase(object):
    def __init__(self, **kwargs):
        self.data = kwargs.get('data')
        self._children = []
        self._parent = kwargs.get('parent')

    @property
    def children(self):
        return self._children

    def modify_child(self, index, new_child):
        self._children[index] = new_child

    def add_child(self, child):
        self._children.append(child)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def get_child_count(self):
        return len(self.children)

    def get_serializable_data(self):
        return str(self.data)

    def pretty_print(self, current_node=None, indent='', last='updown'):
        current_node = current_node or self

        size_branch = {child: child.get_child_count() + 1 for child in current_node.children}
        up = sorted(current_node.children, key=lambda node: node.get_child_count() + 1)
        down = []
        while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
            down.append(up.pop())

        """ Printing of "up" branch. """
        for child in up:
            next_last = 'up' if up.index(child) is 0 else ''
            next_indent = '{0}{1}{2}'.format(indent,
                                             ' ' if 'up' in last else '│',
                                             ' ' * len(current_node.get_serializable_data()))
            self.pretty_print(current_node=child, indent=next_indent, last=next_last)

        """ Printing of current node. """
        if last == 'up':
            start_shape = '┌'
        elif last == 'down':
            start_shape = '└'
        elif last == 'updown':
            start_shape = ' '
        else:
            start_shape = '├'

        if up:
            end_shape = '┤'
        elif down:
            end_shape = '┐'
        else:
            end_shape = ''

        print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.get_serializable_data(), end_shape))

        """ Printing of "down" branch. """
        for child in down:
            next_last = 'down' if down.index(child) is len(down) - 1 else ''
            next_indent = '{0}{1}{2}'.format(indent,
                                             ' ' if 'down' in last else '│',
                                             ' ' * len(current_node.get_serializable_data()))
            self.pretty_print(current_node=child, indent=next_indent, last=next_last)
