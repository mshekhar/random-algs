def split_sms(as_words, break_length=24):
    c = 1
    suffix_format = ' ({0}/{1})' if break_length == 24 else ' ({0}/0{1})'

    chunk_length = 0
    chunk = []
    all_chunks = []

    for i in as_words:
        if break_length == 24 and c > 9:
            # print 'calling double'
            return split_sms(as_words, break_length=break_length - 1)

        max_len = break_length - (0 if c <= 9 else 1)
        if chunk_length + len(i) <= max_len:
            chunk_length += len(i) + 1
            chunk.append(i)
        else:
            all_chunks.append(" ".join(chunk) + suffix_format.format(c, c))
            c += 1
            chunk_length = 0
            chunk = []

            chunk_length += len(i) + 1
            chunk.append(i)

    if break_length == 24 and c > 9:
        # print 'calling double'
        return split_sms(as_words, break_length=break_length - 1)

    if len(chunk) > 0:
        all_chunks.append(" ".join(chunk) + suffix_format.format(c, c))

    for i in range(len(all_chunks)):
        break_point = -2 if c < 9 else -3
        all_chunks[i] = all_chunks[i][:break_point] + str(c) + ')'

    for i in all_chunks:
        print len(i), '   ', i
    return all_chunks


def split_string_into_multiple():
    s = raw_input()
    if len(s) > 30:
        return len(split_sms(s.split(' ')))
    else:
        return 1


split_sms("The best lies are always mixed with a little truth".split(" "))
print '\n\n\n'
split_sms(
    "The best lies are always mixed with a little truth The best lies are always mixed with a little truth The best lies are always mixed with a little truth The best lies are always mixed with a little truth The best lies are always mixed with a little truth The best lies are always mixed with a little truth".split(
        " "))

# print split_string_into_multiple("The best lies are always mixed with a little truth")
# print split_string_into_multiple("There is no creature on earth half so terrifying as a truly just man!!!!!")
# print split_string_into_multiple("You know nothing, Jon Snow")
