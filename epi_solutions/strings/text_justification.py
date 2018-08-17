class Solution(object):
    def get_spaces_dist(self, chunk, chunk_word_count, max_len):
        spaces_count = max_len - chunk_word_count
        remaining_spaces = spaces_count
        spaces = [0] * (len(chunk) - 1)
        # print 'remaining_spaces', remaining_spaces, chunk, chunk_word_count, max_len, spaces
        loop_exit = False if spaces else True
        while not loop_exit:
            for i in range(len(spaces)):
                if remaining_spaces > 0:
                    spaces[i] += 1
                    remaining_spaces -= 1
                else:
                    loop_exit = True
                    break

        spaces.append(remaining_spaces)
        # print chunk, spaces
        return spaces

    def balance_spaces_in_chunk(self, chunk, chunk_word_count, max_len):
        spaces = self.get_spaces_dist(chunk, chunk_word_count, max_len)
        return ''.join([a + ' ' * b for a, b in zip(chunk, spaces)])

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        chunk_length = 0
        chunk_word_count = 0
        chunk = []
        all_chunks = []

        for i in words:
            if chunk_length + len(i) <= maxWidth:
                chunk_length += len(i) + 1
                chunk_word_count += len(i)
                chunk.append(i)
            else:
                all_chunks.append(self.balance_spaces_in_chunk(chunk, chunk_word_count, maxWidth))

                chunk_length = 0
                chunk_word_count = 0
                chunk = []

                chunk_length += len(i) + 1
                chunk_word_count += len(i)
                chunk.append(i)
        if chunk:
            text_ = " ".join(chunk)
            end_space = " " * (maxWidth - len(text_))
            all_chunks.append(text_ + end_space)

        return all_chunks


print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
print Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                              "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
