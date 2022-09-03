import io
import sys

_INPUT = """\
6
5
1 2
2 3
3 4
3 5
3
2 2
5 3
3 3
10
1 2
2 3
3 5
2 8
3 4
4 6
4 9
5 7
9 10
6
1 1
2 2
3 3
4 4
5 5
3 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs(G,s):
    inf=10**8
    D=[inf]*len(G)
    P=[-1]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          P[y]=x
          D[y]=D[x]+1
          dq.append(y)
    return P,D

  N=int(input())
  G=[[] for _ in range(N)]
  for _ in range(N-1):
    A,B=map(int,input().split())
    A-=1; B-=1
    G[A].append(B)
    G[B].append(A)
  P0,D0=bfs(G,0)
  s=D0.index(max(D0))
  P1,D1=bfs(G,s)
  t=D1.index(max(D1))
  P2,D2=bfs(G,t)
  PP1=[P1[i//18] for i in range(N*18)]
  for i in range(17):
    for j in range(N):
      PP1[j*18+i+1]=PP1[PP1[j*18+i]*18+i]
  PP2=[P2[i//18] for i in range(N*18)]
  for i in range(17):
    for j in range(N):
      PP2[j*18+i+1]=PP2[PP2[j*18+i]*18+i]
  Q=int(input())
  for i in range(Q):
    U,K=map(int,input().split())
    U-=1
    if max(D1[U],D2[U])<K: print(-1)
    else:
      now=U
      if D1[U]>=K:
        for j in range(18):
          if (K>>j)&1==1:
            now=PP1[now*18+j]
        print(now+1)
      else:
        for j in range(18):
          if (K>>j)&1==1:
            now=PP2[now*18+j]
        print(now+1)