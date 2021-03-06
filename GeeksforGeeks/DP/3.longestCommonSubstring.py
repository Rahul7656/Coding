''' Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
'''

def longestCommonSubstr(S1, S2, n, m):
    dp = [[0 for x in range(m+1)]
            for l in range(n+1)]

    res = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            res = max(res,dp[i][j])
    return res

if __name__=="__main__":
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'

    n = len(X)
    m = len(Y)

    print("Length of longest common substring: ")
    print(longestCommonSubstr(X,Y,n,m))  
