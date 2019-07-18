import urlparse


def parse_params(key, value, params_split):
    k2 = key.split('.', 1)
    if k2[0]:
        if len(k2) == 1:
            params_split[k2[0]] = value
        else:
            if k2[0] not in params_split:
                params_split[k2[0]] = {}
            if len(k2) > 1:
                params_split[k2[0]][k2[1]] = value


def parse_moriarty_access_logs(log_file_name):
    iter_params_split = {}
    filter_params_split = {}
    paths = set()
    methods = set()
    with open('/Users/mayank.shekhar/Downloads/' + log_file_name) as f:
        for c, line in enumerate(f):
            line_split = line.split(' ')
            method = line_split[3]
            methods.add(method)
            d1 = urlparse.urlparse(line.split(' ')[4])
            if d1.path.endswith('iterator'):
                paths.add(d1.path.split('/')[-1])
                for k, v in urlparse.parse_qs(d1.query).items():
                    parse_params(key=k, value=v, params_split=iter_params_split)
                # iterator_keys = iterator_keys | set(urlparse.parse_qs(d1.query).keys())
            elif d1.path.endswith('filter'):
                paths.add(d1.path.split('/')[-1])
                for k, v in urlparse.parse_qs(d1.query).items():
                    parse_params(key=k, value=v, params_split=filter_params_split)
                # filter_keys = iterator_keys | set(urlparse.parse_qs(d1.query).keys())
            else:
                pass

            if c % 50000 == 0:
                print 'paths ', c, paths
                print 'filter ', c, iter_params_split
                print 'iterator ', c, filter_params_split
                print 'methods ', c, methods
    return iter_params_split, filter_params_split


iter_params_split_1, filter_params_split_1 = parse_moriarty_access_logs("moriarty_access.log")
iter_params_split_2, filter_params_split_2 = parse_moriarty_access_logs("moriarty_access_2.log")

import pdb

pdb.set_trace()

# def split_params(params, params_split):
#     for k in params:
#         k2 = k.split('.', 1)
#         if k2[0]:
#             if k2[0] not in params_split:
#                 params_split[k2[0]] = {}
#             if len(k2) > 1:
#                 params_split[k2[0]][k2[1]] = None


# iter_params_split = {}
# split_params(iter_params, iter_params_split)
# print iter_params_split
# filter_params_split = {}
# split_params(filter_params, filter_params_split)
# print filter_params_split
print len(set(iter_params_split_2.keys()) - set(iter_params_split_1.keys()))
print len(set(filter_params_split_2.keys()) - set(filter_params_split_1.keys()))

[(k, iter_params_split_2[k]) for k in set(iter_params_split_2.keys()) - set(iter_params_split_1.keys())]

r1 = [('asin', ['b073vkq5y4']), ('psig', ['aovvaw3ip2x6udsb_ov3ltt_0xmb']), ('src_id', ['fromsearch__0']),
 ('fxFed', ['true']), ('cache-get-false', ['true']), ('pid', ['botf7m5xnfxah7nr']), ('cache-disable', ['true']),
 ('utm_source', ['whatsapp']), ('seller', ['a38299i3xfydy']), ('facet', {'price_range.from': ['199']}),
 ('url', ['https //www com/pin/688698967987106783/', 'https com/pin/688698967987106783/']),
 ('ved', ['2ahukewig2pb8yvxhahwhinakhzbicqoqjhx6bagbeam']),
 ('ust', ['1556637021828103', '1556637021828103https com/urlsa=i']), ('utm_medium', ['appshare']), ('debug', ['true']),
 ('uact', ['8']), ('cad', ['rja'])]


[(k, filter_params_split_2[k]) for k in set(filter_params_split_2.keys()) - set(filter_params_split_1.keys())]
r2 = [('facet', {'price_range.from': ['199']}), ('context', {'internal': ['true']})]

# tmp = {}
# for (k, v) in r2:
#     if isinstance(v, list) and len(v) == 1:
#         tmp[k] = v[0]
#     else:
#         tmp[k] = v
# import json
# json.dumps(tmp)

{
    "facet": {
        "price_range.from": ["199"]
    },
    "context": {
        "internal": ["true"]
    }
}