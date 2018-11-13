class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)

        ptr_1 = 0

        i = 0
        while i < len(dominoes):
            # print i, dominoes[i], dominoes
            # if i == 3:
            #     import pdb
            #     pdb.set_trace()
            if dominoes[i] == 'R':
                ptr_1 = i

                i += 1
                while i < len(dominoes) and dominoes[i] == '.':
                    i += 1
                if i >= len(dominoes) or dominoes[i] == 'R':
                    while ptr_1 < min(len(dominoes), i):
                        dominoes[ptr_1] = 'R'
                        ptr_1 += 1
                else:
                    j = ptr_1
                    ptr_1 += 1
                    # print 'lR case'
                    while ptr_1 < i:
                        if ptr_1 - j < i - ptr_1:
                            dominoes[ptr_1] = 'R'
                        elif ptr_1 - j > i - ptr_1:
                            dominoes[ptr_1] = 'L'
                        ptr_1 += 1
                    # print 'lR case exit', ptr_1, i
                continue
            elif dominoes[i] == 'L':
                while ptr_1 < i:
                    if dominoes[ptr_1] == '.':
                        dominoes[ptr_1] = 'L'
                    ptr_1 += 1
            i += 1

        return "".join(dominoes)


print Solution().pushDominoes(".L.R...LR..L..")
print Solution().pushDominoes("RR.L")
print Solution().pushDominoes("")
