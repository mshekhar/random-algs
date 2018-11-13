import string


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        next_required_alphabet = {l: [] for l in string.lowercase}
        for i in d:
            if i:
                next_required_alphabet[i[0]].append((i, 0))
        longest_word = ""
        for c, i in enumerate(s):
            # print i, c
            next_alphabet_list = []
            while next_required_alphabet[i]:
                nxt, nxt_idx = next_required_alphabet[i].pop()
                if nxt_idx == len(nxt) - 1:
                    # import pdb
                    # pdb.set_trace()
                    if len(nxt) > len(longest_word) or (len(nxt) == len(longest_word) and nxt < longest_word):
                        longest_word = nxt
                else:
                    # print 'moving from', nxt[nxt_idx], 'to', nxt[nxt_idx + 1], nxt_idx + 1, s[c], c
                    if i == nxt[nxt_idx + 1]:
                        next_alphabet_list.append((nxt, nxt_idx + 1))
                    else:
                        next_required_alphabet[nxt[nxt_idx + 1]].append((nxt, nxt_idx + 1))
            next_required_alphabet[i] = next_alphabet_list

        return longest_word


print Solution().findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"])
print Solution().findLongestWord(s="abpcplea", d=["z"])

s = "wsmzffsupzgauxwokahurhhikapmqitytvcgrfpavbxbmmzdhnrazartkzrnsmoovmiofmilihynvqlmwcihkfskwozyjlnpkgdkayioieztjswgwckmuqnhbvsfoevdynyejihombjppgdgjbqtlauoapqldkuhfbynopisrjsdelsfspzcknfwuwdcgnaxpevwodoegzeisyrlrfqqavfziermslnlclbaejzqglzjzmuprpksjpqgnohjjrpdlofruutojzfmianxsbzfeuabhgeflyhjnyugcnhteicsvjajludwizklkkosrpvhhrgkzctzwcghpxnbsmkxfydkvfevyewqnzniofhsriadsoxjmsswgpiabcbpdjjuffnbvoiwotrbvylmnryckpnyemzkiofwdnpnbhkapsktrkkkakxetvdpfkdlwqhfjyhvlxgywavtmezbgpobhikrnebmevthlzgajyrmnbougmrirsxi"
j = "jpthiudqzzeugzwwsngebdeai"
print Solution().findLongestWord(s=s, d=[j])
# jidx = 0
# for i in xrange(len(s)):
#     if s[i] == j[jidx]:
#         jidx += 1
#     if jidx >= len(j):
#         break
# print jidx, i, len(s), len(j)
