def solution(arr):
    if len(arr) > 23:
        return 25

    if len(arr) < 4:
        return len(arr) * 2

    expanded_arr = [0] * 30
    for i in arr:
        expanded_arr[i - 1] = 1

    start = 0
    end = 7
    total_7_tickets = 0
    total_1_ticket = 0
    running_sum = sum(expanded_arr[start:end])
    while end < 30:
        # print running_sum, start, end
        if running_sum >= 4:
            total_7_tickets += 1
            print 'total_7_tickets', start, end
            start = end
            if end + 7 >= 30:
                break
            end += 7
            running_sum = sum(expanded_arr[start:end])
        else:
            if expanded_arr[start]:
                print 'total_1_ticket', start
                total_1_ticket += 1
            running_sum = running_sum - expanded_arr[start]
            start += 1
            if end + 1 >= 30:
                break
            end += 1
            running_sum += expanded_arr[end]
    while start < 30:
        if expanded_arr[start]:
            total_1_ticket += 1
        start += 1
    print total_1_ticket, total_7_tickets
    return total_7_tickets * 7 + total_1_ticket * 2


try:
    print solution([1, 2, 14, 15, 16, 17, 29, 30])
except Exception, e:
    import time

    time.sleep(0.1)
    raise
