import collections


def sort_hotels(keywords, hotel_ids, reviews):
    # print keywords, hotel_ids, reviews
    counter = collections.Counter()
    c = 0
    keywords_set = set(keywords.split(" "))
    while c < len(hotel_ids):
        res = 0
        for word in reviews[c].split(" "):
            res += int(word in keywords_set)
        counter[hotel_ids[c]] += res
        c += 1
    return map(lambda x: x[0], sorted(counter.items(), key=lambda x: x[1], reverse=True))


print sort_hotels("breakfast beach citycenter location metro view staff price", [1, 2, 1, 1, 2],
                  ['This hotel has a nice view of the citycenter. The location is perfect.',
                   'The breakfast is ok. Regarding location, it is quite far from citycenter but price is cheap so it is worth.',
                   'Location is excellent, 5 minutes from citycenter. There is also a metro station very close to the hotel.',
                   "They said I couldn't take my dog and there were other guests with dogs! That is not fair.",
                   'Very friendly staff and good cost-benefit ratio. Location is a bit far from citycenter.'])
