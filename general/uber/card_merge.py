import collections
from Queue import Queue


def construct_graph(cards):
    graph = collections.defaultdict(set)
    name_nodes = collections.defaultdict(set)
    email_nodes = collections.defaultdict(set)
    phone_nodes = collections.defaultdict(set)

    for card in cards:
        name, email, phone = card
        new_node = card

        if new_node in graph:
            continue
        if name not in name_nodes:
            name_nodes[name].add(new_node)
        else:
            for node in name_nodes.get(name, []):
                print 'n', node, new_node
                graph[node].add(new_node)
                graph[new_node].add(node)

        if email not in email_nodes:
            email_nodes[email] = new_node
        else:
            for node in email_nodes.get(email, []):
                print 'e', node, new_node
                graph[node].add(new_node)
                graph[new_node].add(node)

        if phone not in phone_nodes:
            phone_nodes[phone] = new_node
        else:
            for node in phone_nodes.get(phone, []):
                print 'p', node, new_node
                graph[node].add(new_node)
                graph[new_node].add(node)
        print name_nodes, phone_nodes, email_nodes
    return graph


def find_islands(graph):
    queue = Queue()
    islands = 0
    while graph:
        if queue.qsize() == 0:
            islands += 1
            node_key, connected_nodes = graph.popitem()
            for cn in connected_nodes:
                queue.put(cn)
        while queue.qsize() > 0:
            node = queue.get()
            connected_nodes = graph.pop(node)
            for cn in connected_nodes:
                queue.put(cn)
    return islands


cards = [("n1", "e1", "p1"), ("n1", "e2", "p2"), ("n3", "e1", "p5")]
for key, value in construct_graph(cards).items():
    # print key, value
    pass
# print find_islands(construct_graph(cards))
