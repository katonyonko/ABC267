import io
import sys

_INPUT = """\
6
4 3
3 1 4 2
1 2
1 3
4 1
7 13
464 661 847 514 74 200 188
5 1
7 1
5 7
4 1
4 5
2 4
5 2
1 3
1 6
3 5
1 2
4 6
2 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  G=[[] for _ in range(N)]
  for i in range(M):
    U,V=map(lambda x: int(x)-1, input().split())
    G[U].append(V)
    G[V].append(U)
  cost=[sum([A[G[i][j]] for j in range(len(G[i]))]) for i in range(N)]
  heap=[]
  for i in range(N):
    heappush(heap,(cost[i],i))
  ans=0
  removed=set()
  while heap:
    x,d=heappop(heap)
    removed.add(d)
    if x==cost[d]:
      ans=max(ans,x)
      for i in range(len(G[d])):
        cost[G[d][i]]-=A[d]
        if G[d][i] in removed: continue
        heappush(heap,(cost[G[d][i]],G[d][i]))
  print(ans)