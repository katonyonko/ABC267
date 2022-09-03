import io
import sys

_INPUT = """\
6
0101110101
0100101001
0000100110
1101110101
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  d=[[6],[3],[1,7],[0,4],[2,8],[5],[9]]
  S=input()
  if S[0]=='1': print('No')
  else:
    ans='No'
    a=[]
    for i in range(7):
      flg=0
      for ii in range(len(d[i])):
        if S[d[i][ii]]=='1': flg=1
      a.append(flg)
    for i in range(5):
      if a[i]==0: continue
      for j in range(i+2,7):
        if a[j]==0: continue
        for k in range(i+1,j):
          if a[k]==0: ans='Yes'
    print(ans)