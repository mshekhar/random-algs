# -*- coding: utf-8 -*-


from utils.trees.base import NodeBase

if __name__ == "__main__":
    n0 = NodeBase(data="n0")
    n0_c1 = NodeBase(data="n0_c1")
    n0_c2 = NodeBase(data="n0_c2")
    n0_c3 = NodeBase(data="n0_c3")
    n0.add_child(n0_c1)
    n0.add_child(n0_c2)
    n0.add_child(n0_c3)

    n0_c3_c1 = NodeBase(data="n0_c3_c1")
    n0_c3_c2 = NodeBase(data="n0_c3_c2")
    n0_c3_c3 = NodeBase(data="n0_c3_c3")
    n0_c3_c4 = NodeBase(data="n0_c3_c4")
    n0_c3_c5 = NodeBase(data="n0_c3_c5")
    n0_c3_c6 = NodeBase(data="n0_c3_c6")

    n0_c3.add_child(n0_c3_c1)
    n0_c3.add_child(n0_c3_c2)
    n0_c3.add_child(n0_c3_c3)
    n0_c3.add_child(n0_c3_c4)
    n0_c3.add_child(n0_c3_c5)
    n0_c3.add_child(n0_c3_c6)

    """
       ┌n0_c1
       ├n0_c2
     n0┤
       │     ┌n0_c3_c1
       │     ├n0_c3_c2
       │     ├n0_c3_c3
       └n0_c3┤
             ├n0_c3_c6
             ├n0_c3_c5
             └n0_c3_c4
    """
    n0.pretty_print()
    """
          ┌n0_c3_c1
          ├n0_c3_c2
          ├n0_c3_c3
     n0_c3┤
          ├n0_c3_c6
          ├n0_c3_c5
          └n0_c3_c4
    """
    n0_c3.pretty_print()
