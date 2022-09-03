import io
import sys

_INPUT = """\
6
4 2
5 4 -1 8
10 4
-3 1 -4 1 -5 9 -2 6 -5 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  dp=[[-(10**20)]*M for _ in range(N)]
  dp[0][0]=A[0]
  for i in range(N-1):
    for j in range(M):
      dp[i+1][j]=max(dp[i+1][j],dp[i][j])
      if j>0:
        dp[i+1][j]=max(dp[i+1][j],dp[i][j-1]+(j+1)*A[i+1])
      else:
        dp[i+1][j]=max(dp[i+1][j],A[i+1])
  print(dp[-1][-1])