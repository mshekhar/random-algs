def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) / 2
        if x < a[mid][1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def optimalUtilization(maximumOperatingTravelDistance, forwardShippingRouteList, returnShippingRouteList):
    sorted_return_shipping_route_list = sorted(filter(lambda x: x[1] > 0, returnShippingRouteList), key=lambda x: x[1])
    optimal_val = float('-inf')
    optimal_idx = set()
    for ele in forwardShippingRouteList:
        idx = bisect_right(sorted_return_shipping_route_list, maximumOperatingTravelDistance - ele[1])
        if idx > 0:
            sol_idx = idx - 1
            sum_path = ele[1] + sorted_return_shipping_route_list[sol_idx][1]
            if sum_path > optimal_val:
                optimal_idx = {(ele[0], sorted_return_shipping_route_list[sol_idx][0])}
                optimal_val = sum_path
            elif sum_path == optimal_val:
                optimal_idx.add((ele[0], sorted_return_shipping_route_list[sol_idx][0]))
    return map(lambda x: list(x), optimal_idx)


print optimalUtilization(10000, [[1, 3000], [2, 5000], [3, 7000], [4, 10000]],
                         [[1, 2000], [2, 3000], [3, 4000], [4, 5000]])
print optimalUtilization(7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]])
print optimalUtilization(20, [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]])
print optimalUtilization(20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]])
print optimalUtilization(2, [[1, 0], [2, 0]], [[1, 0], [2, 0]])
