def count_score_combinations(score_options, total_score):
    score_possibility_count = {_: 0 for _ in xrange(0, total_score + 1)}
    score_possibility_count[0] = 1
    for score in score_options:
        for i in xrange(score, total_score + 1):
            score_possibility_count[i] += score_possibility_count[i - score]
    return score_possibility_count[total_score]


print count_score_combinations([2, 3, 7], 12)
