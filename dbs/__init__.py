def chooseFleets(fleets):
    sol = []
    for num in fleets:
        if num % 2 != 0:
            sol.append(0)
        else:
            sol.append((num / 4) + 1)
    return sol
