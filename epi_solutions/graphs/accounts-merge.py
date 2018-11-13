import collections


class DisjointSetNode(object):
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = self


class DisjointSet(object):
    def __init__(self):
        self.node_data_map = {}

    def find_root(self, node):
        if not isinstance(node, DisjointSetNode):
            node = self.node_data_map.get(node) or DisjointSetNode(node)
        curr = node
        parent = curr.parent
        while parent != curr:
            curr = parent.parent
            parent = curr.parent
        return curr

    def union(self, data_1, data_2):
        if data_1 not in self.node_data_map:
            self.node_data_map[data_1] = DisjointSetNode(data_1)
        if data_2 not in self.node_data_map:
            self.node_data_map[data_2] = DisjointSetNode(data_2)
        node_1 = self.node_data_map[data_1]
        node_2 = self.node_data_map[data_2]

        root_1 = self.find_root(node_1)
        root_2 = self.find_root(node_2)

        if root_1 == root_2:
            return False

        if root_1.rank >= root_2.rank:
            root_2.parent = root_1
            if root_1.rank == root_2.rank:
                root_1.rank += 1
        else:
            root_1.parent = root_2
        return True


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        ds = DisjointSet()

        for account_id, account in enumerate(accounts):
            for i in xrange(1, len(account)):
                ds.union(account_id, account[i])

        res_accounts = collections.defaultdict(set)
        for account_id, account in enumerate(accounts):
            for i in xrange(1, len(account)):
                res_accounts[ds.find_root(ds.node_data_map[account_id]).data].add(account[i])
        res = []
        for key in res_accounts:
            res.append([accounts[key][0]] + sorted(res_accounts[key]))
        return res


print Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"],
                                ["John", "johnnybravo@mail.com"],
                                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                ["Mary", "mary@mail.com"]])
