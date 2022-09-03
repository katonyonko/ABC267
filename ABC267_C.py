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
  from itertools import accumulate
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  AA=[0]+list(accumulate(A))
  ans=-(10**100)
  tmp=sum([(i+1)*A[i] for i in range(M)])
  for i in range(N-M):
    ans=max(ans,tmp)
    tmp+=M*A[M+i]-AA[M+i]+AA[i]
  ans=max(ans,tmp)
  print(ans)