class Solution(object):
    def __init__(self):
        self.idx = 0

    def merge_dicts(self, d1, d2):
        res_dict = {}
        for k, v in d1.iteritems():
            if k in d2:
                res_dict[k] = v + d2[k]
            else:
                res_dict[k] = v

        for k, v in d2.iteritems():
            if k not in res_dict:
                res_dict[k] = v
        return res_dict

    def extract_string(self, item_stack, res_count, multiplier):
        s = ""
        continue_ele_find = True
        while continue_ele_find:
            if not item_stack:
                continue_ele_find = False
                continue
            if ord('a') <= ord(item_stack[-1]) <= ord('z'):
                s = item_stack.pop() + s
            else:
                s = item_stack.pop() + s
                if s not in res_count:
                    res_count[s] = 0
                res_count[s] += multiplier
                continue_ele_find = False

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        res_count = {}
        item_stack = []
        while self.idx < len(formula):
            if formula[self.idx] == '(':
                idx_val = self.idx
                self.idx += 1
                tmp_res_count = self.countOfAtoms(formula)
                multiplier_str = ""
                while self.idx < len(formula) and ord('1') < ord(formula[self.idx]) <= ord('9'):
                    multiplier_str += formula[self.idx]
                    self.idx += 1
                self.idx -= 1
                multiplier = int(multiplier_str) if multiplier_str else 1
                for k in tmp_res_count:
                    tmp_res_count[k] = multiplier * tmp_res_count[k]
                res_count = self.merge_dicts(res_count, tmp_res_count)
            elif formula[self.idx] == ')':
                self.idx += 1
                break
            elif ord('A') <= ord(formula[self.idx]) <= ord('Z'):
                self.extract_string(item_stack, res_count, 1)
                item_stack.append(formula[self.idx])
            elif ord('1') < ord(formula[self.idx]) <= ord('9'):
                multiplier_str = ""
                # print 'int check ', formula[self.idx]
                while self.idx < len(formula) and ord('0') <= ord(formula[self.idx]) <= ord('9'):
                    multiplier_str += formula[self.idx]
                    self.idx += 1
                self.idx -= 1
                multiplier = int(multiplier_str) if multiplier_str else 1
                self.extract_string(item_stack, res_count, multiplier)
            else:
                item_stack.append(formula[self.idx])
            self.idx += 1

        if item_stack:
            self.extract_string(item_stack, res_count, 1)
        return res_count


print Solution().countOfAtoms("H2O")
print Solution().countOfAtoms("MgOH20")
print Solution().countOfAtoms("H2O2He3Mg4H5He6")
print Solution().countOfAtoms("Mg(OH)2")
print Solution().countOfAtoms("K4(ON(SO3)2)2")
