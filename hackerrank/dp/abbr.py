def print_dp(v1, v2, dp):
    s = "\n" + str(v1) + ", " + str(v2) + "\n"
    for _ in dp:
        s += repr(_) + "\n"
    return s


def abbreviation(a, b):
    dp = [[False for _ in b] for _ in a]
    # for i in range(len(a)):
    #     if a[i].islower() or not val_matched:
    #         val_matched = True
    #         dp[i][0] = True
    for i in range(len(a)):
        dp[i][0] = any(x.upper() == b[0] for x in a[:i + 1]) \
                   and sum(1 for x in a[:i + 1] if x == b[0]) <= 1 \
                   and not any(x.isupper() and x != b[0] for x in a[:i + 1])
    # print dp
    for i in xrange(1, len(a)):
        for j in xrange(1, len(b)):
            if a[i].upper() == b[j]:
                dp[i][j] = dp[i - 1][j - 1] or dp[i][j] or dp[i - 1][j]
            elif a[i].islower():
                dp[i][j] = dp[i - 1][j]
            # print a[i].islower(), i - 1, j, dp[i - 1][j], dp[i][j], print_dp(a[i], b[j], dp)
    return 'YES' if dp[-1][-1] else 'NO'


print abbreviation("AbcdBCFD", "ABCD")
print abbreviation("XXVVnDEFYgYeMXzWINQYHAQKKOZEYgSRCzLZAmUYGUGILjMDET", "XXVVDEFYYMXWINQYHAQKKOZEYSRCLZAUYGUGILMDETQVWU"), "NO"
print abbreviation("PVJSNVBDXABZYYGIGFYDICWTFUEJMDXADhqcbzva", "PVJSNVBDXABZYYGIGFYDICWTFUEJMDXAD"), "YES"
print abbreviation("QOTLYiFECLAGIEWRQMWPSMWIOQSEBEOAuhuvo", "QOTLYFECLAGIEWRQMWPSMWIOQSEBEOA"), "YES"
print abbreviation("DRFNLZZVHLPZWIupjwdmqafmgkg", "DRFNLZZVHLPZWI"), "YES"
print abbreviation("SLIHGCUOXOPQYUNEPSYVDaEZKNEYZJUHFXUIL", "SLIHCUOXOPQYNPSYVDEZKEZJUHFXUIHMGFP"), "NO"
print abbreviation("RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGGnscruaa", "RYASPJNZEFHEORROXWZFOVDWQCFGRZLWWXJVMTLGG"), "YES"
print abbreviation("AVECtLVOXKPHIViTZViLKZCZAXZUZRYZDSTIHuCKNykdduywb", "AVECLVOXKPHIVTZVLKZCZAXZUZRYZDSTIHCKN"), "YES"
print abbreviation("wZPRSZwGIMUAKONSVAUBUgSVPBWRSTJZECxMTQXXA", "ZPRSZGIMUAKONSVAUBUSVPBWRSTJZECMTQXXA"), "YES"
print abbreviation("SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFYyxu", "SYIHDDSMREKXOKRFDQAOZJQXRIDWXPYINFZCEFY"), "YES"
print abbreviation("EIZGAWWDCSJBBZPBYVNKRDEWVZnSSWZIw", "EIZGAWWDCSJBBZPBYVNKRDEWVZSSWZI"), "YES"
print abbreviation("CEFYyxu", "CEFY")
