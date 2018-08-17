import Queue


class CityNode(object):
    def __init__(self):
        self.city_key = None
        self.visited = False
        self.distance = 0


def construct_city_network(arr):
    capital_node = None
    cities = {}
    for c, i in enumerate(arr):
        city_node = CityNode()
        city_node.city_key = c
        if c == i:
            capital_node = city_node
        else:
            if i not in cities:
                cities[i] = []
            cities[i].append(city_node)
    return capital_node, cities


def solution(arr):
    capital_node, cities = construct_city_network(arr)
    # print capital_node.city_key
    # print cities
    q = Queue.Queue()
    q.put(capital_node)
    dist_map = {0: 1}
    while not q.empty():
        curr_city = q.get()
        # print 'doing for ', curr_city.city_key, q.qsize()
        if curr_city.city_key in cities:
            # print cities[curr_city.city_key]
            for i in cities[curr_city.city_key]:
                if i.visited:
                    continue
                i.distance = curr_city.distance + 1
                if i.distance not in dist_map:
                    dist_map[i.distance] = 0
                dist_map[i.distance] += 1
                q.put(i)

    res = []
    for i in range(1, len(arr)):
        res.append(dist_map.get(i, 0))
    return res


print solution([9, 1, 4, 9, 0, 4, 8, 9, 0, 1])
