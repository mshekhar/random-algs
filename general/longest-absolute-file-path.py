class Solution(object):
    def is_directory(self, ele):
        return len(ele.split(".")) == 1

    def is_file(self, ele):
        return len(ele.split(".")) == 1

    def get_next_word(self, i, input):
        tab_count = 0
        if i != 0:
            i += 1
        while i < len(input) and input[i] == "\t":
            tab_count += 1
            i += 1

        s = []
        while i < len(input) and input[i] != "\n":
            s.append(input[i])
            i += 1

        return i, "".join(s), tab_count

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        parents = []
        current = None
        max_file_len = float('-inf')
        i = 0
        while i < len(input):
            i, current, tab_count = self.get_next_word(i, input)
            print i, current, tab_count, parents
            if not current:
                break
            if self.is_directory(current):
                while len(parents) != tab_count:
                    parents.pop()
                if parents:
                    parents.append((current, len(current) + parents[-1][1]))
                else:
                    parents.append((current, len(current)))

            else:
                if parents:
                    max_file_len = max(max_file_len, len(parents) + len(current) + parents[-1][1])
                else:
                    max_file_len = max(max_file_len, len(current))
        return 0 if max_file_len == float('-inf') else max_file_len


# print Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
# print Solution().lengthLongestPath(
#     "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
# print Solution().lengthLongestPath("dir")
# print Solution().lengthLongestPath("")

print Solution().lengthLongestPath("dir\n    file.txt")
