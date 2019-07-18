# import csv
# import json
#
# fname = "/Users/mayank.shekhar/Downloads/Copy of Sherlock Urls - Final _ All Urls with offerids.csv"
# with open(fname)as f:
#     data = csv.reader(f)
#     c = 0
#     for url, offer in data:
#         if c == 0:
#             c += 1
#             continue
#         if offer != "NULL":
#             # print url, offer
#             offers = json.loads(offer)
#             url += "&offer="
#             new_l = []
#             for offer in offers:
#                 offer_new = offer.replace("nb:mp:", "nb%3Amp%3A")
#                 new_l.append(offer_new)
#             url += ",".join(new_l)
#         print url

# "/sherlock/v1/stores/2oq/c1r/iterator?query-guide=true&pincode=642127&facets.promo%5B%5D=nb%3Amp%3A04db65aa10&facets.promo%5B%5D=nb%3Amp%3A0427208110&tags%5B%5D=western-wear-lingerie&client.tag=mobile-app-retail&products.count=10&products.type=listing&geoBrowse=enabled&query-stub=true&products.start=49&redirection=true&facet-show=all"
import os
import threading
import time


class T1(threading.Thread):
    def __init__(self, thread_id):
        self.lst = []
        self.thread_id = thread_id
        self.s = 0
        super(T1, self).__init__()

    def run(self):
        while self.s < 10:
            print self.lst, self.thread_id
            time.sleep(1)
            self.s += 1


t = T1(os.getpid())
t.start()

try:
    pid = os.fork()
except OSError:
    exit("Could not create a child process")

if pid == 0:
    print "child ", t.lst, t.thread_id, t.s
    print("In the child process that has the PID {}".format(os.getpid()))
    t.lst.append(10)
    print "child ", t.lst, t.thread_id, t.s
    exit()

t.lst.append(20)
print("In the parent process after forking the child {}".format(pid))
print "parent ", t.lst, t.thread_id, t.s
finished = os.waitpid(0, 0)
print(finished)
